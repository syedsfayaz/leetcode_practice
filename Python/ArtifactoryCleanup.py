import requests
import json
import re

repository = "https://artifactory.amerhonda.com/artifactory"
auth = ("fayaz sayyed", "AKCp8ihVmzmPpLoGP18VxbCd5S4GC5nwFMPrwaurj68s8uJNXUgedAGq2DhtWEEnQNYSBT2de")
headers = {'content-type': 'text/plain'}

''' Get a list of all Helm repositories in Artifactory'''
def get_repolist():
    url = repository + "/api/repositories"
    r = requests.get(url, auth=auth, headers=headers, verify=False)
    if r.status_code == 200:
        result = r.json()
        temp_list = []
        for i in result:
            try:
                repo = i['key']
                pattern = re.compile(r'\w*-helm-(dev|np|sbx)-local')
                result = pattern.match(repo)
                result = result.group(0)
                temp_list.append(result)
            except:
                result = None
        return temp_list
    else:
        print("Fail\n")

''' Get a list of all Helm artifacts in Artifactory'''
def get_artifacts(repo):
    url = repository + "/api/search/aql"
    data = 'items.find({"repo":{"$eq": "' + repo + '"}})'
    r = requests.post(url, auth=auth, headers=headers, data=data, verify=False)
    if r.status_code == 200:
        result = r.json()
        return result
    else:
        print("Fail\n")

''' Parse artifacts from dev or feature branches'''
def parse_artifacts(repo):
    # repos = get_repolist(repo)
    result = get_artifacts(repo)
    temp_list = []
    for i in result["results"]:
        filename = i["name"]
        try:
            pattern = re.compile(r'(\w*-*)(\w*-*)(\w*)-(\d*\.\d*\.\d*)-(\w+-*\w*-*\w*\.)tgz')
            artifacts = pattern.match(filename)
            artifact = artifacts.group(0)
        except:
            artifact = None
        if artifact != None:
            temp_list.append(filename)
    return temp_list

''' Delete artifact from a repository'''
def delete_artifact(repo, artifact):
    url = repository + '/' + repo + "/" + artifact
    try:
      r = requests.delete(url, auth=auth, verify=False)
      #print(r.status_code)
    except:
        print(artifact + "not deleted")

repo_list = get_repolist()
for repo in repo_list:
    result = parse_artifacts(repo)
    if result:
        for artifact in result:
            print(repo, artifact)
            # delete_artifact(repo, artifact)