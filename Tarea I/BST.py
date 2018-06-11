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
    def __add(self,contact,root):
        if contact.name < root.name:
            if root.left is None:
                root.left = contact
                (root.left).parent = root
            else:
                self.__add(contact,root.left)
        elif contact.name > root.name:
            if root.right is None:
                root.right = contact
                (root.right).parent = root
            else:
                self.__add(contact,root.right)
        elif contact.name == root.name:
            if contact.last_name < root.last_name:
                if root.left is None:
                    root.left = contact
                    (root.left).parent = root
                else:
                    self.__add(contact,root.left)
            elif contact.last_name > root.last_name:
                if root.right is None:
                    root.right = contact
                    (root.right).parent = root
                else:
                    self.__add(contact,root.right)
    def add(self,contact):
        if self.empty():
            self.root = contact
        else:
            self.__add(contact,self.root)
        self.heigth += 1
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
    def delete_contact(self,contact):
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        def number_children(n):
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children
        if contact == self.root:
            successor = min_value_node(contact.right)
            contact.name = successor.name
            contact.last_name = successor.last_name
            contact.full_name = successor.full_name
            contact.phone = successor.phone
            contact.email = successor.email
            self.delete_contact(successor)
            return
        node_parent = contact.parent
        node_children = number_children(contact)
        if node_children == 0:
            if node_parent.left == contact:
                node_parent.left = None
            else:
                node_parent.right = None
        if node_children == 1:
            if contact.left != None:
                child = contact.left
            else:
                child = contact.right
            if node_parent.left == contact:
                node_parent.left = child
            else:
                node_parent.right = child
            child.parent = node_parent
        if node_children == 2:
            successor = min_value_node(contact.right)
            contact.name = successor.name
            contact.last_name = successor.last_name
            contact.full_name = successor.full_name
            contact.phone = successor.phone
            contact.email = successor.email
            self.delete_contact(successor)
    def delete_name(self,n,root,priority):
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        self.heigth -= 1
        return self.delete_contact(self.search_name(n,root)[priority-1])
    def delete_last_name(self,ln,root,priority): #Implementar
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        self.heigth -= 1
        return self.delete_contact(self.search_last_name(ln,root)[priority-1])
    def delete_phone(self,ph,root,priority): #Implementar
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        self.heigth -= 1
        return self.delete_contact(self.search_phone(ph,root)[priority-1])
    def delete_email(self,e,root,priority): #Implementar
        if self.empty():
            print("Libreta de contactos vacía.")
            return
        self.heigth -= 1
        return self.delete_contact(self.search_email(e,root)[priority-1])
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