
validador = True
arreglo = []

print(' Ingrese palabras para almacenar, el *** es para salir del programa')
while validador:
    palabraIngresado = str(input('Ingrese palabras:  '))
    
    if palabraIngresado !='***':
        try:
            arreglo.index(palabraIngresado)
        except:
            arreglo.append(palabraIngresado)
      
    else:
        validador = False


print("Se muestra el listado de palabras,no muestra palabras repetidas \n")
print(arreglo)