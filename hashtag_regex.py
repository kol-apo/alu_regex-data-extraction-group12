import re

def extract_hashtags(text):
    hashtag_pattern = r'#\w+'
    return re.findall(hashtag_pattern, text)

