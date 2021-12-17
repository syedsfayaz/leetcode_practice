import re

# text = """
# abcdefghijklmnopqrst
# ABCDEFGHIJKLMNOPQRST
#
# 1234567890
#
# """
# # MetaCharacters (Need to be escaped):
# # . ^ $ +
#
# coryms.com
#
# sentence = 'Start a sentence and then bring it to an end'
#
# pattern = re.compile(r'\.')
#
# matches = pattern.finditer(text)
#
# for match in matches:
#     print(match)

IPv4 = '0.255.255.255'
IPv6 = 'FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF'
#pattern = re.compile(r'^(25[0-5]|24[0-9]|[0-1]?[0-9]?[0-9])\.(25[0-5]|24[0-9]|[0-1]?[0-9]?[0-9])\.(25[0-5]|24[0-9]|[0-1]?[0-9]?[0-9])\.(25[0-5]|24[0-9]|[0-1]?[0-9]?[0-9])$')
pattern = re.compile(r'^([A-Za-z0-9]{1,4})\:([A-Za-z0-9]{1,4})\:([A-Za-z0-9]{1,4})\:([A-Za-z0-9]{1,4})\:([A-Za-z0-9]{1,4})\:([A-Za-z0-9]{1,4})\:([A-Za-z0-9]{1,4})\:([A-Za-z0-9]{1,4})$')
result = (pattern.fullmatch(IPv6))
if result:
    print(True)
else:
    print(False)