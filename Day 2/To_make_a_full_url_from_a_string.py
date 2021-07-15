input_string = str(input())
test = input_string.replace("#"," ")
test_list = list(test)
count = 0
test_space = test_list.index(" ")
for space in range(len(test_list)):
    if(test_list[space] == " "):
        if(count < 2):
            test_list[space] = "."
            count += 1
        else:
            test_list[space] = "/"
strs = ""
for i in test_list:
    strs += i
print("https://"+strs+"/")