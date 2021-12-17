# import ipaddress
#
# def is_ipv4(string):
#         try:
#             ipaddress.IPv4Network(string)
#             return True
#         except ValueError:
#             return False
#
# def is_ipv6(string):
#         try:
#             ipaddress.IPv6Network(string)
#             return True
#         except ValueError:
#             return False
#
# def addresses_verify(addresses):
#     for i in addresses:
#         if is_ipv4(i):
#             print('IPv4')
#         elif is_ipv6(i):
#             print('IPv6')
#         else:
#             print('Neither')
#
# if __name__ == '__main__':
#     address_count = int(input())
#     addresses = (input() for _ in range(address_count))
#     addresses_verify(addresses)

from datetime import datetime
file = "rooms.txt"
with open(file, 'r') as f:
    example = f.read().splitlines()

# for i in example:
#     for j in i[2:]:

print(example)
#test = datetime.strptime(example[3], "%H:%M")


print(test)