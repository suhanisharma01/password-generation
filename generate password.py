import random
import string

def strong_password(len):
    password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password) for i in range(len))

len = 9
A = strong_password(len)
print(A)
