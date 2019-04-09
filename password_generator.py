import random
import string

char = string.ascii_letters + string.digits + string.hexdigits
password_len = int(input("Enter password len : "))
print(''.join(random.sample(char,password_len)))
