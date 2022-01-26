import re

name = "Md. Dulal Miah"

if re.search("\w{2,10}.\s\w{3,10}\s\w{4,10}" , name):
    print("yes")
else:
    print("No")