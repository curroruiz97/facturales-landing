# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path

# Directorio del proyecto
project_dir = Path('.')

# Correcciones específicas para nombres de funcionalidades
corrections = [
    ('Tu Negocio Bajo Control', 'Tu negocio bajo control'),
    ('Gestiona Tu Stock', 'Gestiona tu stock'),
    ('Gestiona Clientes', 'Gestiona clientes'),
    ('Crea Y Envia Facturas', 'Crea y envía facturas'),
    ('Crea Y Envia Presupuestos', 'Crea y envía presupuestos'),
    ('Crea Envia Facturas', 'Crea y envía facturas'),
    ('Crea Envia Presupuestos', 'Crea y envía presupuestos'),
    ('Escanea Gastos', 'Escanea gastos'),
    ('Factura Personalizada', 'Factura personalizada'),
    ('Conectado A Gestor', 'Conectado a gestor'),
]

# Archivos HTML a procesar
html_files = list(project_dir.glob('*.html'))

print(f"Procesando {len(html_files)} archivos HTML\n")

files_modified = 0

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplicar todas las correcciones
        for wrong, correct in corrections:
            content = content.replace(wrong, correct)
        
        # Solo escribir si hubo cambios
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {html_file.name}")
            files_modified += 1
        
    except Exception as e:
        print(f"[ERROR] {html_file.name}: {e}")

print(f"\n{files_modified} archivos modificados correctamente")
