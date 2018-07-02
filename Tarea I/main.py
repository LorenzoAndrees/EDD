import os
import unicodedata
def noacc(word):
    s = ''.join((c for c in unicodedata.normalize('NFD',word) if unicodedata.category(c) != 'Mn'))
    return s
def pause():
    input("Pulse enter, para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    return
def list_menu(): #menú para EDD: Lista
    import Lista
    libreta = Lista.Book()
    options = ["Agregar","Buscar","Eliminar","Revisar Libreta de contactos"]
    attributes = ["Nombre","Apellido","N° Telefónico","Email"]
    data = []
    message = "¿Que desea hacer?"
    while True:
        print(message.center(50," "))
        for i in range(4):
            print(i+1,")",options[i])
        print("0 <-- Salir")
        selection = int(input("Selección: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if selection == 1: #AGREGAR
            k=0
            for k in range(4):
                print("Ingrese ",attributes[k], " del contacto: ")
                value = input()
                data.append(value)
            contact = Lista.Contact(data[0],data[1],data[2],data[3])
            data.clear()
            libreta.add(contact)
            print("Contacto agregado :)")
            pause()
            continue
        elif selection == 2: #BUSCAR
            print("Desea buscar por: ")
            for n in range(4):
                print(n+1,")",attributes[n])
            print("0 <-- Volver Atrás")
            bselection = int(input("Selección: "))
            if bselection == 1: #BUSCAR POR NOMBRE
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("Ingrese Nombre del contacto: ")
                if libreta.search_name(name) is not 0:
                    print("Contactos encontrados: ")
                    for n in libreta.search_name(name):
                        print(n)
                pause()
                continue
            elif bselection == 2: #BUSCAR POR APELLIDO
                os.system('cls' if os.name == 'nt' else 'clear')
                lname = input("Ingrese Apellido del contacto: ")
                if  libreta.search_last_name(lname) is not 0:
                    print("Contactos encontrados: ")
                    for l in libreta.search_last_name(lname):
                        print(l)
                pause()
                continue
            elif bselection == 3: #BUSCAR POR TELÉFONO
                os.system('cls' if os.name == 'nt' else 'clear')
                phone = input("Ingrese N° Telefónico del contacto: ")
                if  libreta.search_phone(phone) is not 0:
                    print("Contactos encontrados: ")
                    for p in libreta.search_phone(phone):
                        print(p)
                pause()
                continue
            elif bselection == 4: #BUSCAR POR EMAIL
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese Email del contacto: ")
                if libreta.search_email(email) is not 0:
                    print("Contactos encontrados: ")
                    for e in libreta.search_email(email):
                        print(e)
                pause()
                continue
            elif bselection == 0: #VOLVER ATRÁS
                continue
            else: #SELECCIÓN INVÁLIDA
                print("Ingrese una selección válida... Volviendo al menú :(")
                pause()
                continue
        elif selection == 3: #ELIMINAR
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Desea Eliminar por: ")
            for d in range(4):
                print(d+1,")",attributes[d])
            print("0 <-- Volver Atrás")
            eselection = int(input("Selección: "))
            if eselection == 1: #ELIMINAR POR NOMBRE
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("Ingrese Nombre del contacto: ")
                if  libreta.search_name(name) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_name(name):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_name(name)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_name(name,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 2: #ELIMINAR POR APELLIDO
                os.system('cls' if os.name == 'nt' else 'clear')
                lname = input("Ingrese Apellido del contacto: ")
                if  libreta.search_last_name(lname) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_last_name(lname):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_last_name(lname)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_last_name(lname,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 3: # ELIMINAR POR TELÉFONO
                os.system('cls' if os.name == 'nt' else 'clear')
                phone = input("Ingrese N° Telefónico del contacto: ")
                if  libreta.search_phone(phone) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_phone(phone):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_phone(phone)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_phone(phone,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 4: #ELIMINAR POR EMAIL
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese Email del contacto: ")
                if  libreta.search_email(email) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_email(email):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_email(email)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_email(email,delete)
                        print("Contacto eliminado :)")
        elif selection == 4: #VER LIBRETA DE CONTACTOS
            print("Mostrando Libreta de contactos: ")
            libreta.print_book()
            pause()
            continue
        elif selection == 0: #SALIR
            break
    return
def tree_menu(option): #menú para EDD: Árboles
    options = ["Agregar","Buscar","Eliminar","Revisar Libreta de contactos"]
    attributes = ["Nombre","Apellido","N° Telefónico","Email"]
    data = []
    message = "¿Que desea hacer?"
    if option == 1:
        import BST
        libreta = BST.Book()
    elif option == 2:
        import AVLTree
        libreta = AVLTree.Book()
    while True:
        print(message.center(50," "))
        for i in range(4):
            print(i+1,")",options[i])
        print("0 <-- Salir")
        selection = int(input("Selección: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if selection == 1: #AGREGAR
            k=0
            for k in range(4):
                print("Ingrese ",attributes[k], " del contacto: ")
                value = input()
                data.append(value)
            if option == 1:
                contact = BST.Contact("","","","")
            if option == 2:
                contact = AVLTree.Contact("","","","")
            contact.name = noacc(data[0]).title()
            contact.last_name = noacc(data[1]).title()
            contact.phone = data[2]
            contact.email = data[3]
            data.clear()
            contact.full_name = contact.name + " " + contact.last_name
            if option == 1:
                libreta.add(contact)
            elif option == 2:
                libreta.add(libreta.root,contact)
            print("Contacto agregado :)")
            pause()
            continue
        elif selection == 2: #BUSCAR
            print("Desea buscar por: ")
            for n in range(4):
                print(n+1,")",attributes[n])
            print("0 <-- Volver Atrás")
            bselection = int(input("Selección: "))
            if bselection == 1: #BUSCAR POR NOMBRE
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("Ingrese Nombre del contacto: ")
                print("Contactos encontrados: ")
                contactos = libreta.search_name(name,libreta.root)
                for i in range(len(contactos)):
                    print(i+1,")",contactos[i])
                pause()
                continue
            elif bselection == 2: #BUSCAR POR APELLIDO
                os.system('cls' if os.name == 'nt' else 'clear')
                lname = input("Ingrese Apellido del contacto: ")
                if libreta.search_last_name(lname,libreta.root):
                    print("Contactos encontrados: ")
                    contactos = libreta.search_last_name(lname,libreta.root)
                    for i in range(len(contactos)):
                        print(i+1,")",contactos[i])
                pause()
                continue
            elif bselection == 3: #BUSCAR POR TELÉFONO
                os.system('cls' if os.name == 'nt' else 'clear')
                phone = input("Ingrese N° Telefónico del contacto: ")
                if libreta.search_phone(phone,libreta.root):
                    print("Contactos encontrados: ")
                    contactos = libreta.search_phone(phone,libreta.root)
                    for i in range(len(contactos)):
                        print(i+1,")",contactos[1])
                pause()
                continue
            elif bselection == 4: #BUSCAR POR EMAIL
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese Email del contacto: ")
                if libreta.search_email(email,libreta.root):
                    print("Contactos encontrados: ")
                    contactos = libreta.search_email(email,libreta.root)
                    for i in range(len(contactos)):
                        print(i+1,")",contactos[1])
                pause()
                continue
            elif bselection == 0: #VOLVER ATRÁS
                pause()
                continue
            else: #SELECCIÓN INVÁLIDA
                print("Ingrese una selección válida... Volviendo al menú :(")
                pause()
                continue
        elif selection == 3: #ELIMINAR
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Desea Eliminar por: ")
            for d in range(4):
                print(d+1,")",attributes[d])
            print("0 <-- Volver Atrás")
            eselection = int(input("Selección: "))
            if eselection == 1: #ELIMINAR POR NOMBRE
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("Ingrese Nombre del contacto: ")
                if  libreta.search_name(name,libreta.root):
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_name(name,libreta.root):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_name(name,libreta.root)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_name(name,libreta.root,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 2: #ELIMINAR POR APELLIDO
                os.system('cls' if os.name == 'nt' else 'clear')
                lname = input("Ingrese Apellido del contacto: ")
                if  libreta.search_last_name(lname,libreta.root):
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_last_name(lname,libreta.root):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_last_name(lname,libreta.root)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_last_name(lname,libreta.root,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 3: # ELIMINAR POR TELÉFONO
                os.system('cls' if os.name == 'nt' else 'clear')
                phone = input("Ingrese N° Telefónico del contacto: ")
                if  libreta.search_phone(phone,libreta.root):
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_phone(phone,libreta.root):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_phone(phone,libreta.root)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_phone(phone,libreta.root,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 4: #ELIMINAR POR EMAIL
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese Email del contacto: ")
                if  libreta.search_email(email,libreta.root):
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_email(email,libreta.root):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_email(email,libreta.root)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_email(email,libreta.root,delete)
                        print("Contacto eliminado :)")
        elif selection == 4: #VER LIBRETA DE CONTACTOS
            print("Mostrando Libreta de contactos: ")
            libreta.print_book(libreta.root)
            pause()
            continue
        elif selection == 0: #SALIR
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    return
def twothreetree_menu():#menú para EDD: Árbol 2-3
    import TwoThreeTree
    libreta = TwoThreeTree.Book()
    options = ["Agregar","Buscar","Eliminar","Revisar Libreta de contactos"]
    attributes = ["Nombre","Apellido","N° Telefónico","Email"]
    data = []
    message = "¿Que desea hacer?"
    while True:
        print(message.center(50," "))
        for i in range(4):
            print(i+1,")",options[i])
        print("0 <-- Salir")
        selection = int(input("Selección: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if selection == 1: #AGREGAR
            k=0
            for k in range(4):
                print("Ingrese ",attributes[k], " del contacto: ")
                value = input()
                data.append(value)
            contact = TwoThreeTree.Contact(data[0],data[1],data[2],data[3])
            data.clear()
            libreta.insert(contact)
            print("Contacto agregado :)")
            pause()
            continue
        elif selection == 2: #BUSCAR
            print("Desea buscar por: ")
            for n in range(4):
                print(n+1,")",attributes[n])
            print("0 <-- Volver Atrás")
            bselection = int(input("Selección: "))
            if bselection == 1: #BUSCAR POR NOMBRE
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("Ingrese Nombre del contacto: ")
                if libreta.search_name(name,libreta.root) is not 0:
                    print("Contactos encontrados: ")
                    for n in libreta.search_name(name,libreta.root):
                        print(n)
                pause()
                continue
            elif bselection == 2: #BUSCAR POR APELLIDO
                os.system('cls' if os.name == 'nt' else 'clear')
                lname = input("Ingrese Apellido del contacto: ")
                if  libreta.search_last_name(lname,libreta.root) is not 0:
                    print("Contactos encontrados: ")
                    for l in libreta.search_last_name(lname,libreta.root):
                        print(l)
                pause()
                continue
            elif bselection == 3: #BUSCAR POR TELÉFONO
                os.system('cls' if os.name == 'nt' else 'clear')
                phone = input("Ingrese N° Telefónico del contacto: ")
                if  libreta.search_phone(phone,libreta.root) is not 0:
                    print("Contactos encontrados: ")
                    for p in libreta.search_phone(phone,libreta.root):
                        print(p)
                pause()
                continue
            elif bselection == 4: #BUSCAR POR EMAIL
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese Email del contacto: ")
                if libreta.search_email(email,libreta.root) is not 0:
                    print("Contactos encontrados: ")
                    for e in libreta.search_email(email,libreta.root):
                        print(e)
                pause()
                continue
            elif bselection == 0: #VOLVER ATRÁS
                pause()
                continue
            else: #SELECCIÓN INVÁLIDA
                print("Ingrese una selección válida... Volviendo al menú :(")
                pause()
                continue
        elif selection == 3: #ELIMINAR
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Desea Eliminar por: ")
            for d in range(4):
                print(d+1,")",attributes[d])
            print("0 <-- Volver Atrás")
            eselection = int(input("Selección: "))
            if eselection == 1: #ELIMINAR POR NOMBRE
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("Ingrese Nombre del contacto: ")
                if  libreta.search_name(name,libreta.root) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_name(name,libreta.root):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_name(name,libreta.root)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_name(name,libreta.root,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 2: #ELIMINAR POR APELLIDO
                os.system('cls' if os.name == 'nt' else 'clear')
                lname = input("Ingrese Apellido del contacto: ")
                if  libreta.search_last_name(lname,libreta.root) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_last_name(lname,libreta.root):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_last_name(lname,libreta.root)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_last_name(lname,libreta.root,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 3: # ELIMINAR POR TELÉFONO
                os.system('cls' if os.name == 'nt' else 'clear')
                phone = input("Ingrese N° Telefónico del contacto: ")
                if  libreta.search_phone(phone) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_phone(phone,libreta.root):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_phone(phone,libreta.root)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_phone(phone,libreta.root,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 4: #ELIMINAR POR EMAIL
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese Email del contacto: ")
                if  libreta.search_email(email,libreta.root) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_email(email,libreta.root):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_email(email,libreta.root)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_email(email,libreta.root,delete)
                        print("Contacto eliminado :)")
        elif selection == 4: #VER LIBRETA DE CONTACTOS
            print("Mostrando Libreta de contactos: ")
            libreta.print_preorder()
            pause()
            continue
        elif selection == 0: #SALIR
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    return
def hash_menu(): #menú para EDD: Hash
    import Hash
    libreta = Hash.Book()
    options = ["Agregar","Buscar","Eliminar","Revisar Libreta de contactos"]
    attributes = ["Nombre","Apellido","N° Telefónico","Email"]
    data = []
    message = "¿Que desea hacer?"
    while True:
        print(message.center(50," "))
        for i in range(4):
            print(i+1,")",options[i])
        print("0 <-- Salir")
        selection = int(input("Selección: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if selection == 1: #AGREGAR
            k=0
            for k in range(4):
                print("Ingrese ",attributes[k], " del contacto: ")
                value = input()
                data.append(value)
            contact = Hash.Contact(data[0],data[1],data[2],data[3])
            data.clear()
            libreta.put(contact)
            print("Contacto agregado :)")
            pause()
            continue
        elif selection == 2: #BUSCAR
            print("Desea buscar por: ")
            for n in range(4):
                print(n+1,")",attributes[n])
            print("0 <-- Volver Atrás")
            bselection = int(input("Selección: "))
            if bselection == 1: #BUSCAR POR NOMBRE
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("Ingrese Nombre del contacto: ")
                if libreta.search_name(name) is not 0:
                    print("Contactos encontrados: ")
                    for n in libreta.search_name(name):
                        print(n)
                pause()
                continue
            elif bselection == 2: #BUSCAR POR APELLIDO
                os.system('cls' if os.name == 'nt' else 'clear')
                lname = input("Ingrese Apellido del contacto: ")
                if  libreta.search_last_name(lname) is not 0:
                    print("Contactos encontrados: ")
                    for l in libreta.search_last_name(lname):
                        print(l)
                pause()
                continue
            elif bselection == 3: #BUSCAR POR TELÉFONO
                os.system('cls' if os.name == 'nt' else 'clear')
                phone = input("Ingrese N° Telefónico del contacto: ")
                if  libreta.search_phone(phone) is not 0:
                    print("Contactos encontrados: ")
                    for p in libreta.search_phone(phone):
                        print(p)
                pause()
                continue
            elif bselection == 4: #BUSCAR POR EMAIL
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese Email del contacto: ")
                if libreta.search_email(email) is not 0:
                    print("Contactos encontrados: ")
                    for e in libreta.search_email(email):
                        print(e)
                pause()
                continue
            elif bselection == 0: #VOLVER ATRÁS
                continue
            else: #SELECCIÓN INVÁLIDA
                print("Ingrese una selección válida... Volviendo al menú :(")
                pause()
                continue
        elif selection == 3: #ELIMINAR
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Desea Eliminar por: ")
            for d in range(4):
                print(d+1,")",attributes[d])
            print("0 <-- Volver Atrás")
            eselection = int(input("Selección: "))
            if eselection == 1: #ELIMINAR POR NOMBRE
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("Ingrese Nombre del contacto: ")
                if  libreta.search_name(name) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_name(name):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_name(name)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_name(name,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 2: #ELIMINAR POR APELLIDO
                os.system('cls' if os.name == 'nt' else 'clear')
                lname = input("Ingrese Apellido del contacto: ")
                if  libreta.search_last_name(lname) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_last_name(lname):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_last_name(lname)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_last_name(lname,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 3: # ELIMINAR POR TELÉFONO
                os.system('cls' if os.name == 'nt' else 'clear')
                phone = input("Ingrese N° Telefónico del contacto: ")
                if  libreta.search_phone(phone) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_phone(phone):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_phone(phone)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_phone(phone,delete)
                        print("Contacto eliminado :)")
                pause()
                continue
            elif eselection == 4: #ELIMINAR POR EMAIL
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese Email del contacto: ")
                if  libreta.search_email(email) is not 0:
                    print("Contactos encontrados: ")
                    count = 1
                    for n in libreta.search_email(email):
                        print(count,")",n)
                        count += 1
                    print("¿Cuál desea eliminar?")
                    delete = int(input("Selección: "))
                    if delete > len(libreta.search_email(email)) or delete <= 0:
                        print("Selección inválida, volviendo al menú.")
                        pause()
                        continue
                    else:
                        libreta.delete_email(email,delete)
                        print("Contacto eliminado :)")
        elif selection == 4: #VER LIBRETA DE CONTACTOS
            print("Mostrando Libreta de contactos: ")
            libreta.print_book()
            pause()
            continue
        elif selection == 0: #SALIR
            break
    return
def strc_menu(): #menú General
    structures = ["Lista simple","Árboles","Hash"]
    trees = ["Binario de búsqueda","AVL","2-3","Volver atrás"]
    while True:
        message = "Seleccione la Estructura de datos con la que desea operar:"
        print(message.center(50," "))
        for i in range(3):
            print(i+1,")",structures[i])
        print("0 <-- Salir",)
        selection = int(input("Selección: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if selection == 1: #ENTRAR A MENÚ DE LISTA
            list_menu()
            continue
        elif selection == 2: #ENTRAR A MENÚ DE ÁRBOLES 
            message = "Seleccione el Árbol con el que desea operar:"
            message.center(50," ")
            for i in range(3):
                print(i+1,")",trees[i])
            print("0 <--", trees[i+1])
            tree_selection = int(input("Selección: "))
            if tree_selection == 1 or tree_selection == 2: #ÁRBOL BINARIO DE BÚSQUEDA O AVL
                os.system('cls' if os.name == 'nt' else 'clear')
                tree_menu(tree_selection)
                continue
            elif tree_selection == 3: #ÁRBOL 2-3
                os.system('cls' if os.name == 'nt' else 'clear')
                twothreetree_menu()
                continue
            elif tree_selection == 0: #VOLVER ATRÁS
                continue
            else: #SELECCIÓN INVÁLIDA
                print("Ingrese una selección válida ...")
                pause()
                continue
        elif selection == 3: #ENTRAR A MENÚ DE HASH
            hash_menu()
            continue
        elif selection == 0: #SALIR
            print("Saliendo...")
            break
        else: #SELECCIÓN INVÁLIDA
            print("Ingrese una selección válida ...")
            pause()
            continue
if __name__ == "__main__":
    for i in range(5): # IMPRIMIR BIENVENIDA
        if i == 2:
            message = "BIENVENIDO A SU LIBRETA DE CONTACTOS <3"
            print(message.center(55," "))
        elif i == 0 or i == 4:
            message = "="
            print(message.center(55,"="))
    print("Recuerde que para este programa, cada estructura de datos que use, corresponde a una libreta de contactos distinta.")
    strc_menu()
    print("Adiós :(")