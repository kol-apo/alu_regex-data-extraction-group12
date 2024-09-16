#!/usr/bin/python3
import re

import re

def extract_times(text):
    # Define 24-hour time format
    time_pattern_24 = r'([01]?\d|2[0-3]):[0-5]\d'
    # Define 12-hour time format (with optional AM/PM)
    time_pattern_12 = r'([01]?\d):[0-5]\d\s?[APap][Mm]'

    # Combine both patterns
    combined_pattern = time_pattern_24 + '|' + time_pattern_12

    # Extract times using the combined pattern
    return re.findall(combined_pattern, text)
