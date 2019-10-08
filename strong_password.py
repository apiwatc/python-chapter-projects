import re


def password_detection(passwd):
    if len(passwd) < 8:
        print("Minimum 8 characters")
    else:
        if re.match(r'[0-9]{8,}', passwd):
            print("Invalid: expect at least one upper and lower character")
        elif re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', passwd):
            print("Valid")
        else:
            print("Invalid")
        # pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')


passwd = input('Password: ')
password_detection(passwd)
