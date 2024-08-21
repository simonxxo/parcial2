#parcial 2
mi_lista1 = ["a",  "b", "c", 3, 4, 5, 5, 5, 6, 78, 3, 33]
mi_lista2 = ["a", 3, "c", 56, 7, "hola"]


#Numeros repetidos
def numeros_repetidos(lista):
    print(lista)
    repetidos = 0
    for i in lista:
        if lista.count(i) > 1:
            repetidos += 1
    
    if repetidos == 0:
        print("no hay elementos repetidos")
    else:
        print("la lista tiene uno o mas elementos repetidos")

numeros_repetidos(mi_lista1)

#encontrar string
def encontrar_str(lista):
    print(lista)
    cadenas = []
    for i in lista:
        if type(i) == str:
            cadenas.append(i)
    if len(cadenas) == 0:
        print("no hay strings")
    else:
        print("Las cadenas encontradas son: ", cadenas)
#encontrar_str(mi_lista1)

#3 diferencia de lista
def diferencia_de_listas(lista1, lista2):
    print(lista1, lista2)
    diferencias = []
    for i in lista1:
        if i in lista2:
            pass
        else:
            diferencias.append(i)
    if len(diferencias) == 0:
        print("ambas listas tienen los mismos elementos")
    else:
        print("Los elementos que estan en la primera lista y NO en la segunda son: ", diferencias)
#diferencia_de_listas(mi_lista1, mi_lista2)

def promedio(arreglo_de_reales):
    print(arreglo_de_reales)
    sum = 0
    for i in arreglo_de_reales:
        sum += i
    prom = sum / len(arreglo_de_reales)
    print ("el promedio de los valores en la lista es", prom)

#romedio(arreglo_reales)

#mediana
def mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:  # Si el número de elementos es impar
        mediana = lista_ordenada[n // 2]
    else:  # Si el número de elementos es par
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    print("la lista ordenada es: ", lista_ordenada)
    # Imprimir la mediana
    print("La mediana es:", mediana)


lista_de_enteros = [2, 4, 6, 45, 76, 3, 1]
#mediana(lista_de_enteros)



#acualizacion correcion del parcial
def mediana2(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:  # Si el número de elementos es impar
        mediana = lista_ordenada[n // 2]
        print(lista_ordenada)
        print("la mediana es ", mediana)
    else:  # Si el número de elementos es par
        mediana = [lista_ordenada[n // 2 - 1],  lista_ordenada[n // 2]]
        print("la lista ordenada es: ", lista_ordenada)
        # Imprimir la mediana
        print("La mediana es:",lista_ordenada[n // 2 - 1],  lista_ordenada[n // 2])


lista_de_enteros = [2, 4, 8, 6, 45, 76, 3, 1]
mediana2(lista_de_enteros)
    
            
            
            
       
        
    
