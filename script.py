import re

# Sample input text
text = input("Enter the text you want to extract data from:\n")

# Regex patterns below

# Email regex
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
print("Emails:", emails)

# URL regex
urls = re.findall(r'https?://[^\s]+', text)
print("URLs:", urls)
