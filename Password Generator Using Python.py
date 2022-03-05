import random
import string
letters=string.ascii_letters
numbers='1234567890'
special_characters='!@#$%^-=+_&'
symbols=letters+numbers+special_characters
password_length=int(input("Enter Password Length: "))
password="".join(random.sample(symbols,password_length))
print(password)
