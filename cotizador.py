def main():
    # Entrada de datos
    largo_material = float(input("Ingrese el largo del material (cm): "))
    ancho_material = float(input("Ingrese el ancho del material (cm): "))
    costo_material = float(input("Ingrese el costo del material: "))
    costo_enlozado = float(input("Ingrese el costo de enlozado (poner 0 si no aplica): "))
    costo_perforacion = float(input("Ingrese el costo de perforación (poner 0 si no aplica): "))
    costo_mano_obra = float(input("Ingrese el costo de mano de obra: "))

    largo_bandeja = float(input("¿Cuál es el largo de la bandeja (cm)?: "))
    ancho_bandeja = float(input("¿Cuál es el ancho de la bandeja (cm)?: "))
    altura_bandeja = float(input("¿Cuál es la altura de la bandeja (cm)?: "))

    # Cálculo de las dimensiones reales de la bandeja considerando altura y holgura
    largo_real = largo_bandeja + (2 * altura_bandeja) + 1  # +1 por holgura
    ancho_real = ancho_bandeja + (2 * altura_bandeja) + 1  # +1 por holgura

    # Cálculo de cuántas bandejas caben en el material
    bandejas_largo = int(largo_material / largo_real)
    bandejas_ancho = int(ancho_material / ancho_real)
    total_bandejas = bandejas_largo * bandejas_ancho

    # Cálculo de costo por bandeja
    costo_bandeja = costo_material / total_bandejas
    costo_total_bandeja = costo_bandeja + costo_enlozado + costo_perforacion + costo_mano_obra

    print(f"Del material se pueden cortar {total_bandejas} bandejas.")
    print(f"El costo total por bandeja es: ${costo_total_bandeja:.2f}")

if __name__ == "__main__":
    main()
