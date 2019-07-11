import requests
import json
from requests.auth import HTTPBasicAuth
username = 'sumo99'
password = 'jR22AtfeR9bNbSe'
r = requests.get(
    'https://api.github.com/search/issues?utf8=✓&q=is%3Aopen+is%3Aissue+label%3A"good+first+issue"')
repo_urls = []
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    resultSet = repoItem.get("items")
    for result in resultSet:
        repo_urls.append(result.get("repository_url"))
resultSet = []
for apiUrl in repo_urls:
    print(apiUrl)
    repo_details = requests.get(apiUrl, auth=HTTPBasicAuth(username, password))
    if(repo_details.ok):
        repoResult = json.loads(repo_details.text or repo_details.content)
        resultSet.append(repoResult.get("full_name"))
    else:
        print(repo_details)
        print("Error getting the repository!")
for result in resultSet:
    print(resultSet)
print(resultSet[0])
