import functools

numbers = [1, 2, 3, 4]
dogs = ["Fido", "Aila", "Pluto", "Lady"]

# None functional (how to do)
total = 0
for number in numbers:
    total += number

print(total)

# Functional (what you want)
print(sum(numbers))

# Functional (without the sum function)
print(functools.reduce(lambda my_sum, x : my_sum + x, numbers))

# None Functional
def show_first_none():
    global numbers
    return numbers[0]

print(show_first_none())

# Functional 
def show_first(list):
    return list[0]

print(show_first(numbers))

# (None functional) with local variable that are changed
def my_sum_none(list):
    total = 0
    for number in list:
        total += number
    return total

print(my_sum_none(numbers))

# Functional, no variable - recursion
def my_sum(list):
    if not list:
        return 0
    else:
        return list[0] + my_sum(list[1:])

print(my_sum(numbers))

# None Functional, multiply numbers by 2
def double_none(list):
    new_numbers = []
    for number in list:
        new_numbers.append(number * 2)
    return new_numbers

print(double_none(numbers))

# Functional
def double_one(number):
    return number * 2

print(list(map(double_one, numbers)))

double_lambda = lambda number : number * 2
print(list(map(double_lambda, numbers)))

print(list(map(lambda number : number * 2, numbers)))

# None functional fibonacci
def fibonacci_none(n, first = 1, second = 1):
    my_list = []
    for i in range(n):
        my_list.append(first)
        first, second = second, first + second
    return my_list

print(fibonacci_none(10))

# None functional with a generator (one time list)
def fibonacci_gen(n, first = 1, second = 1):
    for i in range(n):
        yield(first)
        first, second = second, first + second

print(list(fibonacci_gen(10)))

# None functional - bad recursive
def fibonacci_recur(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)

my_list = []
for i in range(1, 11):
    my_list.append(fibonacci_recur(i))

print(my_list)

# Functional - Good recursive
fibonacci = (lambda n, first = 1, second = 1 : [] if n == 0 else [first] + fibonacci(n-1, second, first + second))
print(fibonacci(10))

# None functional list iteration
big_dog_none = []
for dog in dogs:
    big_dog_none.append("Big {}".format(dog))

print(big_dog_none)

# Functional using comprehension ("understanding" - create a list from iterable)
print(["Big {}".format(dog) for dog in dogs])

# First class function - (Delegate in C#) - function as a parameter (or return, variable)
def my_name(name):
    print(name)

my_new_name = my_name
my_name("Hugo")
my_new_name("Hugo")

# Higher order function (Close connected to first class functions (Delegates in C#))
def my_convert(to, number):
    return to(number)

print("Number = " + my_convert(str, 10.132))
print("Number = " + my_convert(str, my_convert(int, 10.132)))

# Filter function (dog with an i)
print(list(filter(lambda x : 'i' in x, dogs)))
