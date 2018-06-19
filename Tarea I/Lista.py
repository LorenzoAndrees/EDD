import unicodedata

def noacc(word):
    s = ''.join((c for c in unicodedata.normalize('NFD',word) if unicodedata.category(c) != 'Mn'))
    return s
    
class Contact:
    def __init__(self,n,ln,ph,e):
        self.next = None
        self.prev = None
        self.name = noacc(n)
        self.last_name = noacc(ln)
        self.full_name = (self.name + " " + self.last_name).title()
        self.phone = ph
        self.email = e
    def __str__(self):
        return str(self.full_name + " ~~~~ " + self.phone + " ~~~~ " + self.email)

class Book:
    def __init__(self):
        self.head = None
        self.length = 0
    def empty(self):
        return self.head == None
    def swap(self,node1,node2):
        node1.next = node2.next
        node2.next = node1
        node2.prev = node1.prev
        node1.prev = node2
        if node2.prev is not None:
            (node2.prev).next = node2
        else:
            self.head = node2
        if node1.next is not None:
            (node1.next).prev = node1
    def bubblesort(self):
        if self.empty():
            return
        else:
            aux = self.head
            n = self.length
            for i in range(n+1,0,-1):
                for j in range(0,i+1):
                    if aux.next is not None:
                        if aux.last_name > (aux.next).last_name:
                            self.swap(aux,aux.next)
                        elif aux.last_name == (aux.next).last_name:
                            if aux.name > (aux.next).name:
                                self.swap(aux,aux.next)
                        else:
                            aux = aux.next
                    else:
                        aux = self.head
                        break
    def add(self,contact):
        if self.empty():
            self.head = contact
        else:
            aux = self.head
            name_repeat = False
            repeat = 0
            while aux:
                print("Añadiendo ",contact.full_name)
                if aux.name == contact.name and aux.last_name == contact.last_name:
                    name_repeat = True
                    repeat += 1
                if aux.next is None:
                    aux.next = contact
                    contact.prev = aux
                    break
                aux = aux.next
            if name_repeat and repeat is not 0:
                contact.full_name = contact.name + " " + contact.last_name + " (" + str(repeat) + ")"
        self.length += 1
        self.bubblesort()
    def search_name(self,n):
        if self.empty():
            print("Su libreta de contactos está vacía.")
            return 0
        else:
            find = False
            aux = self.head
            contacts = []
            while aux:
                if aux.name == n:
                    find = True
                    contacts.append(aux)
                aux = aux.next
            if find is not True:
                print("El contacto no se encuentra en la libreta.")
                return 0
            return contacts
    def search_last_name(self,ln):
        if self.empty():
            print("Su libreta de contactos está vacía.")
            return 0
        else:
            find = False
            aux = self.head
            contacts = []
            while aux:
                if aux.last_name == ln:
                    find = True
                    contacts.append(aux)
                aux = aux.next
            if find is not True:
                print("El contacto no se encuentra en la libreta.")
                return 0
            return contacts
    def search_phone(self,ph):
        if self.empty():
            print("Su libreta de contactos está vacía.")
            return 0
        else:
            find = False
            aux = self.head
            contacts = []
            while aux:
                if aux.phone == ph:
                    find = True
                    contacts.append(aux)
                aux = aux.next
            if find is not True:
                print("El contacto no se encuentra en la libreta.")
                return 0
            return contacts
    def search_email(self,e):
        if self.empty():
            print("Su libreta de contactos está vacía.")
            return 0
        else:
            find = False
            aux = self.head
            contacts = []
            while aux:
                if aux.email == e:
                    find = True
                    contacts.append(aux)
                aux = aux.next
            if find is not True:
                print("El contacto no se encuentra en la libreta.")
                return 0
            return contacts
    def delete(self,node):
        if self.empty():
            print("Libreta de contactos vacia.")
            return
        if self.head == node:
            self.head = node.next
        if node.next is not None:
            (node.next).prev = node.prev
        if node.prev is not None:
            (node.prev).next = node.next 
    def delete_name(self,n,priority):
        if self.search_name(n) is not 0:
            self.delete(self.search_name(n)[priority-1])
            self.length -= 1
    def delete_last_name(self,ln,priority):
        if self.search_last_name(ln) is not 0:
            self.delete(self.search_last_name(ln)[priority-1])
            self.length -= 1
    def delete_phone(self,ph,priority):
        if self.search_phone(ph) is not 0:
            self.delete(self.search_phone(ph)[priority-1])
            self.length -= 1
    def delete_email(self,e,priority):
        if self.search_email(e) is not 0:
            self.delete(self.search_email(e)[priority-1])   
            self.length -= 1     
    def print_book(self):
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        else:
            aux = self.head
            while aux:
                print(aux,"\n-----------------------")
                aux = aux.next