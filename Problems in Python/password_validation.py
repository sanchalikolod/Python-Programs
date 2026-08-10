#Password Validation

def validation(password):
    upper=0
    lower=0
    digit=0
    special=0
    if len(password)<8:
        return False
    for ch in password:
        if ch.isupper():
            upper=upper+1
        if ch.islower():
            lower=lower+1
        if ch.isdigit():
            digit=digit+1
        else:
            special=special+1
    for i in range(len(password)-2):
        if password[i]==password[i+1]==password[i+2]:
            return False
    if upper>=2 and lower>=2 and digit>=2 and special>=1:
        return True

password=input("Enter your password: ")
if validation(password):
    print("Valid password.")
else:
    print("Invalid password.")
