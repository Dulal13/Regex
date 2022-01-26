import re

txt = "I am Dulal and ready for coding"

if re.search("Dulals" , txt):

    print("Dulal is here")

else:
    print("Not present")

find = re.findall("Dulal" , txt)

print(find)