import string 
str_input=input()
missing=""
for i in string.ascii_lowercase:
    if i not in str_input:
        missing+=ele
print(missing)
