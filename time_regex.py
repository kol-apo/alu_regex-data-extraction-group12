#!/usr/bin/python3
import re

def extract_times(text):
    time_pattern_24 = r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b'  # 24-hour format
    time_pattern_12 = r'\b(1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM|am|pm)\b'  # 12-hour format
    return re.findall(f'{time_pattern_24}|{time_pattern_12}', text)

