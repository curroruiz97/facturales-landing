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
    CONTENT_RULES) ni los CTAs a rutas antiguas de la app.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent

# Hosts a los que el sitio puede hacer peticiones (recursos). Los <a> externos se admiten siempre.
ALLOWED_REQUEST_HOSTS = {"app.facturales.es"}

# Directorios que no se revisan.
SKIP_DIRS = {".git", ".claude", ".github", "node_modules", "assets", "scripts", "__pycache__"}

# Ficheros JS/CSS propios (no librerías de terceros) cuyo contenido se revisa en busca de
# peticiones externas y restos de plantilla. Las librerías de terceros solo se revisan en
# busca de "Brevon/Gramentheme/Neotix" fuera de comentarios.
FIRST_PARTY_ASSETS = ["assets/js/header-include.js", "assets/js/main.js", "assets/js/orbit-cta.js"]

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
    (r"(?<!facturas y )presupuestos\s+ilimitados",
     "afirma 'presupuestos ilimitados' (comparten el tope mensual del plan; solo Pro e Ilimitado no tienen tope)"),
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

    # Veracidad del contenido
    check_content(path, raw)


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
    for m in re.finditer(r'(href|src)="([^"]+)"', text):
        ref = m.group(2)
        line = text.count("\n", 0, m.start()) + 1
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
    for css in sorted((ROOT / "assets/css").glob("*.css")):
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

    if args.json:
        print(json.dumps({"pages": len(pages), "errors": errors}, ensure_ascii=False, indent=2))
    else:
        for e in errors:
            print(f"ERROR  {e}")
        print(f"\n{len(pages)} páginas revisadas, {len(errors)} errores.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
