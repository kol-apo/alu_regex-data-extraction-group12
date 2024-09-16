#!/usr/bin/python3

from email_regex import extract_emails
from phone_regex import extract_phone_numbers
from url_regex import extract_urls
from credit_card_regex import extract_credit_card_numbers
from time_regex import extract_times
from html_tag_regex import extract_html_tags
from currency_regex import extract_currency
from hashtag_regex import extract_hashtags

def read_sample_file():
    with open('test_data/sample.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    text = read_sample_file()

    print("Emails:", extract_emails(text))
    print("URLs:", extract_urls(text))
    print("Phone Numbers:", extract_phone_numbers(text))
    print("Credit Card Numbers:", extract_credit_card_numbers(text))
    print("Times:", extract_times(text))
    print("HTML Tags:", extract_html_tags(text))
    print("Hashtags:", extract_hashtags(text))
    print("Currency Amounts:", extract_currency(text))
