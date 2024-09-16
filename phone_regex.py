import re

def extract_phone_numbers(text):
    phone_pattern = r'\(?\d{3}\)?[.\-\s]?\d{3}[.\-\s]?\d{4}'
    return re.findall(phone_pattern, text)
