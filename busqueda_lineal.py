import random


def busqueda_lineal (lista, objetivo):
    match = False
    
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
        

if __name__ == '__main__':
    tamaño_lista = int(input('De que tamaño será la lista'))
    objetivo = int (input('Qué número quieres encontrar?'))
    
    lista = [random.randint(0,100) for i in range (tamaño_lista)]
    
    encontrado = busqueda_lineal(lista, objetivo)
    print (lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')