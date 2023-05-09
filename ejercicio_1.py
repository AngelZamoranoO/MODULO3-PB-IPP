

validador = True
arreglo = []
print(' Ingrese numeros para ser ordenados de mayor a menor, el 0 es para salir del programa')
while validador:
    numeroIngresado = int(input('Ingrese numero:  '))
    
    if numeroIngresado !=0:
        arreglo.append(numeroIngresado)
    else:
        validador = False



for x in range(len(arreglo)):
    for i in range(0,len(arreglo)-x-1):
        if arreglo[i] < arreglo[i+1]:
            aux = arreglo[i]
            arreglo[i] = arreglo[i+1] 
            arreglo[i+1] = aux
          


print("arreglo modificado",arreglo)
