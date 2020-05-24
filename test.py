#code size() du prof
def size(self, node):
    if node is None:
        return 0
    else:
        return self.size(node.getLeft()) + 1 + self.size(node.getRight())
##############
def printValues(self, node):
    if node is None:
        return ""
    else:
        return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())
