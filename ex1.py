class Node():
    def __init__(self, val, right, left):
        self.__val = val
        self.__right = right
        self.__left = left

    def getVal(self):
        return self.__val

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setRight(self,noeud):
        self.__right.append(noeud)

    def setLeft(self,noeud):
        self.__left.append(noeud)


#test programme

#noeud1 = Node(12,17,5)
#noeud2 = Node(5,6,4)
#noeud3 = Node(4,None,3)
#noeud4 = Node(17,19,None)
#noeud5 = Node(19,21,18)
