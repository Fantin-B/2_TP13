from ex2 import *

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
#print("Est-ce une racine ? :",arbre.isRoot(exNoeud))
#print("taille noeud",exNoeud.getVal(),":",arbre.size(exNoeud))
#arbre.printValues(exNoeud)
#print("somme des valeurs de l'arbre :",arbre.sumValues(exNoeud))
#print("nombre de feuille :",arbre.numberLeaves(exNoeud))
#print("Nombre de noeud interne :",arbre.numberInternalNodes(exNoeud))
#print("hauteur noeud",exNoeud.getVal(),":",arbre.height(exNoeud))
#print(arbre.belongs(exNoeud,3))
#arbre.descendants(exNoeud,19)
#arbre.prefixe(exNoeud)
#arbre.infixe(exNoeud)
#arbre.postfixe(exNoeud)


arbre.ancestors2(exNoeud,3)











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
