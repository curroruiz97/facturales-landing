#!/usr/bin/env python3
"""Congela la landing anterior en v1/ para el conmutador v1/v2 (ver «Conmutador v1/v2» en CLAUDE.md).

Uso:  python3 scripts/freeze-v1.py [ref-de-git]      (por defecto, origin/add-template: la base de la PR)

Copia a v1/ las páginas de esa versión y los recursos que usan, y marca cada página como copia:
  - <meta robots noindex>, para que no se indexe;
  - <meta facturales-version=v1>;
  - un script que, en facturales.es, redirige a la misma página del sitio actual (la copia no se sirve en producción);
  - el conmutador, para volver a la versión actual.
No se copian los scripts .py ni el package-lock.json de esa versión, partials/, assets/scss, las páginas con espacios en el nombre
(copias sueltas), las tipografías .ttf (los navegadores usan las .woff2), los .map ni la Font Awesome «duotone», que ninguna página usa.
Solo biblioteca estándar. Repetible: con el mismo commit sale el mismo resultado.
"""
import io
import re
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "v1"

HEAD_SNIPPET = (
    "\n<!-- Copia congelada de la landing anterior (conmutador v1/v2, ver CLAUDE.md): no se indexa y no se sirve en facturales.es. -->"
    '\n<meta name="robots" content="noindex, nofollow">'
    '\n<meta name="facturales-version" content="v1">'
    '\n<script>if(/^(www\\.)?facturales\\.es$/i.test(location.hostname))'
    'location.replace(location.pathname.replace(/\\/v1\\/(?=[^\\/]*$)/,"/")+location.search+location.hash)</script>'
)
BODY_SNIPPET = '<script src="../assets/js/version-switcher.js" defer></script>\n'


def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, capture_output=True).stdout


def wanted(name: str) -> bool:
    parts = name.split("/")
    if len(parts) == 1:
        return name.endswith(".html") and " " not in name
    if parts[0] != "assets" or parts[1] == "scss":
        return False
    return not (name.endswith((".ttf", ".map")) or "fa-duotone" in name)


def mark_page(name: str, html: str) -> str:
    head, n_head = re.subn(r"(<meta\s+charset=[^>]*>)", lambda m: m.group(1) + HEAD_SNIPPET, html, count=1, flags=re.I)
    if n_head != 1:
        head, n_head = re.subn(r"(<head[^>]*>)", lambda m: m.group(1) + HEAD_SNIPPET, html, count=1, flags=re.I)
    body, n_body = re.subn(r"</body>", lambda m: BODY_SNIPPET + m.group(0), head, count=1, flags=re.I)
    if n_head != 1 or n_body != 1:
        raise SystemExit(f"{name}: no se encontró <head> o </body> donde insertar la marca de copia")
    return body


def main() -> int:
    ref = sys.argv[1] if len(sys.argv) > 1 else "origin/add-template"
    sha = git("rev-parse", "--verify", f"{ref}^{{commit}}").decode().strip()
    if OUT.exists():
        shutil.rmtree(OUT)

    archive = tarfile.open(fileobj=io.BytesIO(git("archive", sha)))
    pages = files = 0
    for member in archive.getmembers():
        if not member.isfile() or not wanted(member.name):
            continue
        data = archive.extractfile(member).read()
        target = OUT / member.name
        target.parent.mkdir(parents=True, exist_ok=True)
        if member.name.endswith(".html"):
            data = mark_page(member.name, data.decode("utf-8")).encode("utf-8")
            pages += 1
        target.write_bytes(data)
        files += 1

    meta = git("show", "-s", "--format=%cI%n%s", sha).decode().splitlines()
    (OUT / "SOURCE.txt").write_text(
        "Congelado por scripts/freeze-v1.py: no se edita a mano.\n"
        f"ref:     {ref}\ncommit:  {sha}\nfecha:   {meta[0]}\nasunto:  {meta[1]}\n",
        encoding="utf-8",
    )
    print(f"v1/ congelado desde {sha[:7]}: {pages} páginas y {files - pages} recursos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
