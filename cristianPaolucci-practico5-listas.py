#Ejercicio1

lista_numero = list (range (4, 101, 4))  #Se crea la lista llamada lista_número que contiene los números de 4 a 100, que va de 4 en 4
print (lista_numero)  #Se imprime por pantalla la lista de números
print (type(lista_numero))    #Se imprime tipo de dato de 'lista_numero', que será <class list>


#Ejercicio2

lista_elementos = [1, 30.3, False, "amarillo", -1]  #Se crea la lista llamada lista_elementosque contiene 5 elementos de distintos tipos
lista_penultimo = lista_elementos [3]   #Se accede al elemento en el índice 3 (cuarto elemento de la lista, conteao empieza en 0)
print (lista_penultimo)   #Se imprime 'amarillo'
print (lista_elementos [-3])  #Utilizando indexing con números negativos. Comienza desde atras hacia delante. Cuenta en forma distinta que
                              #la lista con indice positivo. en este caso con positivo desde 0 en adelante. Indice negativo desde 1 en adelante. 


#Ejercicio3

lista_vacia = []  #Se crea un lista llamada 'lista_vacia', que es una lista vacía de elementos
lista_vacia.append ("Mar del Plata") #Se agrega a lista_vacia el elemento, la cadena 'Mar del plata', utilizando el método .append para agregar a la lista
lista_vacia.append (False)  #Se agrega a lista_vacia el elemento 'False' , valor booleano, utilizando el método .append para agregar a la lista
lista_vacia.append (18) #Se agreaga a lisa_vacia el elemento '18', un entero, utilizando el método .append para agregar a la lista

print (lista_vacia)  #Se imprime lista con elementos [Mar del Plata, False, 18]



#Ejercicio4

animales = ["perro", "gato", "conejo", "pez"]  #Se crea la lista animales, que contiene 4 elementos, 4 string
animales [1] =  "loro" #Se reemplaza segundo valor de la lista animales con la palabra 'loro'
animales [3] = "oso"   #Se reemplaza último valor de la lista animales con la palabra 'oso'
print (animales)  #Se imprime lista animales con los valores cambiados [perro, loro, conejo, oso]

print ()
animales2 = ["gallina", "mono", "elefante", "jirafa"]  #Se crea lista animales2, que contiene 4 elementos, 4 string
animales2 [-1] = "oso" #Se indexa con un número negativo, se accede al elemento de la lista, desde el final hacia el principio, se reemplaza, el primer elemento desde atras, jirafa por oso
animales2 [-3] = "loro"  #Se indexa con un número negativo, se accede al elemento de la lista, desde el final hacia el principio, se reemplaza, el tercer elemento desde atras, mono por loro
print (animales2)  #Se imprime por pantalla lista2 cambiada, [gallina, loro, elefante, oso]


#Ejercicio5

#EL PROGRAMA
#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print (numeros)

#LO QUE HACE ESTE PROGRAMA ES ELIMINAR EL NUMERO MAYOR DE LA LISTA, EN ESTE CASO EL 22
#LO QUE IMPRIME POR PANTALLA ES  [8, 15, 3, 7]


#Ahora lo pruebo

numeros = [8, 15, 3, 22, 7]  #Se crea la lista numeros[], con 5 elementos, todos enteros
numeros.remove(max(numeros)) #Se elimina de la lista el número mas alto, el máximo, con la función max() junto a la función .remove()
print (numeros)  #Se imprime la nueva lista, [8, 15, 3, 7]


#Ejercicio6

numeros_multiplo_cinco = list (range(10, 31, 5))  #Se crea la lista numeros_multiplo_cinco con múltiplos de 5 que van de 10 a 30 incluido, utilizando función range para generar secuencia de número
                                                  #utilizando función list() para convertir resultado de range en una lista
print (numeros_multiplo_cinco [:2])   #Se imprime lista multiplo de 5, de 10 a 30



#Ejercicio7

autos = ["sedan", "polo", "suran", "gol"]  #Se crea la lista autos, que contiene 4 elementos, 4 string
autos [1] = "audi"  #Se reemplaza elemento 'polo' de la lista autos, el índice con valor 1 por el elemento ´audi´
autos [2] = "pickup"  #Se reemplaza elemento ´ruran´ de la lista autos, el índice con valor 2 por el elemento ´pickup´
print (autos)  #Se imprime lista modificada [sedan, audi, pickup, gol]

#Ejercicio8

dobles = [] #Se crea la lista vacia dobles[]
dobles.append (5 * 2)  #Se agrega a la lista dobles, el doble de el valor 5 utilizando la función .append() y realizando op. aritmética
dobles.append (10 * 2)   #Se agrega a la lista dobles, el doble de el valor 10 utilizando la función .append() y realizando op. aritmética
dobles.append (15 * 2)   #Se agrega a la lista dobles, el doble de el valor 15 utilizando la función .append() y realizando op. aritmética
print (dobles) #Se imprime ppor pantalla lista dobles cambiada [10, 20, 30]


#Ejercicio9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] #Se crea la lista compras, que a su vez contiene tres diferentes listas []
compras[2].append ("jugo")  #Se agrega con función .append() el elemento ´jugo´ a la lista de índice 2 dentro de lista compras
indice_fideos = compras[1].index("fideos")  #Se obtiene el índice del elemento ´fideos´ en la lista de índice 1 que se ubica dentro de la lista compras
compras[1] [indice_fideos] = "tallarines"  #Se cambia el valor en la posición obtenida para ´fideos´ por ´tallarines´
compras [0].remove("pan") #Se elimina el elemento 'pan' utilizando función .remove() de la lista de índice 0 de lista compras
print (compras)  #Se imprime nueva lista [[leche], [arroz, tallarines, salsa], [agua, jugo]]


#Ejercicio10

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]] #Se crea la lista lista_anidada, que contiene en su interior 4 lista anidadas, con elementos de diferente tipo
print (lista_anidada)  #Se imprime lista_anidada [[15], [True], [25, 5, 57.9, 30.6], [False]]

