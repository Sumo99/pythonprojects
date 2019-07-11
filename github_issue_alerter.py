import requests
import json
from requests.auth import HTTPBasicAuth
import os
from gi.repository import GObject
from gi.repository import Notify


class SendNotification(GObject.Object):
    def __init__(self):

        super(SendNotification, self).__init__()
        # lets initialise with the application name
        Notify.init("myapp_name")

    def send_notification(self, title, text, file_path_to_icon=""):

        n = Notify.Notification.new(title, text, file_path_to_icon)
        Notify.Notification.set_timeout(n, Notify.EXPIRES_NEVER)
        n.show()


my = SendNotification()
username = 'user'
password = 'password'
repo_urls = []
accepted_languages = ["JavaScript", "Python",
                      "Java", "TypeScript", "Go", "Kotlin", "SQL"]
for i in range(1, 11):
    reqUrl = 'https://api.github.com/search/issues?utf8=✓&q=is%3Aopen+is%3Aissue+label%3A"good+first+issue"&page="' + \
        str(i)+"\""
    print(reqUrl)
    r = requests.get(reqUrl)
    if(r.ok):
        repoItem = json.loads(r.text or r.content)
        resultSet = repoItem.get("items")
    for result in resultSet:
        repo_urls.append(result.get("repository_url"))
print(len(repo_urls))
resultSet = set()
for apiUrl in repo_urls:
    print(apiUrl)
    repo_details = requests.get(apiUrl, auth=HTTPBasicAuth(username, password))
    if(repo_details.ok):
        repoResult = json.loads(repo_details.text or repo_details.content)
        language_details = str(repoResult.get("language", "") or "")
        if(language_details in accepted_languages):
            resultSet.add(repoResult.get("full_name", "") +
                          " "+language_details+" "+str(repoResult.get("stargazers_count", "")))
    else:
        print(repo_details)
        print("Error getting the repository!")
print(resultSet)
for result in resultSet:
    my.send_notification("Some github projects to contribute to", result)
