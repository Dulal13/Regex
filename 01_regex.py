import re


nameAge = '''
     Ismail is 34 and Dulal is 22       
'''
# The r means that the string is to be treated as a raw string, which means all escape codes will be ignored.
age = re.findall(r'\d{1,3}',nameAge)
names = re.findall(r'[A-Z][a-z]*',nameAge)

# print(age)
# print(name)

nameAgeDict = {}
i = 0

for name in names:

    nameAgeDict[name] = age[0]
    i += 1

print(nameAgeDict)
