import random

listaNormal = []
listaAsendente = listaNormal
listaDescendente = listaNormal
 
for i in range (10):
    listaNormal.append(random.randint(1, 100))

print("LISTA NORMAL") 
print(listaNormal)


#FUNCION PARA LISTA ASCENDENTE:
def lista2(listaAsendente):
    for i in listaAsendente:
        for j in range(0, len(listaAsendente)-1):
            if listaAsendente[j] > listaAsendente[j+1]:
                aux = listaAsendente[j]
                listaAsendente[j] = listaAsendente[j+1]
                listaAsendente[j+1] = aux
    return listaAsendente


#FUNCION PARA LISTA DESCENDENTE:
def lista3(listaDescendente):
    for i in listaDescendente:
        for j in range(0, len(listaDescendente)-1):
            if listaDescendente[j] < listaDescendente[j+1]:
                aux = listaDescendente[j]
                listaDescendente[j] = listaDescendente[j+1]
                listaDescendente[j+1] = aux
    return listaDescendente

print("LISTA ASCENDENTE")
print(lista2(listaAsendente))
print("LISTA DESCENDENTE")
print(lista3(listaDescendente))