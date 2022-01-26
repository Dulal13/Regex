import re

str = "I am best sing a song"

regex = re.compile('[s]ing')

str = regex.sub("Dulal" , str)
print(str)