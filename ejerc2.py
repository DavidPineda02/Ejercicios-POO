# Realizar un algoritmo que permita descomponer un número en sus factores primos.

class Factores_Primos:
    """
    Clase que descompone un número en sus factores primos.
    """

    def __init__(self, numero):
        """
        Constructor de la clase Factores_Primos.
        Inicializa el número a descomponer.
        Parámetros:
            numero (int): Número entero positivo mayor que 1 a descomponer.
        """
        self.numero = numero  # Almacena el número a descomponer

    def descomponer(self):
        """
        Método que descompone el número en sus factores primos.
        Retorna:
            list: Lista de factores primos del número.
        """
        factores = []  # Lista para almacenar los factores primos encontrados
        divisor = 2  # Comienza con el primer número primo (2)
        num = self.numero  # Copia del número a descomponer

        while num > 1:  # Continúa mientras el número no sea 1
            if num % divisor == 0:  # Si el divisor es un factor primo del número
                factores.append(divisor)  # Agrega el divisor a la lista de factores
                num = num // divisor  # Divide el número entre el divisor
            else:
                divisor += 1  # Si no es divisible, prueba con el siguiente número

        return factores  # Retorna la lista de factores primos


# Programa principal
print("Descomposición de Números en Factores Primos")  # Mensaje de bienvenida

numero = int(input("Ingrese un número entero positivo mayor que 1: "))  # Solicita al usuario un número

if numero <= 1:  # Verifica si el número es menor o igual a 1
    print("Por favor, ingrese un número entero mayor que 1.")  # Mensaje de error si el número no es válido
else:
    numeros = Factores_Primos(numero)  # Crea una instancia de la clase Factores_Primos
    factores_primos = numeros.descomponer()  # Llama al método para descomponer el número
    print(f"Los factores primos de {numero} son:")  # Muestra el encabezado del resultado
    for factor in factores_primos:  # Itera sobre los factores primos encontrados
        print(f"- {factor}")  # Imprime cada factor primo en una línea separada