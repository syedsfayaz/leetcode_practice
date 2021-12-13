##Manager
####Return duplicates letters and count

result = {}
def duplicate_items(input):
    unique = set(input)
    print(unique)
    for items in input:
        if items not in result:
            result[items] = 1
        else:
            result[items] += 1
    # return(result)
    for item, value in result.items():
        if value != 1:
            print(item + ":" + str(value))


duplicate_items('ProgrammingProgramming')


##Lead Engineer
#
##Reverse a number from 3 nuimbers

input = ["A1", A2, A3, B1, B2, B3]
Output = [A3, A2, A1, B3, B2, B1]


# connect to https://github.apple.com/dev
## {"user":"abc@apple.com", "commits":"ticket://99999 bug fix"}
# 1. Commits does not start with ticket -> send email to user,
# 2. For all other commits, send email to a group (dev@apple.com) - list of commits.
# Every one hour - "for the last hour"



###[{"user":"abc@apple.com", "commits":"ticket://99999 bug fix"}, {"user":"abc@apple.com", "commits":"_://99999 bug fix"}]
# 1,2,3,4,5, 6
# Email 1,6 to abc, Email 5 to def, Email "2,3,4" to dev.
#

def parse_commits(input):
    bad_commit = {}
    good_commit = {}
    # count = 0
    for items in input:
        if str(items["commits"][0:6]) != "ticket":
            if items["user"] not in bad_commit:
                bad_commit[items["user"]] = items["commit"]
            else:
                bad_commit[items["user"]] += items["commit"]

        else:
            if items["user"] not in good_commit:
                good_commit["dev@apple.com"] = items["commit"]
            else:
                good_commit["dev@apple.com"] += items["commit"]

    for user, commit in bad_commit.items():
        print("send email to user")
    print("send email to dev@apple.com")


print(parse_commits(

    #

 #
 # Your previous Java content is preserved below:
 #
 #
 #
 # INPUT='162.167.23.100'
 #
 # RANGE='162.167.000.000/16' # min = 162.167.0.0, max = 162.167.255.255
RANGE='162.167.23.100/16'
ip_split = RANGE.split("/")
ip = ip_split[0].split(".")
min_ip = ip[:2]
# print(min_ip)

def find_ipinrange(input):
    temp = input.split(".")
    i = 0
    while i < 2:
        if temp[i] != min_ip[i]:
            return "IP not in range"
        i += 1
    return "Ip is in range"
print(find_ipinrange('162.167.23.100'))