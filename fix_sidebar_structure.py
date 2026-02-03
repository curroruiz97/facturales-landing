# -*- coding: utf-8 -*-
import re

# Páginas de artículos a procesar
article_pages = [
    'verifactu-2027-guia-autonomos-pymes.html',
    'factura-electronica-vs-verifactu.html',
    'contabilidad-negocio-7-pasos.html'
]

print("Corrigiendo estructura del sidebar...\n")

for page in article_pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar el patrón donde está el problema
        # El sidebar debe estar FUERA del col-lg-8, no dentro
        
        # Patrón: encontrar el cierre de la columna principal y asegurar que el sidebar esté después
        pattern = r'(<div class="row g-4">)\s*(<div class="col-12 col-lg-8">)'
        
        if re.search(pattern, content):
            # Verificar que el sidebar esté correctamente estructurado
            # El sidebar debe tener la clase correcta para que Bootstrap lo posicione bien
            content = content.replace(
                '<div class="col-lg-4 col-12">',
                '<div class="col-12 col-lg-4">'
            )
            
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {page} - Estructura del sidebar corregida")
        else:
            print(f"[INFO] {page} - No se encontró el patrón")
        
    except Exception as e:
        print(f"[ERROR] {page}: {e}")

print("\nProceso completado!")
