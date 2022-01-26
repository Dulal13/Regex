import re


phn_number = '345-6788-5678'

if re.search('\w{3}-\w{3}-\w{4}' , phn_number):
    print("Yes! It is a phone number")
else:
    print("It is not")
