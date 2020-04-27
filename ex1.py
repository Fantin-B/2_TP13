class Node():
    def __init__(self, val, left, right):
        self.__val = val
        self.__right = right
        self.__left = left

    def getVal(self):
        if self.__val is None:
            return None
        else :
            return self.__val

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setRight(self,noeud):
        self.__right = noeud

    def setLeft(self,noeud):
        self.__left = noeud


#test programme

#noeud = Node(None,None,None)
#print(noeud.getVal())
#print(noeud.getLeft())
#print(noeud.getRight())
