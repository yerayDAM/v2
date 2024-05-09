from PIL import Image
import os

def resize_image(image_path, new_width=600, new_height=300, output_folder='resize-dnsdumstep'):
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Abrir la imagen
        img = Image.open(image_path)
        # Redimensionar la imagen
        img_resized = img.resize((new_width, new_height), Image.BILINEAR)
        # Extraer el nombre del archivo y la extensión
        filename, ext = os.path.splitext(os.path.basename(image_path))
        # Guardar la imagen redimensionada en la carpeta de salida
        output_path = os.path.join(output_folder, f"{filename}_resized{ext}")
        img_resized.save(output_path)
        print(f"Imagen redimensionada guardada en: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error al redimensionar la imagen: {e}")


# Ejemplo de uso:
#ruta_imagen = 'DnsDums\\intelequia.es.dnsmap.png'  # Reemplaza con la ruta de la imagen que deseas redimensionar
#resize_image(ruta_imagen)