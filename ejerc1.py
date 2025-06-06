# Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad que se ha entregado. La aplicación debe calcular el cambio correspondiente con el menor número de monedas y/o billetes posibles. 

class Pagar:
    """
    Clase que calcula y desglosa el cambio a entregar tras un pago.
    """

    def __init__(self, cantidad_total, cantidad_entregada):
        """
        Constructor de la clase Pagar.
        Inicializa las variables necesarias para calcular el cambio.
        """
        self.cantidad_total = cantidad_total  # Monto total a pagar
        self.cantidad_entregada = cantidad_entregada  # Monto entregado por el cliente
        self.cambio = cantidad_entregada - cantidad_total  # Calcula el cambio inicial

    def cambio_total(self):
        """
        Método que calcula y muestra el desglose del cambio en billetes y monedas.
        """
        billetes = [100000, 50000, 20000, 10000, 5000, 2000, 1000]  # Lista de denominaciones de billetes
        monedas = [1000, 500, 200, 100, 50]  # Lista de denominaciones de monedas

        if self.cantidad_entregada < self.cantidad_total:  # Verifica si el monto entregado es insuficiente
            print("La cantidad entregada es insuficiente")  # Mensaje de error
            return  # Termina el método si no hay suficiente dinero

        else:
            print(f"El cambio es: ${self.cambio}")  # Muestra el monto total del cambio

        cambio_por_entregar = self.cambio  # Variable para llevar el seguimiento del cambio restante
        print("Detalles del cambio: ")

        for billete in billetes:  # Itera sobre las denominaciones de billetes
            cantidad_billetes = cambio_por_entregar // billete  # Calcula cuántos billetes de esta denominación se pueden entregar

            if cantidad_billetes > 0:  # Si se pueden entregar billetes de esta denominación
                print(f"{cantidad_billetes} billetes de ${billete}")  # Muestra la cantidad de billetes
                cambio_por_entregar -= cantidad_billetes * billete  # Resta el valor entregado del cambio restante

        for moneda in monedas:  # Itera sobre las denominaciones de monedas
            cantidad_monedas = cambio_por_entregar // moneda  # Calcula cuántas monedas de esta denominación se pueden entregar

            if cantidad_monedas > 0:  # Si se pueden entregar monedas de esta denominación
                print(f"{cantidad_monedas} monedas de ${moneda}")  # Muestra la cantidad de monedas
                cambio_por_entregar -= cantidad_monedas * moneda  # Resta el valor entregado del cambio restante


while True:
    print("Bienvenido a Retiros Confiables S.A")  # Mensaje de bienvenida
    print("Menú: ")
    print("1. Ingresar datos de pago")  # Opción para ingresar los datos de pago
    print("2. Salir")  # Opción para salir del programa

    opcion = int(input("Seleccione una opción: "))  # Solicita al usuario que seleccione una opción del menú

    if opcion == 1:  # Si el usuario selecciona la opción 1
        cantidad_total = int(input("Ingrese la cantidad total a pagar: "))  # Solicita el monto total a pagar
        cantidad_entregada = int(input("Ingrese la cantidad a entregar: "))  # Solicita el monto entregado por el cliente
        pago = Pagar(cantidad_total, cantidad_entregada)  # Crea una instancia de la clase Pagar
        pago.cambio_total()  # Llama al método para calcular y mostrar el cambio

    elif opcion == 2:  # Si el usuario selecciona la opción 2
        print("Gracias por usar Retiros Confiables S.A")  # Mensaje de despedida
        break  # Sale del bucle while (termina el programa)

    else:  # Si el usuario ingresa una opción inválida
        print("Opción no válida. Intente nuevamente.")  # Mensaje de error