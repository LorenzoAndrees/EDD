import unicodedata

def noacc(word):
    s = ''.join((c for c in unicodedata.normalize('NFD',word) if unicodedata.category(c) != 'Mn'))
    return s
def letter2num(key):        #en este caso, "letter" es la primera letra de la key: el apellido
    return ord(key[0])
def hashstr(key):
    return letter2num(key)%65    #hash con 25 posiciones, correspondientes a las 25 letras del abecedario, sin contar la ñ


class Contact:
    def __init__(self,n,ln,ph,e):
        self.name = (noacc(n)).title()
        self.last_name = (noacc(ln)).title()
        self.full_name = self.name + " " + self.last_name
        self.phone = ph
        self.email = e
    def __str__(self):
        return str(self.full_name + " ~~~~ " + self.phone + " ~~~~ " + self.email)

class Book:
    def __init__(self):
        self.list = [None]*25
    def empty(self):
        return self.list == None
    def put(self,contact):
        key = contact.last_name
        pos = hashstr(key)
        if self.list[pos] is not None:
            self.list[pos].append([key,contact])
        else:
            self.list[pos] =[]
            self.list[pos].append([key,contact])
            self.list[pos].sort()
    def search_name(self,n):
        n= (noacc(n)).title()
        if self.empty():
            print("Su Libreta de Contactos está vacía.")
            return 0
        else:
            find = False
            contacts = []
            for e in self.list:
                if e is not None:
                    for x in e:
                        if x[1].name == n:
                            contacts.append(x[1])
                            find = True
            if not find:
                print("El contacto no se encuentra en la libreta")
                return 0
            return contacts
    def search_last_name(self,ln):
        ln= (noacc(ln)).title()
        if self.empty():
            print("Su Libreta de Contactos está vacía.")
            return 0
        else:
            find = False
            contacts = []
            for e in self.list:
                if e is not None:
                    for x in e:
                        if x[1].last_name == ln:
                            contacts.append(x[1])
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
            for e in self.list:
                if e is not None:
                    for x in e:
                        if x[1].phone == ph:
                            contacts.append(x[1])
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
            for i in self.list:
                if i is not None:
                    for x in i:
                        print(x[1])
                        if x[1].email == e:
                            contacts.append(x[1])
                            find = True
            if not find:
                print("El contacto no se encuentra en la libreta")
                return 0
            return contacts
    def delete_name(self,n,priority):
        delete = False
        if self.search_name(n) is not 0:
            contact = self.search_name(n)[priority-1]
            for k in self.list:
                if k is not None:
                    for x in k:
                        if x[1] == contact:
                            k.remove(x)
                            delete = True
                            if len(x) == 0:
                                x = None
                                k= None
        if not delete:
            print("No sé encontró el contacto en la libreta.")
        return
    def delete_last_name(self,ln,priority):
        delete = False
        if self.search_last_name(ln) is not 0:
            contact = self.search_last_name(ln)[priority-1]
            for k in self.list:
                if k is not None:
                    for x in k:
                        if x[1] == contact:
                            k.remove(x)
                            delete = True
                            if len(x) == 0:
                                x = None
                                k = None
        if not delete:
            print("No sé encontró el contacto en la libreta.")
        return
    def delete_phone(self,ph,priority):
        delete = False
        if self.search_phone(ph) is not 0:
            contact = self.search_phone(ph)[priority-1]
            for k in self.list:
                if k is not None:
                    for x in k:
                        if x[1] == contact:
                            k.remove(x)
                            delete = True
                            if len(x) == 0:
                                x=None
                                k = None
        if not delete:
            print("No sé encontró el contacto en la libreta.")
        return
    def delete_email(self,e,priority):
        delete = False
        if self.search_email(e) is not 0:
            contact = self.search_email(e)[priority-1]
            for k in self.list:
                if k is not None:
                    for x in k:
                        if x[1] == contact:
                            k.remove(x)
                            delete = True
                            if len(x) == 0:
                                x = None
                                k = None
        if not delete:
            print("No sé encontró el contacto en la libreta.")
        return
    def printbook(self):
        for c in self.list:
            if c is not None:
                for x in c:
                    print(x[1])