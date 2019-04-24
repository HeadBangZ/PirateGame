import random

def bubblesort(numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

numbers = [2, 4, 4, 11, 3, 1, 5, 67, 119, 77, 31, 24, 17, 28, 29, 37]

print(str(len(numbers)) + " numbers: ", numbers)
bubblesort(numbers)
print(str(len(numbers)) + " numbers: ", numbers)


def binary_search(number, numbers):
    min_index = 0
    max_index = len(numbers) - 1
    found = False
    while not found and min_index <= max_index:
        median = (min_index + max_index) // 2
        if numbers[median] == number:
            found = True
            answer = median
        elif numbers[median] > number:
            max_index = median - 1
        else:
            min_index = median + 1
    if not found:
        answer = -1
    return answer

print("Sorted numbers", numbers)
for i in [0, 1, 2, 4, 67, 77, 500, 119]:
    result = binary_search(i, numbers)
    if result == -1:
        print(str(i) + " not found")
    else:
        print(str(i) + " found at position " + str(result))

print()

# Dice rolling for statistics
def dice_statistic(throws):
    single_statistics = [0, 0, 0, 0, 0, 0]
    double_statistics = 0
    sum_of_singles = 0

    for i in range(0, throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        single_statistics[dice1 - 1] += 1
        single_statistics[dice2 - 1] += 1
        if dice1 == dice2:
            double_statistics += 1
    
    for i in range(0, len(single_statistics)):
        sum_of_singles += single_statistics[i]
    print(single_statistics, "Number of rolls", str(sum_of_singles))
    print(str(double_statistics), "Doubles out of ", throws, "throws")    

dice_statistic(100)