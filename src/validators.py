import re

EMAIL_TEMPLATE = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", re.I)

def email_validate(email: str) -> bool:
    if not EMAIL_TEMPLATE.fullmatch(email):
        return False

    return True

def pwd_validate(pwd: str) -> bool:
    specialCharacters = "~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/"

    if all(x not in specialCharacters for x in pwd) or any(char.isdigit() for char in pwd) == False or len(pwd) < 8:
        return False

    return True

def login_validate(login: str) -> bool:
    specialCharacters = "~!@#$%^&*-+=`|\(){}[]:;'<>,?/"

    if any(char in specialCharacters for char in login) or re.search('[а-яА-Я]', login):
        return False

    return True