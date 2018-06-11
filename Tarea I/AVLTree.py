import unicodedata

def noacc(word):
    s = ''.join((c for c in unicodedata.normalize('NFD',word) if unicodedata.category(c) != 'Mn'))
    return s

class Contact:
    def __init__(self,n,ln,ph,e):
        self.left = None
        self.right = None
        self.parent = None
        self.name = noacc(n)
        self.last_name = noacc(ln)
        self.full_name = (self.name + " " + self.last_name).title()
        self.phone = ph
        self.email = e
    def __str__(self):
        return str(self.full_name + " ~~~~ " + self.phone + " ~~~~ " + self.email)

class Book:
    def __init__(self):
        self.root = None
        self.heigth = 0
    def empty(self):
        return self.root == None
     def search_name(self,n,root,contacts=[]):
        if self.empty():
            print("Su libreta de contactos está vacía.")
            return
        if root is None:
            pass
        else:
            self.search_name(n,root.left,contacts)
            if root.name == n:
                contacts.append(root)
            self.search_name(n,root.right,contacts)
            return contacts
    def search_last_name(self,ln,root,contacts=[]):
        if self.empty():
            print("Su libreta de contactos está vacía.")
            return
        if root is None:
            pass
        else:
            self.search_last_name(ln,root.left,contacts)
            if root.last_name == ln:
                contacts.append(root)
            self.search_last_name(ln,root.right,contacts)
            return contacts
    def search_phone(self,ph,root,contacts=[]):
        if self.empty():
            print("Su libreta de contactos está vacía.")
            return
        if root is None:
            pass
        else:
            self.search_phone(ph,root.left,contacts)
            if root.phone == ph:
                contacts.append(root)
            self.search_phone(ph,root.right,contacts)
            return contacts
    def search_email(self,e,root,contacts=[]):
        if self.empty():
            print("Su libreta de contactos está vacía.")
            return
        if root is None:
            pass
        else:
            self.search_email(e,root.left,contacts)
            if root.email == e:
                contacts.append(root)
            self.search_email(e,root.right,contacts)
            return contacts
    def print_book(self,root):
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        if root is None:
            pass
        else:
            self.print_book(root.left)
            print(root)
            self.print_book(root.right)