# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
# El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# • mostrar(): Muestra los datos de la cuenta.
# • ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# • retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:
    """
    Clase que representa una cuenta bancaria con un titular y una cantidad de dinero.
    """

    def __init__(self, titular, cantidad):
        """
        Constructor de la clase Cuenta.
        Inicializa el titular y la cantidad de la cuenta.
        Parámetros:
            titular (str): Nombre del titular de la cuenta.
            cantidad (float): Cantidad inicial de dinero en la cuenta.
        """
        if titular == "":  # Verifica si el titular está vacío
            print("¡Error! El Titular es un dato obligatorio...")  # Mensaje de error si el titular no se proporciona
        else:
            self.titular = titular  # Almacena el nombre del titular
            self.cantidad = cantidad  # Almacena la cantidad inicial de dinero

    def get_titular(self):
        """
        Retorna el nombre del titular de la cuenta.
        Retorna:
            str: Nombre del titular.
        """
        return self.titular  # Retorna el titular

    def get_cantidad(self):
        """
        Retorna la cantidad de dinero en la cuenta.
        Retorna:
            float: Cantidad de dinero.
        """
        return self.cantidad  # Retorna la cantidad

    def mostrar(self):
        """
        Muestra los datos de la cuenta (titular y cantidad).
        """
        print(" --------- Datos de la Cuenta --------- ")
        print(f"Nombre del Titular: {self.titular}")  # Muestra el nombre del titular
        print(f"Cantidad: {self.cantidad}")  # Muestra la cantidad de dinero

    def set_cantidad_Ingresada(self, ingresar_dinero):
        """
        Añade una cantidad de dinero a la cuenta.
        Parámetros:
            ingresar_dinero (float): Cantidad de dinero a ingresar.
        """
        if ingresar_dinero > 0:  # Verifica si la cantidad a ingresar es positiva
            self.cantidad += ingresar_dinero  # Incrementa la cantidad de dinero en la cuenta
        else:
            print("¡Error! No se puede ingresar una cantidad negativa")  # Mensaje de error si la cantidad es negativa

    def set_cantidad_Retirada(self, retirar_dinero):
        """
        Retira una cantidad de dinero de la cuenta.
        Parámetros:
            retirar_dinero (float): Cantidad de dinero a retirar.
        """
        if retirar_dinero > 0:  # Verifica si la cantidad a retirar es positiva
            self.cantidad -= retirar_dinero  # Reduce la cantidad de dinero en la cuenta
        else:
            print("¡Error! No se puede retirar una cantidad negativa")  # Mensaje de error si la cantidad es negativa


# Programa principal
while True:  # Bucle principal del menú
    print("\nBienvenido a Confiables S.A")
    print("Menú: ")
    print("1. Ingresar los datos para la cuenta")  # Opción para crear una nueva cuenta
    print("2. Salir")  # Opción para salir del programa
    opcion = int(input("Ingresa la opción: "))  # Solicita al usuario que seleccione una opción

    if opcion == 1:  # Si el usuario selecciona la opción 1
        titular = input("Ingresa el nombre del Titular de la Cuenta: ")  # Solicita el nombre del titular
        cantidad = float(input("Ingresa la cantidad inicial de la Cuenta: "))  # Solicita la cantidad inicial
        cuenta_iniciando = Cuenta(titular, cantidad)  # Crea una instancia de la clase Cuenta
        cuenta_iniciando.mostrar()  # Muestra los datos iniciales de la cuenta

        while True:  # Bucle secundario para operaciones en la cuenta
            print("\nMenú: ")
            print("1. Ingresar dinero a la Cuenta")  # Opción para ingresar dinero
            print("2. Retirar dinero de la cuenta")  # Opción para retirar dinero
            print("3. Salir al menú principal")  # Opción para regresar al menú principal
            seleccion = int(input("Ingresa la opción: "))  # Solicita al usuario que seleccione una opción

            if seleccion == 1:  # Si el usuario selecciona la opción 1
                ingresar_dinero = float(input("Ingresa la cantidad de dinero a Ingresar: "))  # Solicita la cantidad a ingresar
                cuenta_iniciando.set_cantidad_Ingresada(ingresar_dinero)  # Llama al método para ingresar dinero
                cuenta_iniciando.mostrar()  # Muestra los datos actualizados de la cuenta

            elif seleccion == 2:  # Si el usuario selecciona la opción 2
                retirar_dinero = float(input("Ingresa la cantidad de dinero a Retirar: "))  # Solicita la cantidad a retirar
                cuenta_iniciando.set_cantidad_Retirada(retirar_dinero)  # Llama al método para retirar dinero
                cuenta_iniciando.mostrar()  # Muestra los datos actualizados de la cuenta

            elif seleccion == 3:  # Si el usuario selecciona la opción 3
                break  # Sale del bucle secundario y regresa al menú principal

            else:  # Si el usuario ingresa una opción inválida
                print("Opción no válida. Intente nuevamente.")  # Mensaje de error

    elif opcion == 2:  # Si el usuario selecciona la opción 2
        print("Gracias por usar Confiables S.A")  # Mensaje de despedida
        break  # Sale del bucle principal, terminando el programa

    else:  # Si el usuario ingresa una opción inválida
        print("Opción no válida. Intente nuevamente.")  # Mensaje de error