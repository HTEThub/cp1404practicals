"""
Emails
Estimate: 30 minutes
Actual: 40 minutes
"""

email_to_names = {}

email_input = input("Email: ")
while email_input != "":
    split_domain = email_input.split("@")
    email_name = split_domain[0].split(".")
    name = ' '.join(email_name)
    name = name.title()
    email_to_names[email_input] = name
    choice = input(f"Is your name {name}? (Y/n): ").lower()
    if choice == "n":
        real_name = input("Your Name: ")
        email_to_names[email_input] = real_name
    email_input = input("Email: ")
for email, name in email_to_names.items():
    print(f"{name} ({email})")
