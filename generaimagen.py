from PIL import Image, ImageDraw, ImageFont

def generate_image(template_path, texts, positions, font_path, font_size, text_color):
    # Cargar la imagen de plantilla
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)

    # Cargar la fuente
    font = ImageFont.truetype(font_path, font_size)

    # Agregar cada línea de texto a la imagen
    for text, position in zip(texts, positions):
        draw.text(position, text, font=font, fill=text_color)

    return image

if __name__ == "__main__":
    template_path = "plantilla.jpg"  # Ruta de la imagen de plantilla

    # Solicitar datos dinámicos al usuario
    tipo_entrega = input("Ingrese el tipo de entrega: ")
    nombre = input("Ingrese el nombre: ")
    rut = input("Ingrese el RUT: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    empresa_transporte = input("Ingrese la empresa de transporte: ")

    # Solicitar la cantidad de copias
    num_copias = int(input("Ingrese la cantidad de copias: "))

    # Crear una lista de textos y posiciones
    texts = [
        f"Tipo de Entrega: {tipo_entrega}",
        f"Nombre: {nombre}",
        f"RUT: {rut}",
        f"Dirección: {direccion}",
        f"Teléfono: {telefono}",
        f"Empresa de Transporte: {empresa_transporte}"
    ]

    # Definir la posición inicial y el incremento vertical
    initial_position = (180, 110)
    line_height = 20  # Altura de cada línea de texto

    # Calcular las posiciones para cada línea de texto
    positions = [(initial_position[0], initial_position[1] + i * line_height) for i in range(len(texts))]

    font_path = "arial.ttf"          # Ruta de la fuente TrueType
    font_size = 14                   # Tamaño de la fuente ajustado
    text_color = (0, 0, 0)           # Color del texto negro (R, G, B)

    # Generar las imágenes y guardarlas en una lista
    images = []
    for _ in range(num_copias):
        image = generate_image(template_path, texts, positions, font_path, font_size, text_color)
        images.append(image)

    # Crear páginas del PDF con 3 imágenes por página
    pdf_pages = []
    for i in range(0, len(images), 3):
        # Crear una nueva página en blanco
        page_width, page_height = images[0].size[0], images[0].size[1] * 3
        page = Image.new('RGB', (page_width, page_height), (255, 255, 255))

        # Pegar hasta 3 imágenes en la página
        for j in range(3):
            if i + j < len(images):
                page.paste(images[i + j], (0, j * images[0].size[1]))

        pdf_pages.append(page)

    # Guardar todas las páginas en un único archivo PDF
    pdf_path = "resultado.pdf"
    pdf_pages[0].save(pdf_path, save_all=True, append_images=pdf_pages[1:], format="PDF")