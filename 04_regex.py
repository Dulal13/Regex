import re

# names = "Dulal , Dulali , Kalam , Labonno , Joui"

# name = re.findall('[DKL]ulali' , names)

# print(name)


str = "Sat , cat , mat , chat"

lst = re.findall('[smc]at' , str)

print(lst)