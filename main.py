import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"


all = lower + upper + numbers +symbols
length = int(input("numero de carctares? "))
password = "".join(random.sample(all,length))

print("sua senha random é:",password)
