
'''
Linked Lists
'''
class node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        total = 0
        cur = self.head
        print(self.head.data)
        print(self.head.next.data)
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    def display(self):
        elements=[]
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)

        #elements.append(cur_node.data)
        print(elements)

    def get(self,index):
        if index >= self.length():
            return None
        cur = self.head
        cur_ind = 0
        while cur_ind <= index:
            if cur_ind == index:
                return cur.data
            cur = cur.next
            cur_ind += 1
## 1,2,3,4,5
    def erase(self, index):
        if index >= self.length():
            return None
        cur = self.head
        cur_ind = 0
        while cur_ind <= index:
            last_node = cur
            cur = cur.next
            if cur_ind == index:
                last_node.next = cur.next
                return
            cur_ind += 1


my_list = linked_list()

my_list.append(1)
my_list.append(2)

my_list.append(3)
my_list.append(7)
my_list.append(5)
my_list.append(6)
print(my_list.length())
# print(my_list.display())
# my_list.erase(3)
# print(my_list.display())
#print("%d",my_list.get(4))


#my_list.display()
#
# '''
# Dictionaries vs list comparison
# '''
# class_names = ["jack", "bob","mary","jeff","ann","pierre","martha","clause","pablo","susan","gustav"]
#
#
# def create_dataset():
#     import random
#     num_entries = 50000000000000000000000000
#     f = open('data.txt',"w")
#     for i in range(num_entries):
#         current = random.choice(class_names)
#         f.write(current+"\n")
#     f.close()
#
# def read_dataset_list():
#     class_counts = []
#     for c in class_names:
#         class_counts.append(0)
#     with open("data.txt","r") as f:
#         for line in f:
#             line = line.strip()
#             if line != "":
#                 class_counts[class_names.index(line)] += 1
#     print (class_counts)
#
# def read_dataset_dict():
#     class_counts = {}
#     for c in class_names:
#         class_counts[c] = 0
#     with open("data.txt","r") as f:
#         for line in f:
#             line = line.strip()
#             if line != "":
#                 class_counts[line] += 1
#     print(class_counts)
#
# import time
# create_dataset()
# t0 = time.time()
# read_dataset_list()
# t1 = time.time()
# print(t1-t0)
# t0=time.time()
# read_dataset_dict()
# t1=time.time()
# print(t1-t0)










