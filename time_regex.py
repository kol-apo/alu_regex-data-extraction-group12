#!/usr/bin/python3
import re

def extract_times(text):
    time_pattern = r'([01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?'
    combined_pattern = time_pattern_24 + '|' + time_pattern_12
    return re.findall(combined_pattern, text)
