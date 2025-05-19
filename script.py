import re

# Sample input text
text = input("Enter the text you want to extract data from:\n")

# Regex patterns below

# Email regex
emails = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', text)
print("Emails:", emails)

# URL regex
urls = re.findall(r'(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?', text)
print("URLs:", urls)

# Phone number regex
phones = re.findall(r'\b(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}\b', text)
if not phones:
    print("No valid phone numbers found. Please check your input.")
else:
    print("Phone Numbers:", phones)

# Hashtag regex
hashtags = re.findall(r'#\w+', text)
print("Hashtags:", hashtags)

#Time regex
times = re.findall(r'\b\d{1,2}:\d{2}(?:\s?[APap][Mm])?\b', text)
print("Times:", times)

if not any([emails, urls, phones, hashtags, times]):
    print("No recognizable data found in the input.")
