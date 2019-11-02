import re


def parse_bytes(input_string):
    byte_regex = re.compile(r'[0-1]{8}')
    return byte_regex.findall(input_string)
