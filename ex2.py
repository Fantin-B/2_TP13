from ex1 import *

class BinaryTree():
    def __init__(self,root):
        self.__root = root

    def getRoot(self):
        return self.__root


#test programme
root = BinaryTree(12)
noeud1 = Node(root.getRoot(),17,5)
noeud2 = Node(noeud1.getRight(),6,4)
noeud3 = Node(noeud2.getRight(),None,None)
noeud4 = Node(noeud2.getLeft(),None,4)
noeud5 = Node(noeud4.getLeft(),None,3)
noeud6 = Node(noeud1.getLeft(),19,None)
noeud7 = Node(noeud6.getLeft(),21,18)
noeud8 = Node(noeud7.getRight(),None,None)
noeud9 = Node(noeud7.getLeft(),None,None)
