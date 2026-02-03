# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path

# Directorio del proyecto
project_dir = Path('.')

# Lista completa de correcciones de Title Case
corrections = {
    # Conectores y artículos que NO deben ir en mayúscula
    ' Y ': ' y ',
    ' A ': ' a ',
    ' De ': ' de ',
    ' Del ': ' del ',
    ' En ': ' en ',
    ' Con ': ' con ',
    ' Para ': ' para ',
    ' Por ': ' por ',
    ' Sin ': ' sin ',
    ' Tu ': ' tu ',
    ' Tus ': ' tus ',
    ' El ': ' el ',
    ' La ': ' la ',
    ' Los ': ' los ',
    ' Las ': ' las ',
    ' Un ': ' un ',
    ' Una ': ' una ',
    
    # Títulos específicos encontrados en las imágenes
    'Crea Facturas Y Tickets': 'Crea facturas y tickets',
    'Fácil Y Sin Errores': 'fácil y sin errores',
    'Personaliza Facturas Y Presupuestos': 'Personaliza facturas y presupuestos',
    'Personaliza Facturas Y': 'Personaliza facturas y',
    'Con Tu Marca': 'con tu marca',
    'Controla Tus Ingresos Y Gastos': 'Controla tus ingresos y gastos',
    'En Tiempo Real': 'en tiempo real',
    'Tu Negocio Bajo Control': 'Tu negocio bajo control',
    'Crea Y Envía Facturas': 'Crea y envía facturas',
    'Crea Y Envía Presupuestos': 'Crea y envía presupuestos',
    'Gestiona Tu Stock': 'Gestiona tu stock',
    'Conectado A Gestor': 'Conectado a gestor',
    'Beneficios De Tener': 'Beneficios de tener',
    'Visión Global De Tu Negocio': 'Visión global de tu negocio',
    'Toma Decisiones Informadas': 'Toma decisiones informadas',
    'Optimiza Recursos': 'Optimiza recursos',
    
    # Más casos comunes
    'Los Servicios Más Reconocidos': 'Los servicios más reconocidos',
    'Gestiona Tus': 'Gestiona tus',
    'Controla Tus': 'Controla tus',
    'Mejora Tu': 'Mejora tu',
    'Optimiza Tu': 'Optimiza tu',
}

# Archivos HTML a procesar
html_files = list(project_dir.glob('*.html'))

print(f"Procesando {len(html_files)} archivos HTML\n")

files_modified = 0
total_corrections = 0

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_corrections = 0
        
        # Aplicar todas las correcciones
        for wrong, correct in corrections.items():
            count = content.count(wrong)
            if count > 0:
                content = content.replace(wrong, correct)
                file_corrections += count
        
        # Solo escribir si hubo cambios
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {html_file.name} - {file_corrections} correcciones")
            files_modified += 1
            total_corrections += file_corrections
        
    except Exception as e:
        print(f"[ERROR] {html_file.name}: {e}")

print(f"\n{'='*50}")
print(f"Resumen:")
print(f"  Archivos modificados: {files_modified}")
print(f"  Total de correcciones: {total_corrections}")
print(f"{'='*50}")
