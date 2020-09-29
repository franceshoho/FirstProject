def range_sum(numbers, start, end):
    # return sum of numbers between start and end
    total = 0
    for number in numbers:
        if start <= number <= end:
            total += number
    return total


def last_indexof_max(numbers) :
    # return the last index of max. number in a list of numbers
    if not numbers :
        return -1
    index = len(numbers) - 1
    for i in range(index, 0, -1) :
        if numbers[i] > numbers[index] :
            index = i
    return index


def first_indexof_max(numbers):
    if not numbers :
        return -1
    index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[index]:
            index = i
    return index

def average(numbers):
    numbers = [float(x) for x in input()]
    print(sum(numbers) / len(numbers))

def number_divided_by3(min, max):
    return [number for number in range(min, max+1) if number % 3 == 0]



def main():
    # input1 = "5 1 3 4 2"
    # input2 ="2 4"
    input1 = input("Please enter a string of numbers: ")
    input_numbers = [int(number) for number in input1.split(" ")]
    a, b = [int(n) for n in input("enter start end range: ").split()]
    print(range_sum(input_numbers, a, b))
    print("first index of MAX: ", first_indexof_max(input_numbers))
    print("last index of MAX: ", last_indexof_max(input_numbers))

    # if you have a string number without a space.  Don't need split()
    numbers_nospace = input("please input numbers without space: ")
    numbers = [float(x) for x in numbers_nospace]
    print(average(numbers))

    words = ["apple", "it", "creek", "pelican", "subsequent", "horse",
             "apothecary"]
    words_len =[len(word) for word in words]
    print(words_len)

    print("Number divided by 3 between 0-100:",
          number_divided_by3(0, 100))


if __name__ == "__main__":
    main()