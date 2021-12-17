# def read_file(filename):
# #     host2req = {}
# #
# #     with open(filename) as file:
# #         for line in file:
# #             line_list = line.split()
# #             if line_list[0] in host2req:
# #                 host2req[line_list[0]] += 1
# #             else:
# #                 host2req[line_list[0]]  = 1
# #
# #     #file = open("records_"+filename, "w")
# #     with open("records_"+filename, "w") as f:
# #          for host in host2req:
# #              print(host + " " + str(host2req[host]))
# #              f.write(host+ " "+str(host2req[host])+ "\n")
# #     #    file.write(host+" "+str(host2req[host]), end="\n")
# #     #file.close()

def read_file(filename):
    sorted_dict= {}
    with open(filename, 'r') as f:
        for line in f:
            single_line = line.split()
            if single_line[0] in sorted_dict:
                sorted_dict[single_line[0]] += 1
            else:
                sorted_dict[single_line[0]] = 1
        print(sorted_dict)

    file_name = '{0}-{1}'.format('hostaccess', filename)
    with open (filename, 'w') as f:
         for key, value in sorted_dict.items():
             f.write('{0} {1}'.format(key,value))





file_name = "host_access_log_00.txt"
read_file(file_name)