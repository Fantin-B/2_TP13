from ex1 import *

class BinaryTree():
    def __init__(self,root):
        self.__root = root

    def getRoot(self):
        return self.__root

    def isRoot(self, node):
        if node == self.__root:
            return True
        else:
            return False


    def height(self,node):

        if node == None or (node.getLeft()==None and node.getRight()==None) :
            return 1

        hauteurNoeuddroite = 1+ self.height(node.getRight())
        hauteurNoeudgauche = 1+ self.height(node.getLeft())
        hauteurNoeud = max(hauteurNoeuddroite,hauteurNoeudgauche)

        return hauteurNoeud



    def size(self,node):

        if node == None:
            return -1
        if node.getLeft()==None and node.getRight()==None :
            return 0

        tailleNoeuddroite = 1+ self.size(node.getRight())
        tailleNoeudgauche = 1+ self.size(node.getLeft())
        tailleNoeud = tailleNoeuddroite + tailleNoeudgauche
        print("taille noeud",node.getVal(),":",tailleNoeud)
        return tailleNoeud









#test programme
root = Node(12,None,None)
arbre = BinaryTree(root)

noeud5 = Node(5,None,None)
root.setLeft(noeud5)

noeud6 = Node(6,None,None)
noeud5.setRight(noeud6)

noeud4 = Node(4,None,None)
noeud5.setLeft(noeud4)

noeud3 = Node(3,None,None)
noeud4.setLeft(noeud3)

noeud17 = Node(17,None,None)
root.setRight(noeud17)

noeud19 = Node(19,None,None)
noeud17.setRight(noeud19)

noeud21 = Node(21,None,None)
noeud19.setRight(noeud21)

noeud18 = Node(18,None,None)
noeud19.setLeft(noeud18)

#print(arbre.height(noeud5))
print(arbre.size(root))














def affichageNoeud(noeud):
    print("Valeur :",noeud.getVal())
    if noeud.getRight() != None:
        print("Noeud droit :",noeud.getRight().getVal())
    else :
        print("Noeud droit :",None)
    if noeud.getLeft() != None:
        print("Noeud gauche :",noeud.getLeft().getVal())
    else :
        print("Noeud gauche :",None)
#affichageNoeud(root)
