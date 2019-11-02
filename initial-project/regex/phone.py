import re


def extract_phone(input_string):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input_string)
    if match:
        return match.group()
    return None


def extract_all_phone(input_string):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input_string)


def is_valid_phone(input_string):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.fullmatch(input_string)
    if match:
        return True
    return False


print(extract_phone("my number is 432 567-8976"))
print(extract_all_phone("my number is 432 567-8976 or 282 897-0987 "))
