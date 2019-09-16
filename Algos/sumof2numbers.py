# get input of array of numbers
# find pairs of numbers that equal 15

print("\nEnter a list of numbers and i will find the pairs whose some equals 15.")
print("------------------------------------------------------------------------")
input_arr = input("Enter array of elements comma separated :\n")

print(type(input_arr))
print(input_arr)

num_arr = list(map(int,input_arr.split(",")))

count = 0
res = []

for num in num_arr:
    temp = 15 - num
    print(temp)
    if temp in num_arr:
        count += 1
        if num not in res:
            res.append(num)

print("number of pairs whose sume equal to 15 : " + str(count))
print(res)