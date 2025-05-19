Project Name: REGEX DATA EXTRACTOR

Project description:This is a simple project built using Python to extract structured data from unstructured text using Regular Expressions (Regex).
The app allows user to extracts specific types of data such as email addresses, phone numbers, URLs, and hashtags.
This project was built as part of a regex data extraction assignment to demonstrate real-world use of pattern matching and text analysis.

Types of data the app extracts: Email addresses, URLs, Phone numbers, Hashtags, and Time.

How to run: Run the script in your terminal, or use the file in vs code. Remember to paste your text input and then press Enter when prompted.

Sample Data:
Hello! You can reach me at umwalinda@gmail.com

Visit our website at https://www.LU.com or our blog at https://blog.LU.org/page.

For inquiries, call (250) 786-7890.

Our prices range from $19.99 to $1,234.56. We also accept credit card numbers like 1234-5678-9012-3456.

Follow us on social media #umwali #WebDevLife.

We’re open from 2:30 AM to 14:30 PM


you can use that text as the input for testing.

OUTPUT:
Emails: ['umwalinda@gmail.com']
URLs: ['https://www.LU.com, https://blog.LU.org/page']
Phone number: ['(250)786-7890']
Hashtags: ['#umwli, #WebDevLife']
Times" ['2:30 AM, 14:30 PM']

Files in this Project: script.py, and README.md(this file)

Some Error Handling methods:
If no valid phone numbers are found, a message will appear asking the user to check their input.

Invalid formats like phone numbers with letters (e.g., 123-abc-7890) will be ignored.

The script handles a variety of input formats and spacing from different counrties.

My Names:UMWALI Linda
Github username: Linda5-umwali

