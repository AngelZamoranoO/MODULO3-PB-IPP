
unPunto=['A','E','I','L','N','O','R','S','T','U']
dosPunto=['D','G']
tresPunto=['B', 'C','M' ,'P']
cuatroPunto=['F', 'H', 'V' ,'W' ,'Y']
cincoPunto=['K']
ochoPunto=['J', 'X']
diezPunto=['Q', 'Z']

puntos= int()
ingresoPalabra = str(input("Jugemos Scrabble, ingrese una palabra: \n"))
palabraMayuscula = ingresoPalabra.upper()

try:
    for letra in palabraMayuscula:
        
        if letra in unPunto:
            puntos=puntos+1
            
        if letra in dosPunto:
            puntos = puntos + 2
            
        if letra in tresPunto:
            puntos = puntos + 3
            
        if letra in cuatroPunto:
            puntos = puntos + 4
            
        if letra in cincoPunto:
            puntos = puntos + 5
            
        if letra in ochoPunto:
            puntos = puntos + 8
            
        if letra in diezPunto:
            puntos = puntos + 10
                        
        if letra in ' ':
            
            unPunto.index(letra)

    print('Obtenido la cantidad de',puntos, 'puntos')       

except ValueError as ValueError:
    print('No debe tener espacios la palabra, intentalo nuevamente, error =>',ValueError)




