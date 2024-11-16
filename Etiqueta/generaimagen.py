from PIL import Image, ImageDraw, ImageFont

def generate_image(template_path, constant_texts, constant_positions, texts, positions, font_path, font_size, text_color, bold_font_path):
    # Cargar la imagen de plantilla
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)

    # Cargar las fuentes
    font = ImageFont.truetype(font_path, font_size)
    bold_font = ImageFont.truetype(bold_font_path, font_size)

    # Agregar los textos constantes a la imagen con fuente en negrita
    for text, position in zip(constant_texts, constant_positions):
        draw.text(position, text, font=bold_font, fill=text_color)

    # Agregar cada línea de texto dinámico a la imagen
    for text, position in zip(texts, positions):
        if ':' in text:
            # Separar la parte izquierda y derecha del texto
            left_part, right_part = text.split(':', 1)
            left_part += ':'

            # Dibujar la parte izquierda en negrita
            draw.text(position, left_part, font=bold_font, fill=text_color)

            # Calcular la posición de la parte derecha
            left_bbox = draw.textbbox(position, left_part, font=bold_font)
            left_width = left_bbox[2] - left_bbox[0]
            right_position = (position[0] + left_width, position[1])

            # Dibujar la parte derecha en regular
            draw.text(right_position, right_part, font=font, fill=text_color)
        else:
            # Dibujar el texto completo en regular si no contiene ':'
            draw.text(position, text, font=font, fill=text_color)

    return image

if __name__ == "__main__":
    template_path = "plantilla.jpg"  # Ruta de la imagen de plantilla

    # Datos constantes
    constant_texts = [
        "Nombre: Eduardo Cabrera Espinoza",
        "Rut: 5.546.781-1     Teléfono: 56 9 20547036"
    ]
    constant_positions = [
        (170, 30),  # Coordenadas para el nombre
        (170, 50)  # Coordenadas para el rut y telefono
    ]

    # Solicitar datos dinámicos al usuario
    tipo_entrega = input("Ingrese el tipo de entrega: ")
    nombre = input("Ingrese el nombre: ")
    rut = input("Ingrese el RUT: ")
    direccion1 = input("Ingrese la primera parte de la dirección: ")
    direccion2 = input("Ingrese la segunda parte de la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    empresa_transporte = input("Ingrese la empresa de transporte: ")

    # Solicitar la cantidad de copias
    num_copias = int(input("Ingrese la cantidad de copias: "))

    # Crear una lista de textos dinámicos
    texts = [
        f"Tipo de Entrega: {tipo_entrega}",
        f"Nombre: {nombre}",
        f"RUT: {rut}",
        f"Dirección: {direccion1}",
        f"{direccion2}",
        f"Teléfono: {telefono}",
        f"Empresa de Transporte: {empresa_transporte}"
    ]

    # Definir la posición inicial y el incremento vertical para los textos dinámicos
    initial_position = (170, 85)
    line_height = 20  # Altura de cada línea de texto

    # Calcular las posiciones para cada línea de texto dinámico
    positions = [(initial_position[0], initial_position[1] + i * line_height) for i in range(len(texts))]

    font_path = "arial.ttf"          # Ruta de la fuente TrueType
    bold_font_path = "arialbd.ttf"   # Ruta de la fuente TrueType en negrita
    font_size = 14                   # Tamaño de la fuente ajustado
    text_color = (0, 0, 0)           # Color del texto negro (R, G, B)

    # Generar las imágenes y guardarlas en una lista
    images = []
    for _ in range(num_copias):
        image = generate_image(template_path, constant_texts, constant_positions, texts, positions, font_path, font_size, text_color, bold_font_path)
        images.append(image)

    # Crear páginas del PDF con 3 imágenes por página y márgenes
    pdf_pages = []
    margin = 35  # Tamaño del margen en píxeles
    for i in range(0, len(images), 3):
        # Crear una nueva página en blanco con márgenes
        page_width, page_height = images[0].size[0] + 2 * margin, images[0].size[1] * 3 + 4 * margin
        page = Image.new('RGB', (page_width, page_height), (255, 255, 255))

        # Pegar hasta 3 imágenes en la página con márgenes
        for j in range(3):
            if i + j < len(images):
                page.paste(images[i + j], (margin, margin + j * (images[0].size[1] + margin)))

        pdf_pages.append(page)

    # Guardar todas las páginas en un único archivo PDF
    pdf_path = "resultado.pdf"
    pdf_pages[0].save(pdf_path, save_all=True, append_images=pdf_pages[1:], format="PDF")