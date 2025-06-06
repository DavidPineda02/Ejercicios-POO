# Escribir dos funciones que permitan calcular:
# • La cantidad de segundos en un tiempo dado en horas, minutos y segundos. La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
# • Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas, minutos y segundos o salir del programa.

class calcular_tiempo:
    """
    Clase que proporciona métodos para convertir tiempo entre horas, minutos, segundos y segundos totales.
    """

    def convertir_a_segundos(horas, minutos, segundos):
        """
        Convierte horas, minutos y segundos a segundos totales.
        Parámetros:
            horas (int): Cantidad de horas.
            minutos (int): Cantidad de minutos.
            segundos (int): Cantidad de segundos.
        Retorna:
            int: Tiempo total en segundos.
        """
        resultado_segundos = horas * 3600 + minutos * 60 + segundos  # Calcula los segundos totales
        return resultado_segundos  # Retorna el resultado

    def convertir_a_horas(segundos_totales):
        """
        Convierte segundos totales a horas, minutos y segundos.
        Parámetros:
            segundos_totales (int): Tiempo total en segundos.
        Retorna:
            tuple: Horas, minutos y segundos resultantes.
        """
        horas = segundos_totales // 3600  # Calcula las horas dividiendo entre 3600
        minutos = (segundos_totales % 3600) // 60  # Calcula los minutos restantes
        segundos = segundos_totales % 60  # Calcula los segundos restantes
        return horas, minutos, segundos  # Retorna una tupla con horas, minutos y segundos


# Programa principal
print("Conversión de Tiempo")  # Mensaje de bienvenida

while True:  # Bucle principal del menú
    print("Menú: ")
    print("1. Convertir a Segundos")  # Opción para convertir a segundos
    print("2. Convertir a Horas, Minutos y Segundos")  # Opción para convertir a horas, minutos y segundos
    print("3. Salir")  # Opción para salir del programa

    opcion = int(input("Seleccione una opción: "))  # Solicita al usuario que seleccione una opción

    if opcion == 1:  # Si el usuario selecciona la opción 1
        horas = int(input("Ingrese las horas: "))  # Solicita las horas
        minutos = int(input("Ingrese los minutos: "))  # Solicita los minutos
        segundos = int(input("Ingrese los segundos: "))  # Solicita los segundos

        # Llama al método para convertir a segundos
        segundos_totales = calcular_tiempo.convertir_a_segundos(horas, minutos, segundos)
        print(f"\nEl tiempo en segundos es: {segundos_totales} segundos\n")  # Muestra el resultado

    elif opcion == 2:  # Si el usuario selecciona la opción 2
        segundos_totales = int(input("Ingresa el total de segundos: "))  # Solicita los segundos totales

        # Llama al método para convertir a horas, minutos y segundos
        horas, minutos, segundos = calcular_tiempo.convertir_a_horas(segundos_totales)
        print(f"\n{segundos_totales} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos\n")

    elif opcion == 3:  # Si el usuario selecciona la opción 3
        print("Gracias por usar Conversión de Tiempo")  # Mensaje de despedida
        break  # Sale del bucle while, terminando el programa

    else:  # Si el usuario ingresa una opción inválida
        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")  # Mensaje de error