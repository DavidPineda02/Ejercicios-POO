# Vamos a realizar dos funciones: una que nos permita convertir un número entero a binario, y otra que nos permita convertir un numero binario a decimal.
# • ConvertirABinario: Función que recibe un número entero y devuelve una cadena con la representación del número en binario.
# • ConvertirADecimal: Función que recibe una cadena con la representación binaria de un número y devuelve el número en decimal.
# Crea un programa principal que permita convertir de decimal a binario y de binario a decimal.

class Convertir_Numeros:
    """
    Clase que proporciona métodos para convertir números entre binario y decimal.
    """

    def ConvertirABinario(numero_entero):
        """
        Convierte un número entero a su representación binaria.
        Parámetros:
            numero_entero (int): Número entero positivo a convertir.
        Retorna:
            str: Representación binaria del número como una cadena.
        """
        binario = ""  # Inicializa una cadena vacía para almacenar el resultado binario

        while numero_entero > 0:  # Continúa mientras el número sea mayor que 0
            if numero_entero % 2 == 0:  # Verifica si el número es divisible entre 2
                bina = 0  # Si es divisible, el dígito binario es 0
            else:
                bina = 1  # Si no es divisible, el dígito binario es 1

            binario = str(bina) + binario  # Agrega el dígito binario al inicio de la cadena
            numero_entero = numero_entero // 2  # Divide el número entre 2 para continuar el proceso

        return binario  # Retorna la representación binaria como una cadena

    def ConvertirADecimal(numero_binario):
        """
        Convierte un número binario a su equivalente en decimal.
        Parámetros:
            numero_binario (str): Número binario como una cadena (Ej: "1010").
        Retorna:
            int: Valor decimal equivalente al número binario.
        """
        decimal = 0  # Inicializa el valor decimal en 0
        cuantos_numeros = len(numero_binario) - 1  # Calcula la posición del primer dígito binario

        for i in numero_binario:  # Itera sobre cada dígito del número binario
            decimal += int(i) * 2 ** cuantos_numeros  # Calcula el valor decimal correspondiente al dígito
            cuantos_numeros -= 1  # Reduce la posición para el siguiente dígito

        return decimal  # Retorna el valor decimal resultante


# Programa principal
print("Conversión de Números Enteros a Binarios y viceversa")  # Mensaje de bienvenida

while True:
    print("Menú: ")
    print("1. Convertir a Binario")  # Opción para convertir un número entero a binario
    print("2. Convertir a Decimal")  # Opción para convertir un número binario a decimal
    print("3. Salir")  # Opción para salir del programa

    seleccion = int(input("Seleccione una opción: "))  # Solicita al usuario que seleccione una opción

    if seleccion == 1:  # Si el usuario selecciona la opción 1
        numero_entero = int(input("Ingrese un número entero (Ej: 34, 156): "))  # Solicita un número entero
        binario = Convertir_Numeros.ConvertirABinario(numero_entero)  # Llama al método para convertir a binario
        print(f"El número {numero_entero} en binario es: {binario}")  # Muestra el resultado

    elif seleccion == 2:  # Si el usuario selecciona la opción 2
        numero_binario = input("Ingrese un número binario (Ej: 11100, 1010011): ")  # Solicita un número binario
        decimal = Convertir_Numeros.ConvertirADecimal(numero_binario)  # Llama al método para convertir a decimal
        print(f"El número {numero_binario} en decimal es: {decimal}")  # Muestra el resultado

    elif seleccion == 3:  # Si el usuario selecciona la opción 3
        print("Gracias por usar Conversión de Números Enteros a Binarios y viceversa")  # Mensaje de despedida
        break  # Sale del bucle while, terminando el programa

    else:  # Si el usuario ingresa una opción inválida
        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")  # Mensaje de error