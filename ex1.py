class Node():
    def __init__(self, val, left, right):
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
        self.__right = noeud

    def setLeft(self,noeud):
        self.__left = noeud

    def __str__(self):
        return str(self.getVal())

#test programme

#noeud = Node(8,5,4)
#print(noeud)
