import re


def is_valid_time(input_string):
    time_regex = re.compile(r'^[0-9]{1,2}:[0-9]{2}$')
    match = time_regex.fullmatch(input_string)
    if match:
        return True
    return False
