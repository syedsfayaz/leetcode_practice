##### Lists Manipulation

my_list = [1, 2, 3]

#my_list.insert(3, 4)
#my_list.append([4,5])
#my_list.extend([4, 5])
#my_list = [4, 5] + my_list
# my_list.extend([3, 4])
# print(my_list)

#del my_list[2]  ## Deletes element from index 2
#my_list.remove(1)  ### Removes element mentioned from my_list
#my_list.pop(0)  ## pops element at index
#my_list.pop()
#my_list.clear()  Clears the entire list

#print(my_list)


#my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
# # #a = my_dict.pop('Second') #pop element
# #
# # # print('Dictionary:', my_dict)
# # b = my_dict.popitem() #pop the key-value pair
# # #print('Key, value pair:', b)
# # # print('Dictionary', my_dict)
# # # # my_dict.clear() #empty dictionary
# # # # print('n', my_dict)


# my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
# # print(my_dict.keys()) #get keys
# # print(my_dict.values()) #get values
# # print(my_dict.items()) #get key-value pairs
# # print(my_dict.get('First'))
# for item, value in my_dict.items():
#     print(f'{item}:{value}')


# my_tuple = (1, 2, 3)
# my_tuple = my_tuple + (4, 5, 6) #add elements
# print(my_tuple)

# my_set = {1, 2, 3, 4}
# my_set_2 = {3, 4, 5, 6}
# print(my_set.union(my_set_2), '----------', my_set | my_set_2)
# print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
# print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
# print(my_set_2.difference(my_set), '----------', my_set - my_set_2)
# print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
# # my_set.clear()
# # print(my_set)

### Stack Datastructure using dequeue  LIFO

from collections import deque
# stack = deque()
# stack.append('1')
# stack.append('2')
# stack.append('3')
# print(stack.pop())

# class stack():
#     def __init__(self):
#         self.stack = list()
#     def push(self, item):
#         self.stack.append(item)
#     def pop(self):
#         if len(self.stack) > 0:
#             return self.stack.pop()
#         else:
#             return("stack is empty")
#     def peek(self):
#         if len(self.stack) > 0:
#             return self.stack[-1]
#     def __str__(self):
#         return str(self.stack)

# class stack:
#     def __init__(self):
#         self.container = deque()
#
#     def push(self, val):
#         self.container.append(val)
#
#     def pop(self):
#         return self.container.pop()
#
#     def peek(self):
#         return self.container[-1]
#
#     def is_empty(self):
#         return len(self.container) == 0
#
#     def size(self):
#         return len(self.container)
# s = stack()
# s.push('1')
# s.push('2')
# s.push('3')
# print(s.peek())
# print(s.pop())
# print(s.peek())
# print(s.__str__())

# string = "We will conquere COVID-19"
# length = len(string)
# for i in string:
#    s.push(i)
#
# print(s.size(), s)
#
#
# result = ""
# while s.size() != 0:
#     result += s.pop()
#
# print(result)

# def is_balanced(item):
#     s = stack()
#     paranthesis = {'{':'}','(':')','[':']'}
#     for ch in item:
#         if ch in paranthesis:
#             s.push(paranthesis[ch])
#         if ch in paranthesis.values() and ch == s.peek():
#             s.pop()
#     return s.size() == 0
#
#
# print(is_balanced("({a+b})"))  #   --> True


#### Queue == FIFO

# from collections import deque
#
# q = deque()
#
# q.appendleft(1)
# q.appendleft(2)
# q.appendleft(3)
# q.appendleft(4)
# print(q)
# q.pop()
# print(q)


diction = {"abc": 1, "nuws": 5, "udciw": 7, "yec": 3, "nus": 4}
listed = [1, 3, 4, 56, 3, 2, 5, 7]
#result = sorted(diction.items(), key=lambda x:x[1])
result = sorted(listed, reverse=True)
print(result)












