import re

with open("sample.txt", "w") as file:
    file.write("""
Hello user,

Contact us at support@gmail.com
For business queries: company123@yahoo.com
Personal mail: test.user@outlook.com
""")

with open("sample.txt", "r") as file:
    data = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)

with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")

print("\nExtracted Emails:")
for email in emails:
    print(email)
