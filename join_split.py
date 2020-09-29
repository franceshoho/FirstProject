# put your python code here
numbers = "5 8 2 7 8 8 2 4"
target = "8"
numbers = numbers.split()  # turn number string into a list of numbers
return_list = []  # to hold position index

for i, number in enumerate(numbers):
    if (number == target) :
        return_list.append(str(i))

if (return_list != []) :
    print(" ".join(return_list))
else :
    print("not found")


def range_sum(numbers, start, end):
    # return sum of numbers between start and end
    total = 0
    for number in numbers:
        if start <= number <= end:
            total += number
    return total



input_numbers = [int(number) for number in input().split(" ")]  # list of input numbers
a, b = [int(n) for n in input().split()]  # get range a and b
print(range_sum(input_numbers, a, b))

numbers = input("input string to reverse").split(" ")
print(numbers)
