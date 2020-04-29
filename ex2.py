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



    def size(self,node):

        if node == None:
            return -1
        if node.getLeft()==None and node.getRight()==None :
            return 0

        tailleNoeuddroite = 1+ self.size(node.getRight())
        tailleNoeudgauche = 1+ self.size(node.getLeft())
        tailleNoeud = tailleNoeuddroite + tailleNoeudgauche

        if self.isRoot(node)==True:
            tailleNoeud += 1

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
        return self.size(node) - self.numberLeaves(node)



    def height(self,node):

        if node == None or (node.getLeft()==None and node.getRight()==None) :
            return 0

        hauteurNoeuddroite = 1+ self.height(node.getRight())
        hauteurNoeudgauche = 1+ self.height(node.getLeft())
        hauteurNoeud = max(hauteurNoeuddroite,hauteurNoeudgauche)

        return hauteurNoeud



    def belongs(self,node,val):

        if node!=None and node.getVal()== val :
            return True

        elif node!=None :
            brancheDroite = self.belongs(node.getRight(),val)
            brancheGauche = self.belongs(node.getLeft(),val)
            if brancheDroite==True or brancheGauche==True:
                return True
            else:
                return False



    def descendants(self,node,val):

        if node!=None and node.getVal() == val:
            #print("Descendant :",node.getVal())
            if node.getRight()!=None:
                print("Descendant :",node.getRight().getVal())
                self.descendants(node,node.getRight().getVal())
            if node.getLeft()!=None:
                print("Descendant :",node.getLeft().getVal())
                self.descendants(node,node.getLeft().getVal())

        elif node!=None and node.getVal() != val:
            self.descendants(node.getRight(), val)
            self.descendants(node.getLeft(), val)


    def ancestors(self,node,val):

        if node!=None and (node.getLeft()!=None or node.getRight()!=None):

            if node.getRight().getVal() == val  or node.getLeft().getVal() == val:
                print("ancêtre :", node.getVal())
                self.ancestors(self.__root,node.getVal())

            elif node.getVal() != val:
                self.ancestors(node.getRight(), val)
                self.ancestors(node.getLeft(), val)



    def ancestors2(self,node,val):
        if node!=None and (node.getLeft()!=None or node.getRight()!=None):

            if node.getRight() != None:
                print(node.getRight().getVal())

            if node.getLeft()!=None:
                print(node.getLeft().getVal())

            elif node.getVal() != val:
                self.ancestors2(node.getRight(), val)
                self.ancestors2(node.getLeft(), val)



#            #ici, node redeviens la racine de norte arbre du début
#            if (node.getRight()!=None and node.getLeft()!=None):
#                if (node.getRight().getVal()==val or node.getLeft().getVal()==val):
#                    self.ancestors(node,node.getVal())
#                    print(1)
#                elif (node.getRight().getVal()!=val or node.getLeft().getVal()!=val):
#                    self.ancestors(node, val)
#                    self.ancestors(node, val)








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

#noeud1 = Node(1,None,None)
#noeud21.setRight(noeud1)
#
#noeud2 = Node(2,None,None)
#noeud6.setRight(noeud2)
#
#noeud45 = Node(45,None,None)
#noeud2.setRight(noeud45)
#
#noeud46 = Node(46,None,None)
#noeud45.setRight(noeud46)


exNoeud = root
#print("hauteur noeud",exNoeud.getVal(),":",arbre.height(exNoeud))
#print("taille noeud",exNoeud.getVal(),":",arbre.size(exNoeud))
#arbre.printValues(exNoeud)
#print("nombre de feuille :",arbre.numberLeaves(exNoeud))
#print("Nombre de noeud interne :",arbre.numberInternalNodes(exNoeud))
#print("somme des valeurs de l'arbre :",arbre.sumValues(exNoeud))
#print(arbre.belongs(exNoeud,17))
#arbre.descendants(exNoeud,4)
arbre.ancestors2(exNoeud,17)





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
