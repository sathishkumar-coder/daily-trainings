height_of_student = str(input())
height = list(height_of_student)
sorted= sorted(height)
test_list = []
for height in range(len(sorted)):
        if height[i] != sorted[i]:
            test_list += height[i]
if sorted == height:
    print("0")
elif len(test_list) == len(sorted):
    print(len(test_list))
else:
    print(len(sorted)-len(test_list))