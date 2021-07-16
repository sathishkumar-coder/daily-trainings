string_ = input()
f = string_.replace("#"," ")
l = f.split(' ')
b = [int(i) for i in l]
n = 0
for i in b:
    if i<0:
        n+= 1
print(n)