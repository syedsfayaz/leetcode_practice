
#
# def square(x):
#     return x * x
#
# def cube(x):
#     return x * x * x
#
# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result
#
# squares = my_map(cube, [1,2,3,4,5])
#
# print(squares)

# def logger(msg):
#
#     def log_message():
#         print('Log:', msg)
#     return log_message
#
#
# log_hi = logger('HI!')
# log_hi()

# def html_tag(tag):
#
#     def wrap_text(msg):
#         print('<{0}>{1}</{0}>'.format(tag,msg))
#     return wrap_text
#
# print_h1 = html_tag('h1')
# print(print_h1)
#
# #print_h1('Test HeadLine')



# import random, xrange
# a = [random.randrange(1, 1000) for _ in xrange(100000000000000000000000)]
# print(a)







# class Myiter():
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         current = self.start
#         self.start += 1
#         return current

# result = Myiter(1, 10)
# # for n in result:
# #     print(n)
# print(result.__next__())
# print(result.__next__())

# def my_range(start, end):
#     current = start
#     while current <= end:
#         yield current
#         current += 1
#
# result = my_range(1, 10)
#
# print(next(result))
# print(result.__next__())
# print(result.__next__())

# stg = 'lower'
# print(stg.lower())
# print(stg.upper())
# print(stg.capitalize())
# print("".join(reversed(stg)))

# j = []
# for i in stg:
#     j = [i] + j
#
# print ("".join(j))
# def pyfunc(r):
#     for x in range(r):
#         print(' '*(r-x-1)+'*'*(2*x+1))
# pyfunc(2)
##0,1,1,2,3,5..



# class Fibonacci:
#
#     def __init__(self):
#         self.list = [0, 1]
#
#     def get_Fiboseries(self, length):
#         self.length = length
#         i = 2
#         while i < self.length:
#             next = self.list[-1] + self.list[-2]
#             self.list.append(next)
#             i += 1
#         return self.list
#
#     def get_prime(self, length):
#
#
# Fibo = Fibonacci()
#
# print(Fibo.get_Fiboseries(9))

# def find_capital():
with open("data.txt", 'r') as f:
     text = f.read()
     count = 0
     # for i in text:
     #     if i.isupper():
     #         count += 1
     return count

# print(find_capital())













