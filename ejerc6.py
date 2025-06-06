# Realizar un programa que pida un mes y un año (superior a 1900) y muestre el calendario del mes de esta manera:
# L M M J V S D
# ==========================
# 1 2 3 4 5 6
# 7 8 9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# Para ello es necesario averiguar que día de la semana (Lunes, Martes, ...) corresponde con un fecha determinada.
# Hay muchas maneras de calcularlo: nosotros vamos a contar los días que han trascurridos
# desde el año 1900 (NOTA: ten en cuenta que queremos realizar un calendario que empiece en lunes, no en domingo).

class calendario:
    """
    Clase que proporciona métodos para trabajar con calendarios,
    incluyendo la verificación de años bisiestos, cálculo de días en un mes,
    y generación de un calendario mensual.
    """

    def bisiesto(year):
        """
        Determina si un año es bisiesto.
        Parámetros:
            year (int): Año a verificar.
        Retorna:
            bool: True si el año es bisiesto, False en caso contrario.
        """
        if year % 4 == 0:  # Verifica si el año es divisible entre 4
            if year % 100 == 0:  # Si es divisible entre 100, verifica si también es divisible entre 400
                if year % 400 == 0:  # Si es divisible entre 400, es bisiesto
                    return True
                else:
                    return False  # Si no es divisible entre 400, no es bisiesto
            else:
                return True  # Si no es divisible entre 100, pero sí entre 4, es bisiesto
        return False  # Si no es divisible entre 4, no es bisiesto

    def dias_mes(month, year):
        """
        Calcula el número de días en un mes dado un año.
        Parámetros:
            month (int): Mes (1-12).
            year (int): Año.
        Retorna:
            int: Número de días en el mes.
        """
        if month == 2:  # Si el mes es febrero
            if calendario.bisiesto(year):  # Verifica si el año es bisiesto
                return 29  # Febrero tiene 29 días en un año bisiesto
            else:
                return 28  # Febrero tiene 28 días en un año no bisiesto
        elif month in [4, 6, 9, 11]:  # Meses con 30 días
            return 30
        else:  # Todos los demás meses tienen 31 días
            return 31

    def dias_1900(month, year):
        """
        Calcula el número total de días desde el 1 de enero de 1900 hasta el primer día del mes y año dados.
        Parámetros:
            month (int): Mes (1-12).
            year (int): Año.
        Retorna:
            int: Número total de días.
        """
        dias = 0  # Inicializa el contador de días

        for ye in range(1900, year):  # Itera sobre todos los años desde 1900 hasta el año dado
            if calendario.bisiesto(ye):  # Si el año es bisiesto, suma 366 días
                dias += 366
            else:  # Si no es bisiesto, suma 365 días
                dias += 365

        for mes in range(1, month):  # Itera sobre todos los meses hasta el mes dado
            dias = dias + calendario.dias_mes(mes, year)  # Suma los días de cada mes
        return dias  # Retorna el total de días

    def imprimir_calendario(month, year):
        """
        Imprime el calendario de un mes y año dados.
        Parámetros:
            month (int): Mes (1-12).
            year (int): Año.
        """
        print("\n L  M  M  J  V  S  D")  # Encabezado del calendario
        print("==========================")

        dia1 = calendario.dias_1900(month, year) % 7  # Calcula el día de la semana del primer día del mes
        dias_mes = calendario.dias_mes(month, year)  # Obtiene el número de días en el mes

        print("   " * dia1, end="")  # Imprime espacios en blanco para alinear el primer día
        for dia in range(1, dias_mes + 1):  # Itera sobre todos los días del mes
            print(f"{dia:2d} ", end="")  # Imprime el número del día con formato
            if (dia + dia1) % 7 == 0:  # Si es el último día de la semana, imprime una nueva línea
                print()
        print()  # Imprime una línea en blanco al final


# Programa principal
print("Mostrar el calendario de un mes y año (desde 1900)")  # Mensaje de bienvenida

year = int(input("Ingrese el año (mayor a 1900): "))  # Solicita el año al usuario
month = int(input("Ingrese el mes (1-12): "))  # Solicita el mes al usuario

if year < 1900:  # Verifica si el año es menor a 1900
    print("El año debe ser mayor a 1900")
elif month < 1 or month > 12:  # Verifica si el mes está fuera del rango válido
    print("El mes debe estar entre 1 y 12")
else:
    calendario.imprimir_calendario(month, year)  # Llama al método para imprimir el calendario