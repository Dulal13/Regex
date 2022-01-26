import re

str = "cat , dat,pat,aat"
lst = re.findall('[^a-d]at' , str)
print(lst)