import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')


res = pattern.search('Call me at 515 555-4242!')

res2 = pattern.findall('Call me at 515 555-4242! or 534 678-7272')

print(res.group())

print(res2)

response3 = re.search(r'\d{3} \d{3}-\d{4}', 'Calm down folks and call 675 134-9090')

print(response3.group())


