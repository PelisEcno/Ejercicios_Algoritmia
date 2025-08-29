# Programa que determina si un número ingresado por el usuario es múltiplo de 5.

# Entradas:
# Este programa solicita al usuario que ingrese un número entero.
# Luego, valida si la entrada es un número entero válido.
#
# Salidas:
# Finalmente, se muestra un mensaje indicando si el número es múltiplo de 5 o no.
# En caso de error en la entrada, se muestra un mensaje de advertencia.
#
# Procesos:
# Se verifica si el número ingresado es divisible entre 5 utilizando el operador módulo (%).

print("Este algoritmo te dirá si un número es múltiplo de 5.")
input("Presiona la tecla Enter para continuar...")

try:
    # Entrada: Solicita al usuario un número entero
    num = int(input("Ingresa un número entero: "))

    # Proceso: Verifica si el número es múltiplo de 5
    if num % 5 == 0:
        # Salida: Muestra que el número es múltiplo de 5
        print(f"El número {num} es múltiplo de 5.")
    else:
        # Salida: Muestra que el número no es múltiplo de 5
        print(f"El número {num} no es múltiplo de 5.")
except ValueError:
    # Salida: Mensaje de error si la entrada no es válida
    print("Entrada no válida. Por favor, ingresa un número entero.")