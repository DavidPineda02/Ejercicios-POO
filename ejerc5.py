# Diseñar un programa que permita adivinar al ordenador un determinado número entero y positivo para lo cual se deben leer los límites en los que está comprendido dicho número.
# El programa deberá ir mostrando números que recibirán las siguientes respuestas:
# 1. ‘S’, si es correcto.
# 2. ‘A’, si es más alto que el número a adivinar.
# 3. ‘B’, si es más bajo. Al finalizar el programa, se deberá escribir el número de intentos realizados para acertar el número.

class Adivinar_Numero:
    """
    Clase que implementa un juego donde la computadora intenta adivinar un número pensado por el usuario.
    Utiliza el método de búsqueda binaria para reducir el rango de posibles números.
    """

    def __init__(self, limite_inferior, limite_superior):
        """
        Constructor de la clase Adivinar_Numero.
        Inicializa los límites del rango y el contador de intentos.
        Parámetros:
            limite_inferior (int): Límite inferior del rango.
            limite_superior (int): Límite superior del rango.
        """
        self.limite_inferior = limite_inferior  # Almacena el límite inferior del rango
        self.limite_superior = limite_superior  # Almacena el límite superior del rango
        self.intentos = 0  # Inicializa el contador de intentos

    def jugar(self):
        """
        Método principal del juego.
        La computadora intenta adivinar el número del usuario utilizando búsqueda binaria.
        """
        while True:  # Bucle principal del juego
            # Calcula el número medio del rango actual como intento de adivinanza
            intento_adivinar = (self.limite_inferior + self.limite_superior) // 2
            self.intentos += 1  # Incrementa el contador de intentos

            # Pregunta al usuario si el número es correcto
            print(f"\n¿Es {intento_adivinar} tu número?")
            print("Responde con: S (sí), A (es más alto), B (es más bajo)")
            respuesta = input("Respuesta: ").upper()  # Lee y normaliza la respuesta del usuario

            if respuesta == "S":  # Si el usuario confirma que el número es correcto
                print(f"\n¡He adivinado tu número! Era {intento_adivinar}.")
                print(f"Total de intentos: {self.intentos}")  # Muestra el total de intentos realizados
                break  # Termina el bucle y finaliza el juego
            elif respuesta == "A":  # Si el número es más alto
                self.limite_inferior = intento_adivinar + 1  # Actualiza el límite inferior
            elif respuesta == "B":  # Si el número es más bajo
                self.limite_superior = intento_adivinar - 1  # Actualiza el límite superior
            else:  # Si la respuesta no es válida
                print("Respuesta inválida. Por favor, responde con S, A o B.")

# Programa principal
print("Bienvenido al juego de adivinar un número")  # Mensaje de bienvenida

limite_inferior = int(input("Ingrese el límite inferior: "))  # Solicita el límite inferior del rango
limite_superior = int(input("Ingrese el límite superior: "))  # Solicita el límite superior del rango

# Crea una instancia de la clase Adivinar_Numero con los límites ingresados
adivinar = Adivinar_Numero(limite_inferior, limite_superior)
adivinar.jugar()  # Inicia el juego llamando al método `jugar`   