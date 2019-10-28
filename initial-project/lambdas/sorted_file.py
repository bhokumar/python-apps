nums = [4, 6, 1, 30, 55, 23]
#nums.sort()

print(nums)

sorted_numbers = sorted(nums)

print(nums)

print(sorted_numbers)


users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

sorted_user = sorted(users, key=lambda user: user['username'])

sorted_user_tweets = sorted(users, key=lambda user: len(user['tweets']))

print(sorted_user)

print(sorted_user_tweets)