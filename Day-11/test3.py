import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

for i in range(len(response.json())):
    print(response.json()[i]["user"]["login"])

'''
danwinship
bmwiedemann
bmwiedemann
bmwiedemann
bmwiedemann
p0lyn0mial
adityasamant25
leemingeer
kannon92
kannon92
kannon92
harche
aroradaman
angeladietz
p0lyn0mial
p0lyn0mial
ZacharyZQ
MikeSpreitzer
ardaguclu
lianghao208
CatherineF-dev
benluddy
liggitt
gyuho
p0lyn0mial
carlory
carlory
lianghao208
carlory
carlory

'''

# print(response.status_code) --> 200

# print(len(response.json())) --> 30
# print(range(len(response.json()))) # will get a sequence --> range(0,30)  


# print(response.json()[0]["user"]) now use it in a for loop
    
'''
print(response.json()[0]["user"]) will give this below output

$ python test3.py 
{'login': 'danwinship', 'id': 96040, 'node_id': 'MDQ6VXNlcjk2MDQw', 'avatar_url': 'https://avatars.githubusercontent.com/u/96040?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/danwinship', 'html_url': 'https://github.com/danwinship', 'followers_url': 
'https://api.github.com/users/danwinship/followers', 'following_url': 'https://api.github.com/users/danwinship/following{/other_user}', 'gists_url': 'https://api.github.com/users/danwinship/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/danwinship/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/danwinship/subscriptions', 'organizations_url': 'https://api.github.com/users/danwinship/orgs', 'repos_url': 'https://api.github.com/users/danwinship/repos', 'events_url': 'https://api.github.com/users/danwinship/events{/privacy}', 'received_events_url': 'https://api.github.com/users/danwinship/received_events', 'type': 'User', 'site_admin': False}

'''

# print(response.json()[0]["user"]["login"]) now use it in a for loop

'''
print(response.json()[0]["user"]["login"]) will give this output

danwinship
'''

# for i in range(len(response.json())):
#     print(i)


# for i in range(0,30):
#     print(i)

