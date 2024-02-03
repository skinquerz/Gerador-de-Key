import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"


all = lower + upper + numbers +symbols
length = int(input('qual a quantidade de caracteres? '))
password = "".join(random.sample(all,length))
print(f'sua senha random é:{password}')
