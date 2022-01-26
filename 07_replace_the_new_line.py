import re

randStr = '''
I am ready for
my 
new job

'''

regex = re.compile("\n")

randStr = regex.sub(" " , randStr)
print(randStr)