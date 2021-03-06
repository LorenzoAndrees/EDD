import unicodedata

def noacc(word):
    s = ''.join((c for c in unicodedata.normalize('NFD',word) if unicodedata.category(c) != 'Mn'))
    return s

class Contact:
    def __init__(self,n,ln,ph,e):
        self.left = None
        self.right = None
        self.parent = None
        self.name = (noacc(n)).title()
        self.last_name = (noacc(ln)).title()
        self.full_name = self.name + " " + self.last_name
        self.phone = ph
        self.email = e
        self.height = 1
    def __str__(self):
        return str(self.full_name + " ~~~~ " + self.phone + " ~~~~ " + self.email)

class Book:
    def __init__(self):
        self.root = None
    def empty(self):
        return self.root == None
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def dobalance(self,balance,contact,root):
        if balance > 1 and contact.name < (root.left).name:
            return self.rightRotate(root)
        if balance < -1 and contact.name > (root.right).name:
            return self.leftRotate(root)
        if balance > 1 and contact.name > (root.left).name:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and contact.name < (root.right).name:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    def add(self, root, contact):
        if self.root is None:
            self.root = contact
            return
        if not root:
            return contact
        elif contact.last_name < root.last_name:
            root.left = self.add(root.left,contact)
        else:
            root.right = self.add(root.right,contact)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and contact.last_name < root.left.last_name:
            return self.rightRotate(root)
        if balance < -1 and contact.last_name > root.right.last_name:
            return self.leftRotate(root)
        if balance > 1 and contact.last_name > root.left.last_name:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and contact.last_name < root.right.last_name:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def search_name(self,n,root,contacts=[]):
        n= (noacc(n)).title()
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
        ln= (noacc(ln)).title()
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
    def delete_contact(self,contact,root):
        if not root:
            return root
        elif contact.last_name < root.last_name:
            root.left = self.delete_contact(contact,root.left)
        elif contact.last_name > root.last_name:
            root.right = self.delete_contact(contact,root.right)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.name = temp.name
            root.last_name = last_temp.name
            root.full_name = full_temp.name
            root.phone = temp.phone
            root.email = temp.email
            root.right = self.delete_contact(temp,root.right)
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def delete_name(self,n,root,priority):
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        return self.delete_contact(self.search_name(n,self.root)[priority-1])
    def delete_last_name(self,ln,root,priority): #Implementar
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        return self.delete_contact(self.search_last_name(ln,self.root)[priority-1])
    def delete_phone(self,ph,root,priority): #Implementar
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        return self.delete_contact(self.search_phone(ph,self.root)[priority-1])
    def delete_email(self,e,root,priority): #Implementar
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        return self.delete_contact(self.search_email(e,self.root)[priority-1])
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

