import random
from string import ascii_uppercase, ascii_lowercase, digits

def get_random_password(length = 8) -> str:
    str_ = ascii_uppercase + ascii_lowercase + digits
    password = ''.join(random.sample(str_, length))
    return password

print(get_random_password())
