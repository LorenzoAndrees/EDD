import unicodedata

def noacc(word):
    s = ''.join((c for c in unicodedata.normalize('NFD',word) if unicodedata.category(c) != 'Mn'))
    return s
def str2num(key):
    return sum([ord(c) for c in key])
def hashstr(key,size):
    return str2num(key)%size

class Contact:
    def __init__(self,n,ln,ph,e):
        self.next = None
        self.prev = None
        self.name = (noacc(n)).title()
        self.last_name = (noacc(ln)).title()
        self.full_name = self.name + " " + self.last_name
        self.phone = ph
        self.email = e
    def __str__(self):
        return str(self.full_name + " ~~~~ " + self.phone + " ~~~~ " + self.email)

class Book:
    def __init__(self,size):
        self.list = [None]*size
        self.size= size
    def empty(self):
        return self.list == None
    def bubblelist(list):
        for i in range(len(lista)-1,0,-1):
            for j in range(i):
                if (lista[j]).last_name>(lista[j+1]).last_name
                    lista[j],lista[j+1] = lista[j+1],lista[j]
                elif (lista[j]).last_name==(lista[j+1]).last_name
                    (lista[j]).name>(lista[j+1]).name
                        lista[j],lista[j+1] = lista[j+1],lista[j]
            print(lista)
        return lista
    def put(self,contact):
        key= contact.last_name
        for k in self.list[hashstr(key,self.size)]:
            if k == key:
                repeat +=1
        key = contact.last_name + " (" + repeat + ")"
        pos = hashstr(key,self.size)
        if self.list[pos] is not None:
            self.list[pos].append([key,contact])
            bubblelist(self.list)
            return
        else:
            self.list[pos] =[]
            self.list[pos].append([key,contact])
            return
    def search_name(self,n):
        if self.empty():
            print("Su Libreta de Contactos está vacía.")
            return 0
        else:
            find = False
            contacts = []
            for e in self.list[hashstr(n,self.size)]:
                if e[0] is n:
                    contacts.append(e[1])
                    find = True
            if not find:
                print("El contacto no se encuentra en la libreta")
                return 0
            return contacts
    def search_last_name(self,ln):
        if self.empty():
            print("Su Libreta de Contactos está vacía.")
            return 0
        else:
            find = False
            contacts = []
            for e in self.list[hashstr(ln,self.size)]:
                if e[0] is ln:
                    contacts.append(e[1])
                    find = True
            if not find:
                print("El contacto no se encuentra en la libreta")
                return 0
            return contacts
    def search_phone(self,ph):
        if self.empty():
            print("Su Libreta de Contactos está vacía.")
            return 0
        else:
            find = False
            contacts = []
            for e in self.list[hashstr(ph,self.size)]:
                if e[0] is ph:
                    contacts.append(e[1])
                    find = True
            if not find:
                print("El contacto no se encuentra en la libreta")
                return 0
            return contacts
    def search_email(self,e):
        if self.empty():
            print("Su Libreta de Contactos está vacía.")
            return 0
        else:
            find = False
            contacts = []
            for i in self.list[hashstr(e,self.size)]:
                if i[0] is e:
                    contacts.append(i[1])
                    find = True
            if not find:
                print("El contacto no se encuentra en la libreta")
                return 0
            return contacts
    def delete_name(self,n,priority):
        if self.search_name(n) is not 0:
            
    def printHash(self):
        for contact in self.lista:
            if contact is not None:
                print(contact)