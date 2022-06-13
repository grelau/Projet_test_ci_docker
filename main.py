def count_char(password):
    i = 0
    for letter in password:
        i += 1
    return i

def check_if_maj(password):
    upper = False
    for letter in password:
        if letter.isupper():
            upper = True
    return upper

def check_if_special(password):
    result = False
    special = ['!', '*', '-']
    for letter in password:
        if letter in special:
            result = True
    return result

def check_if_valid_password(password):
    password_len = 10
    if count_char(password) < password_len:
        return False
    if check_if_maj(password) == False:
        return False
    if check_if_special(password) == False:
        return False
    return True

result = check_if_valid_password("Bonjourrrrrr")
if result == True:
    print("password is valid")
else:
    print('password is invalid')


