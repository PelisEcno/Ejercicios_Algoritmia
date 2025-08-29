#Programa para determinar si un numero es positivo o negativo.

#Nombre: Programa para determinar si un numero es positivo o negativo.

#Entradas:
#   Numero: Numero a verificar

# Salidas:
#    Mensaje que indica si es negativo o es positivo.

# Proceso: Pide el numero que desea verificar. Verifica si es es positivo o negativo. Imprime el mensaje que indica si es positivo o no

numero = float(input("Ingrese un número: "))
if numero < 0:
    print("El número es negativo")
else:
    print("El número no es negativo")
