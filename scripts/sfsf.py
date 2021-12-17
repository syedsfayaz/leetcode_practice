# def alternatingSums(a):
#     for x in a[::2]:
#         print(x)
import itertools
def alternatingSums(a):
    for item in itertools.islice(a, 1, None, 2):
        print(item)

a = [50, 60, 60, 45, 70]
alternatingSums(a)

logfile_path = "/root/devops/server.log"
with open(logfile_path, "r") as log:
    lines = log.readlines()
    list = []
    for line in lines:
        list.append(line)
        # print(list)

    list1 = []
    size = []
    for i in list:
        i1 = str(i)
        # list1.append(i1[1])
        i2 = i1.split(" ")[3:][0]
        i3 = i1.split(" ")[3:][-2]
        list1.append(i2)
        size.append(i3)
        i1 = ""

    commonfile = set(list1)

    for image in commonfile:
        for i in list1:
            if

    print(list1, size)
