
suma = 0
while True:
    entradaNumero = input("Ingrese un número //presione Enter para finalizar: ")
    
    if entradaNumero == "":
        break
    
    try:
        suma += int(entradaNumero)
    except ValueError as ValueError:
        print("Error: Debe ingresar un número. ValueError => ",ValueError)
        continue

print("La suma de los números ingresados es: ",suma)
