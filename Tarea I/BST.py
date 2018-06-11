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
        self.depth = 0
    def empty(self):
        return self.root == None
    def __add(self,contact,root):
        if contact.name < root.name:
            if root.left is None:
                root.left = contact
                (root.left).parent = contact
            else:
                self.__add(contact,root.left)
        elif contact.name > root.name:
            if root.right is None:
                root.right = contact
                (root.right).parent = contact
            else:
                self.__add(contact,root.right)
        elif contact.name == root.name:
            if contact.last_name < root.last_name:
                if root.left is None:
                    root.left = contact
                    (root.left).parent = contact
                else:
                    self.__add(contact,root.left)
            elif contact.last_name > root.last_name:
                if root.right is None:
                    root.right = contact
                    (root.right).parent = contact
                else:
                    self.__add(contact,root.right)
    def add(self,contact):
        if self.empty():
            self.root = contact
        else:
            self.__add(contact,self.root)
    def search_name(self,n,root,names):
        if root is None:
            pass
        else:
            pass
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

if __name__ == "__main__":
    lorenzo = Contact("Lorenzo","Alfaro","86709403","lorenzo.alfaro@mail.udp.cl")
    lucia = Contact("Lucia","Marquez","74472555","lucia.marquez@mail.udp.cl")
    Libreta = Book()
    Libreta.add(lorenzo)
    Libreta.add(lucia)
    Libreta.print_book(Libreta.root)
    marilens = Contact("Marilena","Bravo","61922535","marilenab06@hotmail.com")
    print("Añadiendo a marilens")
    Libreta.add(marilens)
    Libreta.print_book(Libreta.root)
    print("Añadiendo Aroldo")
    aroldo = Contact("Aroldo","Alfaro","61922535","aroldoalfaro@hotmail.com")
    Libreta.add(aroldo)
    Libreta.print_book(Libreta.root)
    lorenzo2 = Contact("Lorenzo","Andrés","86709403","lordandrees@gmail.com")
    print("Añadiendo Lorenzo2")
    Libreta.add(lorenzo2)
    Libreta.print_book(Libreta.root)
