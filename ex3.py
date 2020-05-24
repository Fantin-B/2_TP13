from ex1 import *
from ex2 import *

class BinarySearchTree(BinaryTree):
    def __init__(self,root):
        BinaryTree.__init__(self,root)
        self.__root = root

    def contains(self,node,value):
        if node!=None:
            if node.getVal() == value :
                return True
            gauche = self.contains(node.getLeft(),value)
            droite = self.contains(node.getRight(),value)
            if gauche==True or droite==True:
                return True

    def findMin(self,node):
        if node!=None:
            min = 10000
            if node.getVal() < min :
                min = node.getVal()

            gauche = self.findMin(node.getLeft())
            if gauche < min :
                min = gauche

            droite = self.findMin(node.getRight())
            if droite < min :
                min = droite

            return min


#test programme
root = Node(4,None,None)
arbre = BinarySearchTree(root)

noeud2 = Node(2,None,None)
root.setLeft(noeud2)

noeud3 = Node(3,None,None)
noeud2.setRight(noeud3)

noeud0 = Node(0,None,None)
noeud2.setLeft(noeud0)

noeud1 = Node(1,None,None)
noeud0.setRight(noeud1)

noeud20 = Node(20,None,None)
root.setRight(noeud20)

noeud12 = Node(12,None,None)
noeud20.setLeft(noeud12)

noeud7 = Node(7,None,None)
noeud12.setLeft(noeud7)

noeud6 = Node(6,None,None)
noeud7.setLeft(noeud6)

noeud15 = Node(15,None,None)
noeud12.setRight(noeud15)

noeud13 = Node(13,None,None)
noeud15.setLeft(noeud13)

noeud14 = Node(14,None,None)
noeud13.setRight(noeud14)

exNoeud = root
#arbre.infixe(exNoeud)
#print(arbre.contains(exNoeud,12))
print(arbre.findMin(exNoeud))
