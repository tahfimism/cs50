from validator_collection import validators, errors

mail = input("What's your email address? ")

try:
    validators.email(mail)
    print("Valid")
except ValueError:
    print("Invalid")
