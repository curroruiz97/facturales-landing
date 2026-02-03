# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path

# Directorio del proyecto
project_dir = Path('.')

# Patrones a corregir
corrections = [
    # Breadcrumbs - cambiar "Home" por "Inicio"
    (r'<i class="fa-solid fa-house"></i> Home', r'<i class="fa-solid fa-house"></i> Inicio'),
    (r'>\s*Home\s*</a>', r'> Inicio</a>'),
    
    # Comentarios en inglés que quedan en el código
    (r'By Admin', r'Por Facturales'),
    (r'Read more', r'Leer más'),
    
    # Sidebar y otras secciones comunes
    (r'>Recent Post<', r'>Artículos recientes<'),
    (r'>Category<', r'>Categorías<'),
    (r'>Popular Tags<', r'>Etiquetas<'),
]

# Archivos HTML a procesar
html_files = list(project_dir.glob('*.html'))

print(f"Encontrados {len(html_files)} archivos HTML")
print("Procesando...\n")

files_modified = 0

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplicar todas las correcciones
        for pattern, replacement in corrections:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        # Solo escribir si hubo cambios
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {html_file.name}")
            files_modified += 1
        
    except Exception as e:
        print(f"[ERROR] {html_file.name}: {e}")

print(f"\n{files_modified} archivos modificados")
