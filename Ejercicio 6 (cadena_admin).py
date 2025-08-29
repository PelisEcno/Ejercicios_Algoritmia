# Programa que verifica si el usuario tiene permisos de administrador
#
# Entradas:
# Solicita el nombre de usuario (cadena de texto).
#
# Salidas:
# Indica si el acceso es concedido o denegado.
#
# Procesos:
# Compara el nombre ingresado con "admin".

print("Este algoritmo verifica si tienes permisos de administrador.")
input("Presiona la tecla Enter para continuar...")

# Entrada
usuario = input("Ingresa tu nombre de usuario: ")

# Proceso y salida
if usuario == "admin":
    print("Acceso concedido. ¡Bienvenido, administrador!")
else:
    print(f"Acceso denegado. El usuario '{usuario}' no tiene permisos de administrador.")