# Crear un programa que convierta un número entero (mayor que 1 y menor o igual que 1000) a número romano.
# Creamos la clase 'Romano' que contiene el método para convertir a número romano.

class Romano:
    """
    Clase que convierte un número entero a su equivalente en números romanos.
    """

    def numero_romanos(numero):
        """
        Convierte un número entero a su representación en números romanos.
        Parámetros:
            numero (int): Número entero entre 1 y 1000 a convertir.
        Retorna:
            str: Representación del número en números romanos.
        """
        # Lista de tuplas con los valores numéricos y sus equivalentes en números romanos
        valores = [
            (1000, 'M'),  # 1000 se representa como 'M'
            (900, 'CM'),  # 900 se representa como 'CM'
            (500, 'D'),   # 500 se representa como 'D'
            (400, 'CD'),  # 400 se representa como 'CD'
            (100, 'C'),   # 100 se representa como 'C'
            (90, 'XC'),   # 90 se representa como 'XC'
            (50, 'L'),    # 50 se representa como 'L'
            (40, 'XL'),   # 40 se representa como 'XL'
            (10, 'X'),    # 10 se representa como 'X'
            (9, 'IX'),    # 9 se representa como 'IX'
            (5, 'V'),     # 5 se representa como 'V'
            (4, 'IV'),    # 4 se representa como 'IV'
            (1, 'I')      # 1 se representa como 'I'
        ]

        # Verifica si el número está fuera del rango válido (1-1000)
        if numero < 1 or numero > 1000:
            print("El número debe estar entre 1 y 1000")
            return ""  # Retorna una cadena vacía si el número no es válido

        resultado_romano = ""  # Inicializa una cadena vacía para almacenar el resultado en números romanos

        # Itera sobre la lista de valores y sus equivalentes en números romanos
        for valor, romano in valores:
            while numero >= valor:  # Mientras el número sea mayor o igual al valor actual
                resultado_romano += romano  # Agrega el símbolo romano al resultado
                numero -= valor  # Reduce el número restando el valor actual

        return resultado_romano  # Retorna la representación en números romanos


# Programa principal
print("Conversión de Números Enteros a Romanos")  # Mensaje de bienvenida

numero = int(input("Ingrese un número entero (1-1000): "))  # Solicita al usuario que ingrese un número
num_romano = Romano.numero_romanos(numero)  # Llama al método para convertir el número a romano
print(f"El número {numero} en romano es: {num_romano}")  # Muestra el resultado