class Tree:

    def __init__(self, val):
        self.value = val
        #print(self.value)
        self.leftChild = None
        self.rightChild = None


    def insert(self, val):
        if self.value == val:
            return False
        elif val > self.value:
            if self.rightChild:
               return self.rightChild.insert(val)
            else:
               self.rightChild = Tree(val)
               return True
        elif val < self.value:
            if self.leftChild:
                return self.leftChild.insert(val)
            else:
                self.leftChild = Tree(val)
                return True

    def find(self, val):
        if self.value == val:
            return True
        elif self.value > val:
            if self.leftChild:
               return self.leftChild.find(val)
            else:
                return False
        elif self.value < val:
            if self.rightChild:
                return self.rightChild.find(val)
            else:
                return False
        else:
            return False

    def inorder(self):
        elements = []
        if self.leftChild:
            elements += self.leftChild.inorder()
        if self.value:
            elements += [self.value]
            #print(str(self.value))
        if self.rightChild:
            elements += self.rightChild.inorder()
        return elements

    def preorder(self):
        elements = []
        if self.value:
            elements += [self.value]

        if self.leftChild:
            elements += self.leftChild.preorder()

            #print(str(self.value))
        if self.rightChild:
            elements += self.rightChild.preorder()
        return elements

    def postorder(self):
        elements = []
        if self.leftChild:
            elements += self.leftChild.postorder()

            #print(str(self.value))
        if self.rightChild:
            elements += self.rightChild.postorder()

        if self.value:
            elements += [self.value]
        return elements

    def find_max(self):
        if self.rightChild is None:
            return self.value
        else:
            return self.rightChild.find_max()

    def find_min(self):
        if self.leftChild is None:
            return self.value
        else:
            return self.leftChild.find_min()

    def calculate_sum(self):
        sum = 0
        if self.value:
            sum += self.value
        if self.rightChild:
            sum += self.rightChild.calculate_sum()
        if self.leftChild:
            sum += self.leftChild.calculate_sum()
        return sum

    # def delete(self, val):
    #     if val == self.value:
    #         if self.rightChild and self.leftChild:
                
    def delete(self, val):
        if val < self.value:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
        elif val > self.value:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
        else:
            if self.leftChild is None and self.rightChild is None:
                return None
            elif self.leftChild is None:
                return self.rightChild
            elif self.rightChild is None:
                return self.leftChild

            # min_val = self.rightChild.find_min()
            # self.value = min_val
            # self.rightChild = self.rightChild.delete(min_val)
            max_val = self.leftChild.find_max()
            self.value = max_val
            self.leftChild = self.leftChild.find_max(max_val)

        return self
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
        if self.rightChild and self.leftChild:
            return 1 + max(self.leftChild.getheight(), self.rightChild.getheight())
        elif self.leftChild:
            return 1 + self.leftChild.getheight()
        elif self.rightChild:
            return 1 + self.rightChild.getheight()
        else:
            return 1




# def build_tree(elements):
#     root = Tree(elements[0])
#     for i in range(1, len(elements)):
#         root.insert(elements[i])
#
#
# numbers = [1, 3, 4, 5, 6, 7, 8, 4, 3, 2, 2]
# numbers_tree = build_tree(numbers)

my_tree = Tree(1)
for i in [1, 3, 4, 5, 6, 7, 8, 4, 34, 2, 24]:
    my_tree.insert(i)
# countries = ["India", "China", "Usa", "Germany", "India", "Pakistan"]
# my_tree = Tree(countries[0])
# for i in range(1, len(countries)):
#     my_tree.insert(countries[i])

#print(my_tree.find("America"))
#print(my_tree.inorder())
# print(my_tree.preorder())
# print(my_tree.postorder())
# print(my_tree.find_max())
# print(my_tree.find_min())
# print(my_tree.calculate_sum())
#print(my_tree.delete(7))
#print(my_tree.inorder())
#print(my_tree.getsize())
print(my_tree.getheight())



