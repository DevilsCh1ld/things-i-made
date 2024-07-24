#This is my first "Serious Program", so any suggestions would be greatly appreciated#

print("""
      Bienvenido a la calculadora
      Para salir escribe "Salir"
      Las Operaciones disponibles son suma, multi, div y resta
""")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un numero: ")
        if resultado.lower() == "salir":
            break
    resultado = int(resultado)
    op = input("Ingresar Operacion: ")
    if op.lower() == "salir":
            break
    n2 = (input("Ingrese el Segundo Numero: "))
    if n2.lower() == "salir":
            break
    n2 = int(n2)
    if op.lower() == "suma":
       suma = resultado + n2
       print(f"El resultado es: {suma}")
    elif op.lower() == "multi":
        multi = resultado * n2
        print(f"El resultado es: {multi}")
    elif op.lower() == "div":
        div = resultado // n2
        print(f"El resultado es: {div}")
    elif op.lower() == "resta":
        resta = resultado - n2
        print(f"El resultado es: {resta}")
    else:
        print("Operacion no valida")
        break     
