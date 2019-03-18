import requests
r = requests.get('https://api.github.com/search/issues?q=%22%22+label:%22Good+First+Issue%22+state:open')
r.json()
#to do use the notifier subprocess to alert the user when a issue is available!
