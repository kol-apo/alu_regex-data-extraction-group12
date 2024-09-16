#!/usr/bin/python3
import re

def extract_urls(text):
    url_pattern = r'https?://[^\s/$.?#].[^\s]*'
    return re.findall(url_pattern, text)

