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

# Phone number regex
phones = re.findall(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', text)

if not phones:
    print("⚠️ No valid phone numbers found. Please check your input.")
else:
    print("Phone Numbers:", phones)

