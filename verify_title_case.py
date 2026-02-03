# -*- coding: utf-8 -*-
from pathlib import Path
import re

# Patrones que NO deben aparecer (Title Case incorrecto)
bad_patterns = [
    r' Y (?=[A-ZÁÉÍÓÚÑ])',  # " Y " seguido de mayúscula
    r' A (?=[A-ZÁÉÍÓÚÑ])',  # " A " seguido de mayúscula  
    r' De (?=[A-ZÁÉÍÓÚÑ])', # " De " seguido de mayúscula
    r' En (?=[A-ZÁÉÍÓÚÑ])', # " En " seguido de mayúscula
    r' Con (?=[A-ZÁÉÍÓÚÑ])',# " Con " seguido de mayúscula
    r' Tu (?=[A-ZÁÉÍÓÚÑ])', # " Tu " seguido de mayúscula
]

project_dir = Path('.')
html_files = list(project_dir.glob('*.html'))

print("Verificando Title Case incorrecto...\n")

issues_found = 0
files_with_issues = 0

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        file_issues = []
        
        for pattern in bad_patterns:
            matches = re.findall(pattern, content)
            if matches:
                file_issues.extend(matches)
        
        if file_issues:
            print(f"[!] {html_file.name}: {len(file_issues)} casos encontrados")
            files_with_issues += 1
            issues_found += len(file_issues)
    
    except Exception as e:
        print(f"[ERROR] {html_file.name}: {e}")

print(f"\n{'='*50}")
if issues_found == 0:
    print("✓ NO SE ENCONTRARON CASOS DE TITLE CASE INCORRECTO")
    print("✓ TODOS LOS ARCHIVOS ESTÁN CORRECTOS")
else:
    print(f"[!] Se encontraron {issues_found} casos en {files_with_issues} archivos")
print(f"{'='*50}")
