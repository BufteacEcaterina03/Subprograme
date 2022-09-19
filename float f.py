def creare_lista():
    w=int(input("introdu nr de elemnte:"))
    lista_locala=[]
    for i in range(w):
        element=float(input("introdu elementul cu nr:"))
        lista_locala.append(element)
    return lista_locala
listaa=creare_lista()
print(listaa)