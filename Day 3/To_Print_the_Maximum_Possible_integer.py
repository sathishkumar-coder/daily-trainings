def sumofdigits(num):
    int_to_string = str(num)
    test = list(map(int, int_to_string.strip()))
    return (sum(test))
    
num = int(input())
sum_of_digits = sumofdigits(num)
for i in range(num-1, 10, -1):
    if(sumofdigits(i) > sum_of_digits):
        print(i)
        break
    else:
        if(i == 11):
            print(N)
            break