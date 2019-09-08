# get input of array of numbers
# find pairs of numbers that equal 15

print("\nEnter a list of numbers and i will find the pairs whose some equals 15.")
print("------------------------------------------------------------------------")
input_arr = input("Enter array of elements comma separated :\n")

num_arr = list(map(int, input_arr.split(',')))

print(num_arr)
