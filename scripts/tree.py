class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        elif self.value < data:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        elif self.value < data:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

    def getsize(self):
        if self.leftChild and self.rightChild:
            return 1 + self.leftChild.getsize() + self.rightChild.getsize()
        elif self.leftChild:
            return 1 + self.leftChild.getsize()
        elif self.rightChild:
            return 1 + self.rightChild.getsize()
        else:
            return 1

    def getheight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getheight(), self.rightChild.getheight())
        elif self.leftChild:
            return 1 + self.leftChild.getheight()
        elif self.rightChild:
            return 1 + self.rightChild.getheight()
        else:
            return 1




class Tree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("postorder")
        self.root.postorder()

    def inorder(self):
        print("inorder")
        self.root.inorder()

    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # data is in root node
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.value = delNode.value
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None

            return True

        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        # case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

            node.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.leftChild = None
                else:
                    delNodeParent.rightChild = None

    def getsize(self):
        if self.root:
            return self.root.getsize()
        else:
            return 0

    def getheight(self):
        if self.root:
            return self.root.getheight()
        else:
            return 0


if __name__ == '__main__':
    bst = Tree()
    listing = [10, 11, 12, 3, 12, 15, 2, 14, 94, 23, 45, 65, 0]
    for i in listing:
        bst.insert(i)
    #print(bst.insert(15))
    # bst.preorder()
    # bst.postorder()
    # bst.inorder()
    # print(bst.getheight())
    # print(bst.getsize())
    # print(bst.remove(94))
    # print(bst.remove(0))
    # print(bst.getheight())
    # print(bst.getsize())
    #bst.preorder()
    #print(bst.find(2))