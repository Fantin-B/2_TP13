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

        return tailleNoeud



    def printValues(self, node):

        if node!=None and (node.getRight()==None and node.getLeft()==None) :
            print("valeur de noeud",node.getVal()," :",node.getVal())

        elif node!=None :
            print("valeur de noeud",node.getVal()," :",node.getVal())
            self.printValues(node.getRight())
            self.printValues(node.getLeft())



    def sumValues(self, node):

        if node!=None and (node.getRight()==None and node.getLeft()==None) :
            return node.getVal()

        elif node!=None :
            brancheDroite = self.sumValues(node.getRight())
            brancheGauche = self.sumValues(node.getLeft())
            if brancheDroite==None:
                brancheDroite=0
            if brancheGauche==None:
                brancheGauche=0
            total = node.getVal() + brancheDroite + brancheGauche
            return total


    def numberLeaves(self, node):

        if node!=None and (node.getRight()==None and node.getLeft()==None) :
            return 1

        elif node!=None :
            brancheDroite = self.numberLeaves(node.getRight())
            brancheGauche = self.numberLeaves(node.getLeft())
            if brancheGauche == None:
                brancheGauche = 0
            if brancheDroite == None:
                brancheDroite = 0
            return  brancheGauche + brancheDroite


    def numberInternalNodes(self, node):
        return self.size(node) +1 - self.numberLeaves(node)



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

exNoeud = root
#print("hauteur noeud",exNoeud.getVal(),":",arbre.height(exNoeud))
#print("taille noeud",exNoeud.getVal(),":",arbre.size(exNoeud))
arbre.printValues(exNoeud)
#print("nombre de feuille :",arbre.numberLeaves(exNoeud))
#print("Nombre de noeud interne :",arbre.numberInternalNodes(exNoeud))
print("somme des valeurs de l'arbre :",arbre.sumValues(exNoeud))










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
