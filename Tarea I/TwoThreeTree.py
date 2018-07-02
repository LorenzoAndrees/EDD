import unicodedata

def noacc(word):
    s = ''.join((c for c in unicodedata.normalize('NFD',word) if unicodedata.category(c) != 'Mn'))
    return s

class Contact:
    def __init__(self,n,ln,ph,e):
        self.name = (noacc(n)).title()
        self.last_name = (noacc(ln)).title()
        self.full_name = self.name + " " + self.last_name
        self.phone = ph
        self.email = e
    def __str__(self):
        return str(self.full_name + " ~~~~ " + self.phone + " ~~~~ " + self.email)
class Node:
    def __init__(self,contact):
        self.data = [contact]
        self.parent = None
        self.child = []
        self.last_name = contact.last_name
    def __str__(self):
        if self.parent:
            return str(self.parent.data) + " : " + str(self.data)
        return "Root: " + str(self.data)
    def bubblesort(self,list):
        for k in range(len(list)-1,0,-1):
            for i in range(k):
                if list[i].last_name>list[i+1].last_name:
                    list[i],list[i+1] = list[i+1], list[i]
    def _is_leaf(self):
        return len(self.child) == 0
    def _add(self,new_node):
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        self.bubblesort(self.data)
        self.child.extend(new_node.child)
        if len(self.child) > 1:
        	self.bubblesort(self.child)
        if len(self.data) > 2:
            self._split()
    def _insert(self, new_node):
        if self._is_leaf(): 
            self._add(new_node)
        elif new_node.data[0].last_name > self.data[-1].last_name:
            self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0].last_name < self.data[i].last_name:
                    self.child[i]._insert(new_node)
                    break
    def _split(self):
        left_child = Node(self.data[0])
        right_child = Node(self.data[2])
        if self.child:
        	self.child[0].parent = left_child
        	self.child[1].parent = left_child
        	self.child[2].parent = right_child
        	self.child[3].parent = right_child
        	left_child.child = [self.child[0], self.child[1]]
        	right_child.child = [self.child[2], self.child[3]]

        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]
        if self.parent:
        	if self in self.parent.child:
        		self.parent.child.remove(self)
        	self.parent._add(self)
        else:
        	left_child.parent = self
        	right_child.parent = self
    def _find(self,contact,contacts = []):
        if contact in self.data:
            contacts.append(contact)
        elif self._is_leaf():
            return 0
        elif contact.last_name > self.data[-1].last_name:
            contacts.extend(self.child[-1]._find(contact,contacts))
        else:
            for i in range(len(self.data)):
                if contact.last_name < self.data[i].last_name:
                    contacts.extend(self.child[i]._find(contact,contacts))
        return contacts
    def _remove(self, item):
    	pass	
    def _preorder(self):
        for child in self.child:
            print(child.data)
            child._preorder()
class Book:
    def __init__(self):
        self.root = None
    def empty(self):
        return self.root == None
    def insert(self,contact):
        print("Agregando a",contact.full_name,"...")
        if self.empty():
            self.root = Node(contact)
        else:
            self.root._insert(Node(contact)) 
            while self.root.parent:
                self.root = self.root.parent 
        return True
    def remove(self, item):
        self.root.remove(item)
    def search(self,item):
        return self.root._find(item)
    def print_preorder(self):
        self.root._preorder()