import random
n = int(input('Length of the Password : '))
ques = input('Password with Special Character/Characters? Y or N : ')
allal = 'ABCDEFGHIJKLMNOPQRSTUVWKYZabcdefghijklmnopqrstuvwxyz'
allsp = 'ABCDEFGHIJKLMNOPQRSTUVWKYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{}[]<>?|\/'
withi = '!@#$%^&*()_+{}[]<>?|\/'

password = ''
for i in range(n):
    if ques == 'N':
        password+=random.choice(allal)
    elif ques == 'Y':
        password= random.choice(allsp)+ random.choice(withi) + password
    else:
        password = '~ERROR~'
print(password)