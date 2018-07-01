import unicodedata

def noacc(word):
    s = ''.join((c for c in unicodedata.normalize('NFD',word) if unicodedata.category(c) != 'Mn'))
    return s
    
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
    def __init__(self):
        self.head = None
        self.length = 0
    def empty(self):
        return self.head == None
    def merge(self, first, second):
        if first is None:
            return second 
        if second is None:
            return first
        if first.last_name < second.last_name:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None  
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
    def mergeSort(self,tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead
        second = self.split(tempHead)
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)
        return self.merge(tempHead, second)
    def sort(self):
        if self.head and self.head.next:
            i = self.head
            while i.next:
                selected = i
                j = i.next
                while j:
                    if j.last_name < selected.last_name:
                        selected = j
                    j = j.next
                if not selected==i:
                    i, selected = selected,i
                i = i.next
    def split(self, tempHead):
        fast = slow =  tempHead
        while(True):
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next  
        temp = slow.next
        slow.next = None
        return temp
    def add(self,contact):
        self.length += 1
        if self.empty():
            print("Añadiendo ",contact.name," ",contact.last_name,"...")
            self.head = contact
        else:
            aux = self.head
            name_repeat = False
            repeat = 0
            while aux:
                #print("Error")
                if aux.name == contact.name and aux.last_name == contact.last_name:
                    name_repeat = True
                    repeat += 1
                if aux.next is None:
                    aux.next = contact
                    contact.prev = aux
                    break
                aux = aux.next
            print("Añadiendo ",contact.name," ",contact.last_name, "...")
            if name_repeat and repeat is not 0:
                contact.full_name = (contact.name + " " + contact.last_name).title() + " (" + str(repeat) + ")"
        self.head = self.mergeSort(self.head)
           # self.sort()
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
        n= (noacc(n)).title()
        if self.search_name(n) is not 0:
            self.delete(self.search_name(n)[priority-1])
            self.length -= 1
    def delete_last_name(self,ln,priority):
        ln= (noacc(ln)).title()
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