
def read_file(filename):
    hostsinfile = {}
    with open(filename) as file:
        for line in file:
            linelist = line.split()
            if linelist[0] in hostsinfile:
                hostsinfile[linelist[0]] += 1
            else:
                hostsinfile[linelist[0]] = 1


    with open("records_"+filename, "w") as file:
        for host in hostsinfile:
            file.write(host+" "+str(hostsinfile[host])+"\n")

file_name = "file_name.txt"
read_file(file_name)