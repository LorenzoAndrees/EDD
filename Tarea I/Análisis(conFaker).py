from faker import Faker
import time
import os
from time import time
def pause():
    input("Pulse enter, para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    return
def return_name(string):
    c = 0
    n2 = str()
    nfinal = [None]*2
    for k in string:
        if k == " ":
            c+=1
        if c ==2:
                break
        n2 += k
    nfinal[0],nfinal[1] = n2.split(" ")
    return nfinal
fake = Faker()
m = "Resultados de tiempo de complejidad para una EDD"
structures = ["Lista simple","Árbol Binario de búsqueda","Árbol AVL","Árbol 2-3","Hash"]
size = [10,20,100,1000]
print(m.center(50," "))
for i in range(5):
    print(i+1,")",structures[i])
option = int(input())
os.system('cls' if os.name == 'nt' else 'clear')
m = "Cantidad de contactos:"
print(m.center(50," "))
for i in range(4):
    print(i+1,")",size[i])
s = int(input())
os.system('cls' if os.name == 'nt' else 'clear')
if option == 1:
    import Lista
    libreta = Lista.Book()
    print("Ahora se agregaran los contactos.")
    pause()
    tinicial = time()
    for i in range(size[s-1]):
        contact = Lista.Contact("","","912345678","por_defecto@mail.cl")
        fakename = fake.name()
        fullname = return_name(fakename)
        contact.name,contact.last_name = fullname[0],fullname[1]
        contact.full_name = contact.name + " " + contact.last_name
        libreta.add(contact)
    ttotal = time() - tinicial
    print("Cantidad de segundos en agregar ",size[s-1]," contactos: ",ttotal)
    pause()
    print ("Ahora se buscará un contacto por su apellido.")
    pause()
    last_name = input("Buscar Apellido: ")
    tinicial = time()
    libreta.search_last_name(last_name)
    ttotal = time() - tinicial
    print("Cantidad de segundos en buscar un contacto: ",ttotal)
    print("Ahora se borrará un contacto:")
    pause()
    name = input("Borrar Nombre: ")
    tinicial = time()
    libreta.delete_name(name,1)
    ttotal = time() - tinicial
    print("Cantidad de segundos en borrar un contacto: ",ttotal)
elif option == 2:
    import BST
    libreta = BST.Book()
    print("Ahora se agregaran los contactos.")
    pause()
    tinicial = time()
    for i in range(size[s-1]):
        contact = BST.Contact("","","912345678","por_defecto@mail.cl")
        fakename = fake.name()
        fullname = return_name(fakename)
        contact.name,contact.last_name = fullname[0],fullname[1]
        contact.full_name = contact.name + " " + contact.last_name
        libreta.add(contact)
    ttotal = time() - tinicial
    print("Cantidad de segundos en agregar ",size[s-1]," contactos: ",ttotal)
    pause()
    print ("Ahora se buscará un contacto por su apellido.")
    pause()
    last_name = input("Buscar Apellido: ")
    tinicial = time()
    libreta.search_last_name(last_name,libreta.root)
    ttotal = time() - tinicial
    print("Cantidad de segundos en buscar un contacto: ",ttotal)
    print("Ahora se borrará un contacto:")
    pause()
    name = input("Borrar Nombre: ")
    tinicial = time()
    libreta.delete_name(name,libreta.root,1)
    ttotal = time() - tinicial
    print("Cantidad de segundos en borrar un contacto: ",ttotal)
elif option == 3:
    import AVLTree
    libreta = AVLTree.Book()
    print("Ahora se agregaran los contactos.")
    pause()
    tinicial = time()
    for i in range(size[s-1]):
        contact = AVLTree.Contact("","","912345678","por_defecto@mail.cl")
        fakename = fake.name()
        fullname = return_name(fakename)
        contact.name,contact.last_name = fullname[0],fullname[1]
        contact.full_name = contact.name + " " + contact.last_name
        libreta.add(libreta.root,contact)
    ttotal = time() - tinicial
    print("Cantidad de segundos en agregar ",size[s-1]," contactos: ",ttotal)
    pause()
    print ("Ahora se buscará un contacto por su apellido.")
    pause()
    last_name = input("Buscar Apellido: ")
    tinicial = time()
    libreta.search_last_name(last_name,libreta.root)
    ttotal = time() - tinicial
    print("Cantidad de segundos en buscar un contacto: ",ttotal)
    print("Ahora se borrará un contacto:")
    pause()
    name = input("Borrar Nombre: ")
    tinicial = time()
    libreta.delete_name(name,libreta.root,0)
    ttotal = time() - tinicial
    print("Cantidad de segundos en borrar un contacto: ",ttotal)
elif option == 4:
    import TwoThreeTree
    libreta = TwoThreeTree.Book()
    print("Ahora se agregaran los contactos.")
    pause()
    tinicial = time()
    for i in range(size[s-1]):
        contact = TwoThreeTree.Contact("","","912345678","por_defecto@mail.cl")
        fakename = fake.name()
        fullname = return_name(fakename)
        contact.name,contact.last_name = fullname[0],fullname[1]
        contact.full_name = contact.name + " " + contact.last_name
        libreta.insert(contact)
    ttotal = time() - tinicial
    print("Cantidad de segundos en agregar ",size[s-1]," contactos: ",ttotal)
    pause()
    print ("Ahora se buscará un contacto por su apellido.")
    pause()
    last_name = input("Buscar Apellido: ")
    tinicial = time()
    libreta.search_last_name(last_name,libreta.root)
    ttotal = time() - tinicial
    print("Cantidad de segundos en buscar un contacto: ",ttotal)
    print("Ahora se borrará un contacto:")
    pause()
    name = input("Borrar Nombre: ")
    tinicial = time()
    libreta.delete_name(name,libreta.root,0)
    ttotal = time() - tinicial
    print("Cantidad de segundos en borrar un contacto: ",ttotal)
elif option == 5:
    import Hash
    libreta = Hash.Book()
    print("Ahora se agregaran los contactos.")
    pause()
    tinicial = time()
    for i in range(size[s-1]):
        contact = Hash.Contact("","","912345678","por_defecto@mail.cl")
        fakename = fake.name()
        fullname = return_name(fakename)
        contact.name,contact.last_name = fullname[0],fullname[1]
        libreta.put(contact)
    ttotal = time() - tinicial
    print("Cantidad de segundos en agregar ",size[s-1]," contactos: ",ttotal)
    print ("Ahora se buscará un contacto por su apellido.")
    pause()
    last_name = input("Buscar Apellido: ")
    tinicial = time()
    libreta.search_last_name(last_name)
    ttotal = time() - tinicial
    print("Cantidad de segundos en buscar un contacto: ",ttotal)
    print("Ahora se borrará un contacto:")
    pause()
    name = input("Borrar Nombre: ")
    tinicial = time()
    libreta.delete_name(name,1)
    ttotal = time() - tinicial
    print("Cantidad de segundos en borrar un contacto: ",ttotal)