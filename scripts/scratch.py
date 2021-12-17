def isIPv4Address(inputString):
    if len(inputString) == 12 and inputString.count(".") == 3:
        a = inputString.split('.')
        for i in a:
            if int(i) >= 0 and 255 >= int(i):
                continue
            else:
                print(False)
        print(False)
    else:
        print(False)

isIPv4Address("172.169.00.1")