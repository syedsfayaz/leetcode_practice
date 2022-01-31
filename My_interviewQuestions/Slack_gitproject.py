# import git
# import datetime
# import os
# from time import *
# from os import path
# from git import Repo
#
# #repo = 'syedsfayaz/ConferenceRooms'
#
# def commit_files():
#     if repo != None:
#         new_branch = 'your_new_branch'
#         current = repo.create_head(new_branch)
#         current.checkout()
#         master = self.repo.heads.master
#         repo.git.pull('origin', master)
#         #creating file
#         dtime = strftime('%d-%m-%Y %H:%M:%S', localtime())
#         with open(self.local_repo_path + path.sep + 'lastCommit' + '.txt', 'w') as f:
#             f.write(str(dtime))
#         if not path.exists(self.local_repo_path):
#             os.makedirs(self.local_repo_path)
#         print('file created---------------------')
#
#         if repo.index.diff(None) or repo.untracked_files:
#
#             repo.git.add(A=True)
#             repo.git.commit(m='msg')
#             repo.git.push('--set-upstream', 'origin', current)
#             print('git push')
#         else:
#             print('no changes')
#
# commit_files()



import json
import requests
from datetime import datetime

def gh_sesh(user, token):
    s = requests.Session()
    s.auth = (user, token)
    s.headers = {'accept': 'application/vnd.github.v3+json'}
    return s

class GH_Response_Obj:
    def __init__(self, json_all, next_page):
        self.json_all = json_all
        self.next_page = next_page

def gh_get_request(gh_user, gh_token, url):
    s = gh_sesh(gh_user, gh_token)
    response = s.get(url)
    response_status = response.status_code
    if response_status > 200:
        print(f'\n This was the response code: {response_status}')
        exit()

    json = response.json()
    links = response.links

    try:
        next_page = links['next']['url']
    except:
        next_page = None

    full = GH_Response_Obj(json, next_page)

    return full

def gh_post_request(gh_user, gh_token, url, data):
    s = gh_sesh(gh_user, gh_token)
    response = s.post(url, data)
    response_status = response.status_code
    if response_status > 201:
        print(f'\n This was the response code: {response_status}')
        exit()

    json = response.json()

    return json

# def get_branch_sha(gh_user, gh_token, repo_name, branch_name="master"):
# 	'''
# 		Input the FULL repo name in the owner/repo_name format. Ex: magento/knowledge-base
# 		Defaults to master branch. If you don't want to use the master branch, use a different argument.
# 	'''
#
# 	url = f'https://api.github.com/repos/{repo_name}/branches/{branch_name}'
# 	response =gh_get_request(gh_user, gh_token, url)
# 	sha = response.json_all['commit']['sha']
# 	return sha
#
# def create_new_branch(gh_user, gh_token, master_branch_sha):
# 	now = str(datetime.now()).replace(' ', '__').replace(':', '-').replace('.', '')
# 	new_sync_branch = f'new_branch_{now}'
# 	url = f"https://api.github.com/repos/magento-commerce/knowledge-base/git/refs"
#
# 	data = {
# 		"ref": f'refs/heads/{new_sync_branch}',
# 		"sha": master_branch_sha
# 	}
#
# 	data = json.dumps(data)
#
# 	response =gh_post_request(gh_user, gh_token, url, data)
#
# 	return response
#
# def main():
# 	gh_user = input(f"Input your GH username: \n")
# 	gh_token = input(f"Input your GH token: \n")
#     gh_reponame = input(f"Input your GH token: \n")
#     sha = get_branch_sha(gh_user, gh_token, repo_name)
# 	new_sync_branch = create_new_branch(gh_user, gh_token, sha)
# 	print(new_sync_branch)
#
# if __name__ == '__main__':
# 	main()

from invoke import task
@task
def tag(c):
    current_ver = c.run('git describe', hide=True, warn=True).stdout
    return current_ver
print(tag)