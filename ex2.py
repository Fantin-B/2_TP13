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

        #if self.isRoot(node)==True:
        #    tailleNoeud += 1

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

    def prefixe(self,node):
        if node != None:
            print(node.getVal())
            self.prefixe(node.getLeft())
            self.prefixe(node.getRight())


    def infixe(self,node):
        if node!=None:
            self.infixe(node.getLeft())
            print(node.getVal())
            self.infixe(node.getRight())

    def postfixe(self,node):
        if node != None:
            self.postfixe(node.getLeft())
            self.postfixe(node.getRight())
            print(node.getVal())




#            #ici, node redeviens la racine de norte arbre du début
#            if (node.getRight()!=None and node.getLeft()!=None):
#                if (node.getRight().getVal()==val or node.getLeft().getVal()==val):
#                    self.ancestors(node,node.getVal())
#                    print(1)
#                elif (node.getRight().getVal()!=val or node.getLeft().getVal()!=val):
#                    self.ancestors(node, val)
#                    self.ancestors(node, val)
