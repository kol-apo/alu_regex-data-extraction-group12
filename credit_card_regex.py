import re

def extract_credit_card_numbers(text):
    credit_card_pattern = r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}'
    return re.findall(credit_card_pattern, text)

