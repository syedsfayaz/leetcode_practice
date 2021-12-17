
url = "https://api.github.com/orgs/octo-org/repos"
import  requests
import json
def get_org(url):
    result = requests.get(url).json()
    return result
    # pretty = json.dumps(result, indent=2)
    # return pretty

def get_repolist(url):
    result = get_org(url)
    #print(result)
    for items in result:
       item = items["full_name"].strip("octo-org/")
       print(item)


get_repolist(url)

#get the results from github org and print the repo names.