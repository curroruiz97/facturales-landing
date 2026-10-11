#!/usr/bin/env python3
"""Comprobaciones estáticas del sitio de Facturales (solo biblioteca estándar de Python 3).

Uso:
    python3 scripts/check-site.py            # revisa todo el sitio
    python3 scripts/check-site.py -v         # además lista los ficheros que pasan
    python3 scripts/check-site.py index.html pricing.html   # solo esas páginas

Termina con código 1 si alguna comprobación falla. Pensado para ejecutarse antes de cada
commit y en CI (.github/workflows/landing-ci.yml).

Qué comprueba, para cada .html:
  * estructura: etiquetas bien anidadas y balance de <div>, <html lang="es">, título y
    meta description presentes y únicos entre páginas, un único <h1>;
  * enlaces: todo href/src/srcset/url() local existe; sin href="#" vacíos ni anclas
    internas rotas;
  * limpieza: sin restos de plantilla ("Brevon", "Gramentheme", "Neotix", "lorem ipsum")
    salvo en comentarios de licencia de CSS/JS;
  * privacidad: ninguna petición a hosts externos (solo se admite app.facturales.es y los
    enlaces <a>), ni en HTML ni en CSS ni en el JS propio;
  * veracidad del contenido: ninguna de las afirmaciones retiradas por política (ver
    CONTENT_RULES) ni los CTAs a rutas antiguas de la app;
  * SEO: título de 50-60 caracteres y descripción de 120-160, canonical correcto, Open Graph
    y Twitter Card con imagen 1200x630 existente, JSON-LD válido y coherente con la página
    (sin aggregateRating), sitemap.xml y robots.txt, y noindex en la 404;
  * accesibilidad: skip link y un único <main id="main">, jerarquía de encabezados sin
    saltos ni encabezados vacíos, <img> con alt útil, botones/enlaces con nombre accesible,
    iconos decorativos con aria-hidden, sin manejadores onclick en línea y ningún
    "outline: none !important";
  * iconos: todo fa-* usado está en el subconjunto de Font Awesome (assets/css/icons.css);
  * movimiento y color: foco visible y prefers-reduced-motion definidos, sin autoplay de menos
    de 6 s ni ScrollSmoother en el JS propio, sin los naranjas sueltos que unificaron los
    tokens y tokens de color con contraste suficiente (>= 4,5:1).
"""
from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent

SITE_URL = "https://facturales.es"
# Páginas que no se indexan (deben llevar noindex y no aparecer en el sitemap).
NOINDEX_PAGES = {"404.html"}
# Artículos del blog (llevan JSON-LD Article y fecha de revisión visible).
ARTICLES = {
    "verifactu-2027-guia-autonomos-pymes.html",
    "factura-electronica-vs-verifactu.html",
    "contabilidad-negocio-7-pasos.html",
}
# Naranjas sueltos que la paleta unificada (main.css) reemplazó.
STRAY_COLORS = ("#ec8228", "#ff7300", "#d4a017")

# Hosts a los que el sitio puede hacer peticiones (recursos). Los <a> externos se admiten siempre.
ALLOWED_REQUEST_HOSTS = {"app.facturales.es"}

# Directorios que no se revisan.
SKIP_DIRS = {".git", ".claude", ".github", "node_modules", "assets", "scripts", "__pycache__"}

# Ficheros JS/CSS propios (no librerías de terceros) cuyo contenido se revisa en busca de
# peticiones externas y restos de plantilla. Las librerías de terceros solo se revisan en
# busca de "Brevon/Gramentheme/Neotix" fuera de comentarios.
FIRST_PARTY_ASSETS = [
    "assets/js/header-include.js", "assets/js/main.js", "assets/js/home.js",
    "assets/js/pricing.js", "assets/js/orbit-cta.js",
]
# CSS de terceros (no se revisan sus reglas de foco ni sus colores)
VENDOR_CSS = {"bootstrap.min.css", "animate.css", "swiper-bundle.min.css", "all.min.css"}

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param",
    "source", "track", "wbr",
}
# Etiquetas cuyo cierre se puede omitir en HTML válido: no se exige que estén cerradas.
OPTIONAL_END = {"li", "p", "td", "th", "tr", "thead", "tbody", "tfoot", "option", "dt", "dd", "colgroup"}
# Etiquetas SVG que se escriben autocerradas o sin cierre explícito en algunos sitios.
SVG_SELF = {"path", "circle", "rect", "line", "polyline", "polygon", "ellipse", "stop", "use"}

# Atributos que provocan una petición (recurso) según la etiqueta.
REQUEST_ATTRS = {
    "script": ["src"],
    "img": ["src", "srcset"],
    "source": ["src", "srcset"],
    "video": ["src", "poster"],
    "audio": ["src"],
    "iframe": ["src"],
    "embed": ["src"],
    "object": ["data"],
    "track": ["src"],
    "input": ["src"],
    "form": ["action"],
}
LINK_REL_REQUESTS = {
    "stylesheet", "preload", "prefetch", "modulepreload", "icon", "shortcut", "apple-touch-icon",
    "manifest", "preconnect", "dns-prefetch", "mask-icon", "image_src",
}

# Reglas de veracidad: (expresión regular sin distinguir mayúsculas, motivo).
CONTENT_RULES = [
    # Veri*Factu / AEAT
    (r"homologad", "afirma software 'homologado' (no existe homologación; ver política Veri*Factu)"),
    (r"100\s?%\s*(legal|compatible|seguro y legal)", "afirma '100% legal/compatible'"),
    (r"programas?\s+certificados?|software\s+certificad", "habla de programas/software 'certificados'"),
    (r"configurado\s+de\s+serie|viene\s+configurado", "afirma que Veri*Factu viene 'configurado de serie'"),
    (r"puede\s+enviar\s+los\s+registros|env[ií]a\s+(los\s+)?registros\s+(de\s+forma\s+segura\s+)?a\s+la\s+aeat",
     "afirma que Facturales envía registros a la AEAT (aún no hay envío)"),
    (r"cumplimos\s+con\s+(toda|la)\s+(la\s+)?normativa|cumple\s+con\s+todas\s+las\s+normativas",
     "afirma cumplimiento normativo completo"),
    # Funcionalidades inexistentes en la app
    (r"\bstock\b|\bstocks\b|inventario|multialmac|almacenes|almac[eé]n\b", "menciona stock/inventario (no existe en la app)"),
    (r"albar[aá]n|albaranes|proforma", "menciona albaranes/proformas (no existen)"),
    (r"trello|mailchimp|\bslack\b", "menciona integraciones inexistentes (Trello/Mailchimp/Slack)"),
    (r"\bacademia\b", "menciona 'Academia' (no existe)"),
    (r"presupuestos\s+ilimitad[oa]s",
     "afirma 'presupuestos ilimitados' (el plan solo limita las facturas: no se promete nada sobre el límite de presupuestos)"),
    (r"facturas\s+y\s+presupuestos\s*(emitidos\s*)?(/|al)\s*mes|l[ií]mite\s+mensual\s+compartido",
     "dice que los presupuestos cuentan para el tope mensual (la app solo cuenta las facturas emitidas)"),
    (r"recordatorios?\s+(autom[aá]ticos?|de\s+pago)", "afirma recordatorios automáticos de pago (no existen)"),
    (r"facturas\s+recurrentes", "afirma facturas recurrentes (no existen)"),
    (r"conecta\s+tu\s+banco|conexi[oó]n\s+bancaria|open\s*banking", "afirma conexión bancaria (no existe)"),
    (r"confirmaci[oó]n\s+de\s+lectura|vista\s+y\s+cobrada|ve\s+y\s+acepta|visto\s+y\s+aceptado|firma\s+digital",
     "afirma seguimiento de lectura/aceptación o firma en documentos (no existe)"),
    (r"categorizaci[oó]n\s+autom[aá]tica|inteligencia\s+artificial|clasifica\s+gastos\s+autom[aá]ticamente",
     "afirma categorización automática/IA en el OCR (no existe)"),
    (r"alertas\s+autom[aá]ticas|informes\s+(autom[aá]ticos|en\s+pdf|descargables\s+en\s+pdf)",
     "afirma alertas o informes PDF automáticos (no existen)"),
    # Gratis / sin tarjeta
    (r"sin\s+tarjeta", "afirma 'sin tarjeta' (el alta pide método de pago)"),
    (r"gratis\s+para\s+siempre|acceso\s+(al\s+programa\s+es\s+)?gratuito|cuenta\s+gratuita|cuenta\s+gratis",
     "afirma acceso/cuenta gratuita (no hay plan gratuito)"),
    (r"(empieza|empezar|comienza|comenzar|reg[ií]strate|registrarse|crear\s+cuenta|prueba)\s+gratis\b(?!\s+durante)",
     "CTA 'gratis' sin la prueba de 14 días (usa 'Prueba 14 días' / 'Crear cuenta')"),
    # Prueba social y urgencia
    (r"\+\s?10\.000|10\.000\s+(negocios|aut[oó]nomos|empresas)", "cifra de clientes sin respaldo"),
    (r"\b4[.,]8\s?/\s?5\b|software\s+de\s+facturaci[oó]n\s+n\.?\s?[º°o]?\s?1\b", "valoración/ranking sin respaldo"),
    (r"miles\s+de\s+(aut[oó]nomos|empresas|negocios)", "'miles de…' sin respaldo"),
    (r"mar[ií]a\s+garc[ií]a|carlos\s+mart[ií]nez|laura\s+fern[aá]ndez|javier\s+torres|laura\s+mart[ií]nez",
     "testimonio ficticio retirado"),
    (r"horas\s+(semanales|al\s+mes|a\s+la\s+semana)|\bahorra\s+(hasta\s+)?\+?\d+\s*h", "cifra de horas ahorradas sin respaldo"),
    (r"oferta\s+de\s+lanzamiento|countdown", "cuenta atrás / oferta de lanzamiento (urgencia falsa)"),
    (r"-\s?30\s?%", "descuento anual '-30%' (el real es del 23-25 %)"),
    # CTAs y enlaces a la app: rutas canónicas sin .html
    (r"app\.facturales\.es/(signup|signin|politica-de-privacidad|condiciones-legales|politica-de-cookies|aviso-legal)\.html",
     "enlace a la app con .html (usa la ruta canónica sin extensión)"),
]

errors: list[str] = []


def err(path: Path | str, line: int | None, msg: str) -> None:
    rel = path if isinstance(path, str) else str(path.relative_to(ROOT))
    errors.append(f"{rel}{':' + str(line) if line else ''}  {msg}")


class PageParser(HTMLParser):
    """Recoge estructura, metadatos y referencias de una página."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int]] = []
        self.lang: str | None = None
        self.title = ""
        self._in_title = False
        self.description: str | None = None
        self.h1_count = 0
        self.refs: list[tuple[str, str, int, str]] = []  # (tag, attr, linea, valor)
        self.request_refs: list[tuple[str, int, str]] = []  # (descripción, linea, valor)
        self.ids: set[str] = set()
        self.names: set[str] = set()
        self.dead_links: list[int] = []
        self.hash_targets: list[tuple[int, str]] = []
        self.styles: list[tuple[int, str]] = []
        self._in_style = False
        self._style_buf: list[str] = []
        self._style_line = 0
        self.imbalance: list[tuple[int, str]] = []
        self.div_open = 0
        self.div_close = 0
        # SEO y accesibilidad
        self.metas: list[dict] = []
        self.link_tags: list[dict] = []
        self.jsonld: list[tuple[int, str]] = []
        self._in_jsonld = False
        self._jsonld_buf: list[str] = []
        self._jsonld_line = 0
        self.headings: list[tuple[int, int, str]] = []
        self._cur_heading: list | None = None
        self.mains: list[dict] = []
        self.body_links: list[dict] = []
        self.in_body = False
        self.imgs: list[tuple[int, dict]] = []
        self.unnamed_controls: list[tuple[int, str]] = []
        self._ctl: dict | None = None
        self.icons_without_hidden: list[int] = []
        self.times: list[str] = []
        self.crumbs: list[str] = []
        self._in_crumb_nav = False
        self._crumb_li: list[str] | None = None

    # --- utilidades -------------------------------------------------
    def _attrs(self, attrs):
        return {k: (v if v is not None else "") for k, v in attrs}

    def _record_refs(self, tag: str, a: dict, line: int) -> None:
        if "id" in a:
            self.ids.add(a["id"])
        if "name" in a:
            self.names.add(a["name"])
        if "style" in a:
            self.styles.append((line, a["style"]))
        if tag == "a":
            href = a.get("href")
            if href is not None:
                h = href.strip()
                if h in ("", "#") or h.lower().startswith("javascript:"):
                    self.dead_links.append(line)
                elif h.startswith("#"):
                    self.hash_targets.append((line, h[1:]))
                else:
                    self.refs.append(("a", "href", line, h))
        if tag == "link":
            rel = set(a.get("rel", "").lower().split())
            href = a.get("href", "")
            if href:
                self.refs.append(("link", "href", line, href))
                if rel & LINK_REL_REQUESTS:
                    self.request_refs.append((f"<link rel=\"{a.get('rel', '')}\">", line, href))
        for attr in REQUEST_ATTRS.get(tag, []):
            if attr in a and a[attr]:
                val = a[attr]
                if attr == "srcset":
                    for part in val.split(","):
                        u = part.strip().split(" ")[0]
                        if u:
                            self.refs.append((tag, attr, line, u))
                            self.request_refs.append((f"<{tag} {attr}>", line, u))
                else:
                    self.refs.append((tag, attr, line, val))
                    self.request_refs.append((f"<{tag} {attr}>", line, val))
        if tag in ("button", "div", "section", "a", "span") and "data-bs-target" in a:
            t = a["data-bs-target"].strip()
            if t.startswith("#") and len(t) > 1:
                self.hash_targets.append((line, t[1:]))

    # --- eventos del parser -----------------------------------------
    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        a = self._attrs(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self._in_title = True
        if tag == "meta" and a.get("name", "").lower() == "description":
            self.description = a.get("content", "")
        if tag == "meta":
            self.metas.append(a)
        if tag == "link":
            self.link_tags.append(a)
        if tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self._in_jsonld = True
            self._jsonld_buf = []
            self._jsonld_line = line
        if tag == "body":
            self.in_body = True
        if re.fullmatch(r"h[1-6]", tag):
            self._cur_heading = [line, int(tag[1]), ""]
        if tag == "main":
            self.mains.append(a)
        if tag == "a" and self.in_body:
            self.body_links.append(a)
        if tag == "img":
            self.imgs.append((line, a))
            if self._ctl is not None and a.get("alt", "").strip():
                self._ctl["named"] = True
        if tag in ("a", "button"):
            named = bool(a.get("aria-label") or a.get("aria-labelledby") or a.get("title"))
            self._ctl = {"tag": tag, "line": line, "attrs": a, "text": "", "named": named}
        if tag == "i" and re.search(r"\bfa[a-z]?(-[a-z]+)?\b", a.get("class", "")) and a.get("aria-hidden") != "true":
            self.icons_without_hidden.append(line)
        if tag == "time" and "datetime" in a:
            self.times.append(a["datetime"])
        if tag == "nav" and a.get("aria-label") == "Migas de pan":
            self._in_crumb_nav = True
        if self._in_crumb_nav and tag == "li":
            self._crumb_li = []
        if tag == "style":
            self._in_style = True
            self._style_buf = []
            self._style_line = line
        if tag == "div":
            self.div_open += 1
        self._record_refs(tag, a, line)
        if tag not in VOID_TAGS and tag not in SVG_SELF:
            self.stack.append((tag, line))

    def handle_startendtag(self, tag, attrs):
        line = self.getpos()[0]
        a = self._attrs(attrs)
        if tag == "div":
            self.div_open += 1
            self.div_close += 1
        self._record_refs(tag, a, line)

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append((self._jsonld_line, "".join(self._jsonld_buf)))
        if re.fullmatch(r"h[1-6]", tag) and self._cur_heading is not None:
            self.headings.append((self._cur_heading[0], self._cur_heading[1], re.sub(r"\s+", " ", self._cur_heading[2]).strip()))
            self._cur_heading = None
        if tag in ("a", "button") and self._ctl is not None:
            c = self._ctl
            self._ctl = None
            is_link = c["tag"] == "a" and "href" in c["attrs"]
            if (is_link or c["tag"] == "button") and not c["named"] and not c["text"].strip():
                self.unnamed_controls.append((c["line"], c["tag"]))
        if tag == "nav":
            self._in_crumb_nav = False
        if tag == "li" and self._crumb_li is not None:
            self.crumbs.append(re.sub(r"\s+", " ", "".join(self._crumb_li)).strip())
            self._crumb_li = None
        if tag == "style":
            self._in_style = False
            self.styles.append((self._style_line, "".join(self._style_buf)))
        if tag == "div":
            self.div_close += 1
        if tag in VOID_TAGS or tag in SVG_SELF:
            return
        # Busca la etiqueta abierta correspondiente.
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                # Lo que quede abierto por encima debe ser de cierre opcional.
                for t, l in self.stack[i + 1:]:
                    if t not in OPTIONAL_END:
                        self.imbalance.append((l, f"<{t}> abierta en la línea {l} sin cerrar antes de </{tag}> (línea {line})"))
                del self.stack[i:]
                return
        if tag not in OPTIONAL_END:
            self.imbalance.append((line, f"</{tag}> sin etiqueta de apertura"))

    def handle_data(self, data):
        if self._in_jsonld:
            self._jsonld_buf.append(data)
        if self._cur_heading is not None:
            self._cur_heading[2] += data
        if self._ctl is not None:
            self._ctl["text"] += data
        if self._crumb_li is not None:
            self._crumb_li.append(data)
        if self._in_title:
            self.title += data
        if self._in_style:
            self._style_buf.append(data)

    def close(self):
        super().close()
        for t, l in self.stack:
            if t not in OPTIONAL_END and t not in ("html", "body", "head"):
                self.imbalance.append((l, f"<{t}> abierta en la línea {l} sin cerrar"))


def is_external(ref: str) -> str | None:
    """Devuelve el host si la referencia apunta fuera del sitio, o None si es local."""
    r = ref.strip()
    if r.startswith("//"):
        return urlparse("https:" + r).netloc.lower()
    p = urlparse(r)
    if p.scheme in ("http", "https"):
        return p.netloc.lower()
    return None


def is_skippable(ref: str) -> bool:
    r = ref.strip().lower()
    return (
        not r
        or r.startswith(("mailto:", "tel:", "data:", "javascript:", "#", "sms:", "whatsapp:"))
    )


def resolve_local(base_file: Path, ref: str) -> Path:
    path = unquote(urlparse(ref).path)
    if path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = (base_file.parent / path)
    if str(path).endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I)
CSS_IMPORT_RE = re.compile(r"@import\s+(?:url\(\s*)?(['\"])(.*?)\1", re.I)


def check_css_refs(text: str, base_file: Path, where: str, line: int | None = None) -> None:
    """Comprueba url() y @import de un bloque CSS."""
    refs = [m.group(2) for m in CSS_URL_RE.finditer(text)] + [m.group(2) for m in CSS_IMPORT_RE.finditer(text)]
    for ref in refs:
        ref = ref.strip()
        if is_skippable(ref):
            continue
        host = is_external(ref)
        if host is not None:
            if host not in ALLOWED_REQUEST_HOSTS:
                err(base_file, line, f"{where}: petición a host externo {host} ({ref})")
            continue
        if not resolve_local(base_file, ref).exists():
            err(base_file, line, f"{where}: recurso inexistente {ref}")


COMMENT_BLOCK = re.compile(r"/\*.*?\*/", re.S)
COMMENT_LINE_JS = re.compile(r"(?<![:\"'\\])//[^\n]*")
FORBIDDEN_WORDS = re.compile(r"brevon|gramentheme|neotix", re.I)


def strip_comments(text: str, js: bool) -> str:
    text = COMMENT_BLOCK.sub("", text)
    if js:
        text = COMMENT_LINE_JS.sub("", text)
    return text


def expected_url(name: str) -> str:
    return SITE_URL + "/" if name == "index.html" else f"{SITE_URL}/{name}"


def image_size(path: Path) -> tuple[int, int] | None:
    """Dimensiones de un PNG o JPEG (sin dependencias); None si no se puede leer."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return None


def local_from_site_url(url: str) -> Path | None:
    if not url.startswith(SITE_URL + "/"):
        return None
    rel = url[len(SITE_URL) + 1:] or "index.html"
    return ROOT / rel


def check_seo(path: Path, p: PageParser, title: str, desc: str) -> None:
    name = path.name
    meta = {}
    for m in p.metas:
        key = m.get("property") or m.get("name")
        if key:
            meta[key] = m.get("content", "")
    robots = meta.get("robots", "")
    if name in NOINDEX_PAGES:
        if "noindex" not in robots.lower():
            err(path, None, 'la página de error debe llevar <meta name="robots" content="noindex">')
        return
    if "noindex" in robots.lower():
        err(path, None, "una página indexable lleva noindex")
    if not 50 <= len(title) <= 60:
        err(path, None, f"el <title> debe medir 50-60 caracteres (mide {len(title)}): {title!r}")
    if not 120 <= len(desc) <= 160:
        err(path, None, f"la meta description debe medir 120-160 caracteres (mide {len(desc)})")
    canon = [l.get("href", "") for l in p.link_tags if l.get("rel") == "canonical"]
    expected = expected_url(name)
    if canon != [expected]:
        err(path, None, f"canonical incorrecto: {canon} (esperado [{expected!r}])")
    required = ["og:title", "og:description", "og:url", "og:type", "og:locale", "og:site_name", "og:image",
                "og:image:width", "og:image:height", "og:image:alt", "twitter:card", "twitter:title",
                "twitter:description", "twitter:image"]
    for key in required:
        if not meta.get(key):
            err(path, None, f"falta <meta> {key}")
    if meta.get("og:url") and meta["og:url"] != expected:
        err(path, None, f"og:url ({meta['og:url']}) distinto del canonical")
    if meta.get("og:locale") and meta["og:locale"] != "es_ES":
        err(path, None, "og:locale debe ser es_ES")
    if meta.get("og:title") and meta["og:title"] != title:
        err(path, None, "og:title distinto del <title>")
    if meta.get("og:description") and meta["og:description"] != desc:
        err(path, None, "og:description distinta de la meta description")
    if meta.get("twitter:card") and meta["twitter:card"] != "summary_large_image":
        err(path, None, "twitter:card debe ser summary_large_image")
    img = meta.get("og:image", "")
    if img:
        if meta.get("twitter:image") != img:
            err(path, None, "twitter:image distinta de og:image")
        local = local_from_site_url(img)
        if local is None or not local.exists():
            err(path, None, f"og:image no existe en el sitio: {img}")
        else:
            size = image_size(local)
            if size is not None and size != (1200, 630):
                err(path, None, f"og:image debe medir 1200x630 (mide {size[0]}x{size[1]}): {img}")
    if meta.get("og:image:width") not in (None, "1200") or meta.get("og:image:height") not in (None, "630"):
        err(path, None, "og:image:width/height deben ser 1200 y 630")


def jsonld_objects(path: Path, p: PageParser) -> list[dict]:
    out = []
    for line, text in p.jsonld:
        try:
            data = json.loads(text)
        except ValueError as exc:
            err(path, line, f"JSON-LD no válido: {exc}")
            continue
        out.extend(data if isinstance(data, list) else [data])
    return out


def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v)


def check_jsonld(path: Path, p: PageParser, raw: str) -> None:
    name = path.name
    if name in NOINDEX_PAGES:
        return
    objs = jsonld_objects(path, p)
    by_type: dict[str, list[dict]] = {}
    for o in objs:
        if o.get("@context") != "https://schema.org":
            err(path, None, "JSON-LD sin @context https://schema.org")
        by_type.setdefault(str(o.get("@type")), []).append(o)
        for sub in walk(o):
            for bad in ("aggregateRating", "review", "reviews", "ratingValue"):
                if bad in sub:
                    err(path, None, f"JSON-LD con {bad}: no hay valoraciones reales que respalden esos datos")
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", strip_code_blocks(raw)))

    expected: set[str] = set()
    if name == "index.html":
        expected |= {"Organization", "SoftwareApplication"}
    if name == "pricing.html":
        expected.add("SoftwareApplication")
    if name == "faq.html":
        expected.add("FAQPage")
    if name in ARTICLES:
        expected.add("Article")
    if p.crumbs:
        expected.add("BreadcrumbList")
    for t in expected:
        if t not in by_type:
            err(path, None, f"falta el JSON-LD {t}")
    for t in by_type:
        if t not in expected and t not in ("Organization", "SoftwareApplication"):
            err(path, None, f"JSON-LD {t} que la página no necesita")

    for o in by_type.get("SoftwareApplication", []):
        if o.get("applicationCategory") != "BusinessApplication":
            err(path, None, "SoftwareApplication debe ser BusinessApplication")
        offers = o.get("offers", [])
        prices = sorted(float(x.get("price", 0)) for x in offers)
        if prices != [6.45, 11.95, 23.95]:
            err(path, None, f"las ofertas JSON-LD no coinciden con los planes (6,45 / 11,95 / 23,95): {prices}")
        if any(x.get("priceCurrency") != "EUR" for x in offers):
            err(path, None, "las ofertas JSON-LD deben ir en EUR")
    if name == "pricing.html":
        for token in ("6,45", "11,95", "23,95", "4,95", "8,95", "17,95"):
            if token not in raw:
                err(path, None, f"el precio {token} no aparece en la página, pero sí en el JSON-LD")
    for o in objs:
        for sub in walk(o):
            logo = sub.get("logo")
            if isinstance(logo, dict):
                logo = logo.get("url")
            if isinstance(logo, str):
                local = local_from_site_url(logo)
                if local is None or not local.exists():
                    err(path, None, f"logo del JSON-LD inexistente: {logo}")
    for o in by_type.get("FAQPage", []):
        questions = [q.get("name", "") for q in o.get("mainEntity", [])]
        visible = [t for (_l, lvl, t) in p.headings if lvl >= 2 and t.endswith("?")]
        if not questions or any(q not in visible for q in questions):
            err(path, None, "las preguntas del JSON-LD FAQPage no coinciden con las visibles en la página")
    for o in by_type.get("Article", []):
        times = p.times
        if len(times) < 2 or o.get("datePublished") != times[0] or o.get("dateModified") != times[1]:
            err(path, None, f"fechas del JSON-LD ({o.get('datePublished')}, {o.get('dateModified')}) distintas de las visibles {times[:2]}")
        h1 = next((t for (_l, lvl, t) in p.headings if lvl == 1), "")
        if not (o.get("headline") and (o["headline"] == h1 or len(o["headline"]) <= 110)):
            err(path, None, "headline del Article demasiado largo o ausente")
        imgs = o.get("image") or []
        for u in imgs:
            local = local_from_site_url(u)
            if local is None or not local.exists():
                err(path, None, f"imagen del Article inexistente: {u}")
        if (o.get("mainEntityOfPage") or {}).get("@id") != expected_url(name):
            err(path, None, "mainEntityOfPage del Article distinto del canonical")
    for o in by_type.get("BreadcrumbList", []):
        names = [e.get("name") for e in o.get("itemListElement", [])]
        if names != p.crumbs:
            err(path, None, f"BreadcrumbList {names} distinto de las migas visibles {p.crumbs}")
        for e in o.get("itemListElement", []):
            local = local_from_site_url(e.get("item", ""))
            if local is None or not local.exists():
                err(path, None, f"BreadcrumbList apunta a una URL inexistente: {e.get('item')}")


GENERIC_ALT = {"img", "image", "imagen", "logo-img", "logo", "icon", "icono", "photo", "foto", "picture", "banner"}


def check_a11y(path: Path, p: PageParser) -> None:
    if path.name in NOINDEX_PAGES and not p.mains:
        pass  # la 404 también debe cumplirlo: se sigue comprobando abajo
    first = p.body_links[0] if p.body_links else {}
    if first.get("href") != "#main":
        err(path, None, 'el primer enlace del <body> debe ser el skip link <a href="#main">Saltar al contenido</a>')
    if len(p.mains) != 1 or p.mains[0].get("id") != "main":
        err(path, None, f'debe haber un único <main id="main"> (hay {len(p.mains)})')
    prev = 0
    for line, level, text in p.headings:
        if not text:
            err(path, line, f"encabezado h{level} vacío")
        if prev == 0 and level != 1:
            err(path, line, f"el primer encabezado de la página es h{level}, debería ser h1")
        elif prev and level > prev + 1:
            err(path, line, f"salto de jerarquía de h{prev} a h{level}: {text[:50]!r}")
        prev = level
    for line, a in p.imgs:
        alt = a.get("alt")
        if alt is None:
            err(path, line, f"<img> sin atributo alt: {a.get('src', '')}")
        elif alt.strip().lower() in GENERIC_ALT or re.search(r"\.(png|jpe?g|webp|svg)$", alt.strip(), re.I):
            err(path, line, f"<img> con alt genérico {alt!r} (usa una descripción o alt=\"\" si es decorativa)")
    for line, tag in p.unnamed_controls[:5]:
        err(path, line, f"<{tag}> sin nombre accesible (añade texto o aria-label)")
    for line in p.icons_without_hidden[:5]:
        err(path, line, 'icono decorativo <i class="fa…"> sin aria-hidden="true"')
    if len(p.icons_without_hidden) > 5:
        err(path, None, f"... y {len(p.icons_without_hidden) - 5} iconos sin aria-hidden más")


def check_page(path: Path, titles: dict, descriptions: dict) -> None:
    raw = path.read_text(encoding="utf-8")
    p = PageParser()
    try:
        p.feed(raw)
        p.close()
    except Exception as exc:  # pragma: no cover - HTML muy roto
        err(path, None, f"no se pudo analizar el HTML: {exc}")
        return

    # Estructura
    if p.div_open != p.div_close:
        err(path, None, f"<div> desbalanceados: {p.div_open} abiertos y {p.div_close} cerrados")
    for line, msg in p.imbalance[:5]:
        err(path, line, f"etiquetas mal anidadas: {msg}")
    if len(p.imbalance) > 5:
        err(path, None, f"... y {len(p.imbalance) - 5} desajustes de etiquetas más")

    if (p.lang or "").lower() != "es":
        err(path, None, f'<html lang="es"> ausente (lang={p.lang!r})')
    title = re.sub(r"\s+", " ", p.title).strip()
    if not title:
        err(path, None, "falta <title>")
    else:
        titles.setdefault(title, []).append(path.name)
    desc = (p.description or "").strip()
    if not desc:
        err(path, None, "falta <meta name=\"description\">")
    else:
        descriptions.setdefault(desc, []).append(path.name)
    if p.h1_count != 1:
        err(path, None, f"debe haber exactamente un <h1> (hay {p.h1_count})")
    check_seo(path, p, title, desc)
    check_jsonld(path, p, raw)
    check_a11y(path, p)

    # Enlaces muertos y anclas
    for line in p.dead_links:
        err(path, line, 'enlace muerto: href="#" / vacío / javascript:')
    for line, target in p.hash_targets:
        if target not in p.ids and target not in p.names:
            err(path, line, f"ancla interna inexistente: #{target}")

    # Referencias locales y externas
    for tag, attr, line, ref in p.refs:
        if is_skippable(ref):
            continue
        host = is_external(ref)
        if host is not None:
            continue  # los <a> externos se admiten; los recursos se validan abajo
        if not resolve_local(path, ref).exists():
            err(path, line, f"<{tag} {attr}> apunta a un fichero inexistente: {ref}")
    for desc_, line, ref in p.request_refs:
        host = is_external(ref)
        if host is not None and host not in ALLOWED_REQUEST_HOSTS:
            err(path, line, f"{desc_} hace una petición a un host externo: {host}")

    # CSS en línea y bloques <style>
    for line, css in p.styles:
        check_css_refs(css, path, "CSS en línea", line)

    # Restos de plantilla
    for m in FORBIDDEN_WORDS.finditer(raw):
        line = raw.count("\n", 0, m.start()) + 1
        err(path, line, f"resto de plantilla: {m.group(0)!r}")
    for m in re.finditer(r"lorem\s+ipsum", raw, re.I):
        line = raw.count("\n", 0, m.start()) + 1
        err(path, line, "texto de relleno 'lorem ipsum'")

    # Manejadores en línea y naranjas sueltos en el HTML
    for m in INLINE_HANDLER.finditer(raw):
        err(path, raw.count("\n", 0, m.start()) + 1, "manejador de evento en línea (usa addEventListener en un JS propio)")
    for c in STRAY_COLORS:
        for m in re.finditer(re.escape(c), raw, re.I):
            err(path, raw.count("\n", 0, m.start()) + 1, f"naranja suelto {c}: usa los tokens de main.css")
    for line, css in p.styles:
        for m in OUTLINE_NONE.finditer(css):
            err(path, line, "outline: none !important en un <style> (el foco de teclado debe verse)")

    # Veracidad del contenido (se ignoran los bloques <style> y <script> que no son JSON-LD)
    check_content(path, strip_code_blocks(raw))


def strip_code_blocks(raw: str) -> str:
    """Sustituye por espacios CSS y JS (conservando saltos de línea) para que las reglas de contenido
    solo vean el texto y el JSON-LD."""
    def blank(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))
    raw = re.sub(r"<style\b.*?</style>", blank, raw, flags=re.S | re.I)
    raw = re.sub(r"<script\b(?![^>]*application/ld\+json).*?</script>", blank, raw, flags=re.S | re.I)
    raw = re.sub(r'\sstyle="[^"]*"', blank, raw)
    return raw


def check_content(path: Path, raw: str) -> None:
    for pattern, reason in CONTENT_RULES:
        seen_lines: set[int] = set()
        for m in re.finditer(pattern, raw, re.I):
            line = raw.count("\n", 0, m.start()) + 1
            if line in seen_lines:
                continue
            seen_lines.add(line)
            snippet = re.sub(r"\s+", " ", raw[max(0, m.start() - 25): m.end() + 25]).strip()
            err(path, line, f"contenido no permitido ({reason}): …{snippet}…")


def check_header_include() -> None:
    """El menú se inyecta desde JS: se validan sus enlaces y recursos igual que los del HTML."""
    f = ROOT / "assets/js/header-include.js"
    if not f.exists():
        return
    text = f.read_text(encoding="utf-8")
    # Enlaces de los datos (SERVICES) y atributos escritos directamente en la plantilla
    for m in re.finditer(r"href:\s*'([^']+)'", text):
        line = text.count("\n", 0, m.start()) + 1
        if not resolve_local(ROOT / "index.html", m.group(1)).exists():
            err(f, line, f"href apunta a un fichero inexistente: {m.group(1)}")
    for m in re.finditer(r'(href|src)="([^"]+)"', text):
        ref = m.group(2)
        line = text.count("\n", 0, m.start()) + 1
        if re.search(r"['+$]", ref):
            continue  # fragmentos construidos en JS (se validan con los datos)
        if is_skippable(ref):
            if ref == "#":
                err(f, line, 'enlace muerto: href="#"')
            continue
        if is_external(ref) is not None:
            continue
        if not resolve_local(ROOT / "index.html", ref).exists():
            err(f, line, f"{m.group(1)} apunta a un fichero inexistente: {ref}")
    check_content(f, text)


def check_assets() -> None:
    """CSS y JS: url() y @import, peticiones externas en el JS propio y restos de plantilla."""
    for css in sorted((ROOT / "assets/css").rglob("*.css")):
        text = css.read_text(encoding="utf-8", errors="replace")
        check_css_refs(text, css, "CSS")
        if FORBIDDEN_WORDS.search(strip_comments(text, js=False)):
            err(css, None, "resto de plantilla fuera de un comentario de licencia")
    for js in sorted((ROOT / "assets/js").glob("*.js")):
        text = js.read_text(encoding="utf-8", errors="replace")
        if FORBIDDEN_WORDS.search(strip_comments(text, js=True)):
            err(js, None, "resto de plantilla fuera de un comentario de licencia")
    for rel in FIRST_PARTY_ASSETS:
        f = ROOT / rel
        if not f.exists():
            continue
        text = strip_comments(f.read_text(encoding="utf-8", errors="replace"), js=True)
        for m in re.finditer(r"https?://[^\s\"'`)<>]+", text):
            host = urlparse(m.group(0)).netloc.lower()
            if host in ALLOWED_REQUEST_HOSTS or host == "www.w3.org":
                continue
            line = text.count("\n", 0, m.start()) + 1
            err(f, line, f"el JS propio menciona un host externo: {host}")


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def luminance(h: str) -> float:
    def f(c: int) -> float:
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = hex_to_rgb(h)
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


OUTLINE_NONE = re.compile(r"outline\s*:\s*(?:none|0)\b[^;{}]*!important", re.I)
INLINE_HANDLER = re.compile(r"\son(?:click|change|load|submit|input|focus|blur|mouse\w+|key\w+|touch\w+)\s*=", re.I)


def check_styles_and_scripts() -> None:
    """Foco, movimiento reducido, naranjas sueltos, contraste de los tokens y JS propio."""
    css_dir = ROOT / "assets/css"
    own_css = [f for f in sorted(css_dir.rglob("*.css")) if f.name not in VENDOR_CSS]
    for css in own_css:
        text = strip_comments(css.read_text(encoding="utf-8", errors="replace"), js=False)
        for m in OUTLINE_NONE.finditer(text):
            err(css, text.count("\n", 0, m.start()) + 1, "outline: none !important (el foco de teclado debe verse)")
        for c in STRAY_COLORS:
            if c in text.lower():
                err(css, None, f"naranja suelto {c}: usa los tokens de main.css (--accent, --theme-strong, --theme-text)")
        if re.search(r"rgba\(\s*236\s*,\s*130\s*,\s*40", text):
            err(css, None, "naranja suelto rgba(236,130,40,…): usa rgba(249,77,0,…) o los tokens")

    main_css = css_dir / "main.css"
    if main_css.exists():
        text = main_css.read_text(encoding="utf-8", errors="replace")
        if ":focus-visible" not in text:
            err(main_css, None, "falta la regla global :focus-visible")
        if "prefers-reduced-motion" not in text:
            err(main_css, None, "falta el bloque @media (prefers-reduced-motion: reduce)")
        root = re.search(r":root\s*\{(.*?)\}", text, re.S)
        tokens = dict(re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\s*;", root.group(1))) if root else {}
        pairs = [("theme-strong", "white", 4.5, "fondo de botones con texto blanco"),
                 ("theme-text", "bg", 4.5, "texto naranja sobre --bg"),
                 ("theme-text", "white", 4.5, "texto naranja sobre blanco"),
                 ("text-dim", "bg", 4.5, "texto atenuado de titulares sobre --bg"),
                 ("success-strong", "white", 4.5, "fondo verde con texto blanco"),
                 ("accent-dark", "white", 4.5, "final de degradados con texto blanco"),
                 ("text", "bg", 4.5, "texto de cuerpo sobre --bg"),
                 ("theme", "header", 4.5, "naranja de marca sobre fondos oscuros")]
        for a, b, minimum, why in pairs:
            ca = "#FFFFFF" if a == "white" else tokens.get(a)
            cb = "#FFFFFF" if b == "white" else tokens.get(b)
            if not ca or not cb:
                err(main_css, None, f"falta el token --{a if not ca else b} en :root")
                continue
            ratio = contrast(ca, cb)
            if ratio < minimum:
                err(main_css, None, f"contraste insuficiente de --{a} sobre --{b} ({ratio:.2f}:1 < {minimum}): {why}")

    for rel in FIRST_PARTY_ASSETS:
        f = ROOT / rel
        if not f.exists():
            continue
        text = strip_comments(f.read_text(encoding="utf-8", errors="replace"), js=True)
        if "ScrollSmoother" in text:
            err(f, None, "usa ScrollSmoother (el scroll es nativo)")
        for m in re.finditer(r"autoplay\s*:\s*\{[^}]*?delay\s*:\s*(\d+)", text):
            if int(m.group(1)) < 6000:
                err(f, text.count("\n", 0, m.start()) + 1, f"autoplay de {m.group(1)} ms (mínimo 6000 o sin autoplay)")
    for rel in ("assets/js/main.js", "assets/js/home.js"):
        f = ROOT / rel
        if f.exists() and "prefers-reduced-motion" not in f.read_text(encoding="utf-8", errors="replace"):
            err(f, None, "no tiene en cuenta prefers-reduced-motion")


ICON_STYLE_WORDS = {"solid", "regular", "light", "thin", "brands", "duotone", "fw", "lg", "xs", "sm", "xl", "2xl", "2xs", "spin", "pulse"}


def check_icons(pages: list[Path]) -> None:
    """Todo icono fa-* usado debe estar en el subconjunto de assets/css/icons.css."""
    icons_css = ROOT / "assets/css/icons.css"
    if not icons_css.exists():
        err("assets/css/icons.css", None, "falta la hoja de iconos")
        return
    available = set(re.findall(r"\.fa-([a-z0-9-]+)::before", icons_css.read_text(encoding="utf-8")))
    sources = list(pages) + [ROOT / rel for rel in FIRST_PARTY_ASSETS if (ROOT / rel).exists()]
    for f in sources:
        text = f.read_text(encoding="utf-8")
        for m in re.finditer(r"(?<![\w/.-])fa-([a-z0-9-]+)", text):
            name = m.group(1)
            if name in ICON_STYLE_WORDS or name in available:
                continue
            err(f, text.count("\n", 0, m.start()) + 1,
                f"el icono fa-{name} no está en assets/css/icons.css (hay que regenerar el subconjunto de la fuente)")


def check_sitemap(pages: list[Path]) -> None:
    """sitemap.xml lista exactamente las páginas indexables y robots.txt lo anuncia."""
    import xml.etree.ElementTree as ET

    sm = ROOT / "sitemap.xml"
    if not sm.exists():
        err("sitemap.xml", None, "falta sitemap.xml")
    else:
        try:
            tree = ET.parse(sm)
        except ET.ParseError as exc:
            err(sm, None, f"XML no válido: {exc}")
        else:
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            locs = [e.text.strip() for e in tree.getroot().findall("s:url/s:loc", ns) if e.text]
            want = sorted(expected_url(p.name) for p in pages if p.name not in NOINDEX_PAGES)
            if sorted(locs) != want:
                faltan = sorted(set(want) - set(locs))
                sobran = sorted(set(locs) - set(want))
                err(sm, None, f"el sitemap no coincide con las páginas indexables (faltan {faltan}, sobran {sobran})")
            if len(locs) != len(set(locs)):
                err(sm, None, "el sitemap repite URLs")
    rb = ROOT / "robots.txt"
    if not rb.exists():
        err("robots.txt", None, "falta robots.txt")
    elif f"Sitemap: {SITE_URL}/sitemap.xml" not in rb.read_text(encoding="utf-8"):
        err(rb, None, f"robots.txt debe incluir 'Sitemap: {SITE_URL}/sitemap.xml'")


def main() -> int:
    ap = argparse.ArgumentParser(description="Comprobaciones estáticas del sitio de Facturales")
    ap.add_argument("files", nargs="*", help="páginas a revisar (por defecto, todas las .html)")
    ap.add_argument("-v", "--verbose", action="store_true", help="lista también los ficheros correctos")
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    args = ap.parse_args()

    if args.files:
        pages = [ROOT / f for f in args.files]
    else:
        pages = sorted(
            p for p in ROOT.rglob("*.html")
            if not (set(p.relative_to(ROOT).parts[:-1]) & SKIP_DIRS)
        )
    titles: dict[str, list[str]] = {}
    descriptions: dict[str, list[str]] = {}
    for page in pages:
        before = len(errors)
        check_page(page, titles, descriptions)
        if args.verbose and len(errors) == before:
            print(f"ok     {page.relative_to(ROOT)}")
    for title, names in titles.items():
        if len(names) > 1:
            err("(varias páginas)", None, f"<title> repetido en {', '.join(names)}: {title!r}")
    for desc, names in descriptions.items():
        if len(names) > 1:
            err("(varias páginas)", None, f"meta description repetida en {', '.join(names)}")
    if not args.files:
        check_header_include()
        check_assets()
        check_styles_and_scripts()
        check_icons(pages)
        check_sitemap(pages)

    if args.json:
        print(json.dumps({"pages": len(pages), "errors": errors}, ensure_ascii=False, indent=2))
    else:
        for e in errors:
            print(f"ERROR  {e}")
        print(f"\n{len(pages)} páginas revisadas, {len(errors)} errores.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
