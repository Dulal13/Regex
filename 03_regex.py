import re

str = "we need to inform him with latest information"

for i in re.finditer("inform" , str):

    locTup = i.span()
    print(locTup)