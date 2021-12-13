import ipaddress

addr = "121.18.19.20"
#addr = input()
#print(addr)

# if is_ipv4(addr) == True:
#     print('IPv4')



def get_ipv4_pattern(address):
    try:
        ipaddress.IPv4Network(address)
        return (True)
    except ValueError:
        return (False)


print(get_ipv4_pattern("121.18.19.20"))