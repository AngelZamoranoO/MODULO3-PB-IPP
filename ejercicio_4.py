def esAnagrama(data1, data2):
    return sorted(data1) == sorted(data2)

print('Debe escribir 2 palabras para verificar si son anagramas: \n')
palabra1 = str(input('palabra 1: '))
palabra2 = str(input('\npalabra 2: '))

if esAnagrama(palabra1,palabra2):
    print('Son anagramas',palabra1,'  ',palabra2)
else:
    print('No son anagramas',palabra1,'  ',palabra2) 
