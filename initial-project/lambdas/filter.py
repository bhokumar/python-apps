users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

inactive_users_names = list(map(lambda user: user["username"], list(filter(lambda u: not u["tweets"], users))))

print(inactive_users_names)

user_names = [user["username"] for user in users if not user["tweets"]]

print(user_names)