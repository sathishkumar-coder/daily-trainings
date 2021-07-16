import json
input_stri = str(input())
test_stri = ''
for ele in input_stri[:-2]:
    if ele.isdigit() == True:
        test_stri += ele
test_listone= list(test_stri)
test_listtwo = []
identity = 0
for number in test_listone:
    diff = int(number) - identity - 1
    if diff:
        test_listtwo += ["Push","Pop"] * diff
    test_listtwo += ["Push"]
    identity = int(number)
dump_list = json.dumps(test_listtwo)
output_list = dump_list.replace(", ",",")
print(output_list)