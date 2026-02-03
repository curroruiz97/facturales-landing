# -*- coding: utf-8 -*-
import re

# Páginas de artículos a procesar
article_pages = [
    'verifactu-2027-guia-autonomos-pymes.html',
    'factura-electronica-vs-verifactu.html',
    'contabilidad-negocio-7-pasos.html'
]

print("Eliminando secciones de comentarios...\n")

for page in article_pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Eliminar la sección de comentarios existentes
        # Patrón: desde <div class="comments-area"> hasta su </div> de cierre
        pattern_comments = r'<div class="comments-area">.*?</div>\s*</div>\s*</div>\s*'
        content = re.sub(pattern_comments, '', content, flags=re.DOTALL)
        
        # Eliminar el formulario de comentarios
        # Patrón: desde <div class="comment-form-wrap"> hasta su </div> de cierre
        pattern_form = r'<div class="comment-form-wrap">.*?</form>\s*</div>\s*'
        content = re.sub(pattern_form, '', content, flags=re.DOTALL)
        
        if content != original_content:
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {page}")
        else:
            print(f"[INFO] {page} - No se encontraron comentarios")
        
    except Exception as e:
        print(f"[ERROR] {page}: {e}")

print("\nProceso completado!")
