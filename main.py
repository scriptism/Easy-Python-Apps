# imports:
import math

# ----cube a number
def cube_number(n):
    return n ** 3
print(cube_number(3))  

# ----cube a number (alternative method)
def cube_number(n):
    return n * n * n
print(cube_number(3))

# ----find square root of a number
# needs -import math at the top-
def find_square_root(n):
    return math.sqrt(n)
print(find_square_root(16))


# ----calculate power of a number
# needs -import math at the top-
def calculate_power(base, exponent):
    return math.pow(base, exponent)
result = calculate_power(5, 3)
print(result)

# or

def calculate_power_2(base, exponent):
    return base ** exponent
result = calculate_power_2(5, 3)
print(result)

# ----simple interest calculation
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(simple_interest(1000, 5, 3)) 

# ----add two numbers and concatenate with their sum
def add_numbers(num1, num2):
    total = num1 + num2
    return f"{num1}{num2}{total}"
print(add_numbers(7, 5))   # 7512

# ----add two numbers with special case for zero sum
def add_numbers2(num1, num2):
    if num1 + num2 == 0:
        return 0
    total = num1 + num2
    return f"{num1}{num2}{total}"

print(add_numbers2(0, 0))   # 0
print(add_numbers2(2, 3))   # 235

# ----calculate 2 to the power of n
def power_of_two(n):
    return 2 ** n

print(power_of_two(3))   # 8
print(power_of_two(0))   # 1
print(power_of_two(6))   # 64

# ----calculate profit or loss
def calculate_profit_loss(cost_price, selling_price):
    diff = round(abs(selling_price - cost_price), 2)
    if selling_price > cost_price:
        return f"Profit: {diff}"
    elif selling_price < cost_price:
        return f"Loss: {diff}"
    else:
        return "No profit or loss"

print(calculate_profit_loss(100, 120))  # Profit: 20.0
print(calculate_profit_loss(100, 80))   # Loss: 20.0
print(calculate_profit_loss(100, 100))  # No profit or loss

# ----calculate time saved by faster speed
def time_saved(distance, speed1, speed2):
    time1 = distance/speed1
    time2 = distance/speed2
    return round((time1 - time2), 2)
print(time_saved(100, 50, 100))  # 1.0 hour saved
print(time_saved(150, 30, 60))   # 2.5 hours
    

# ----combine two lists of fruits
def fruit_salad(list1, list2):
    return list1 + list2
print(fruit_salad(['apple', 'banana'], ['orange', 'grape']))  

# ---concatenate two lists
def concatenate_lists(list1,list2):
    return list1 + list2
print(concatenate_lists([1,2,3], [12,51,16]))

# ---calculate BMI
def calculate_bmi(weight, height):
    return round((weight/height ** 2), 2)
print(calculate_bmi(70, 1.75))  

# ----calculate area of a circle
def calculate_area(radius):
    area = math.pi * radius **2
    return round(area, 2)
print('Area of a circle with r = 5:', calculate_area(5), 'cm²')

# ----check user preference between car and bike
def check_preference(preference):
    if preference.lower() == "car":
        return "You like car."
    else:
        return "You like bike."
print(check_preference("car"))
# or
def check_preference_2(preference):
    p = preference.lower()
    if p == "car":
        return "You like car"
    elif p == "bike":
        return "You like bike"
    else:
        return "Unknown preference"
print(check_preference_2("bike"))

# ----find the last digit of a number
def last_digit(n):
    return abs(n) % 10
print(last_digit(1234))
print(last_digit(-5678))

# ---sum the second and second last items in a list
def add_items(numbers):
    return numbers[1] + numbers[-2]
print(add_items([1, 2, 3, 4, 5]))  

# ---convert a string to a list of words
def string_to_list(s):
    return s.split()
print(string_to_list("Hello world!"))       
print(string_to_list("  Too   many spaces ")) 
print(string_to_list(""))  

# smiley face: 😊
def replace_smiley(text):
     return text.replace(':)', '😊')
print(replace_smiley("Hello :) How are you?"))

# ----sum numbers greater than n in a list
def sum_greater_than(numbers, n):
    return sum(x for x in numbers if x > n) 
print(sum_greater_than([1, 5, 10, 15, 20], 10))

# ----convert string to title case
def convert_to_titlecase(s):
    return s.title()
print(convert_to_titlecase("hello world from python"))


# ----filter integers from a mixed list
def filter_integers(lst):
    return [x for x in lst if type(x) is int]
print(filter_integers([1, 'two', 3.0, 4, 'five', 6]))


# ---repeat last character of a string n times
def repeat_last_char(string, n):
    return string + string[-1] * n
print(repeat_last_char("hello", 4))


# ----check if one list is a subset of another
def is_subset(list1, list2):
    return set(list1).issubset(list2)
print(is_subset([1, 2], [1, 2, 3, 4]))

# ----sum of squares of numbers in a list
def sum_of_squares(numbers):
     return sum(n ** 2 for n in numbers)
print(sum_of_squares([1, 2, 3, 4]))

# ----modify a tuple by adding an element
def modify_tuple(tupl, elem):
    return tupl + (elem, )
print(modify_tuple((1, 2, 3), 4))

# ----sum of even numbers in a list
def sum_of_evens(numbers):
    return sum(n for n in numbers if n % 2 == 0)
print(sum_of_evens([1, 2, 3, 4, 5, 6]))


# # ----check if a string contains spaces
def has_spaces(s):
    return ' ' in s
print(has_spaces("Hello World"))  # True
print(has_spaces("NoSpaces"))     # False

 

# ---check if a number is within a given range
def is_in_range(n, start, end):
    return start <= n <= end
print(is_in_range(5, 1, 10))


# ----check if two lines are parallel given their slopes
def are_parallel(m1, m2):
    return m1 == m2
print(are_parallel(2, 2))

# ----reverse a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))

# ----swap two values
def swap_values(a,b):
    return b, a
print(swap_values(5,10))


# ----eliminate odd numbers from a list
def eliminate_odd_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]
print(eliminate_odd_numbers([1,2,3,4,5,6,7,8,9,10]))

# ---sort a list in descending order
def sort_descending(numbers):
    return sorted(numbers, reverse=True)
print(sort_descending([5,2,9,1,5,6]))

# ---check if a dictionary is empty
def is_empty(dictionary):
    return len(dictionary) == 0
print(is_empty({}))

# ----check if a key exists in a dictionary
def key_exists(dict1, key):
    return key in dict1
print(key_exists({'a': 1, 'b': 2}, 'a'))


# -----calculate hypotenuse
# needs -import math- at the top
def calculate_hypotenuse(a, b):
    return math.hypot(a, b)
print(round(calculate_hypotenuse(4, 7), 3))


def merge_dictionaries(dict1, dict2):
    return dict1 | dict2

# example call
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dictionaries(a, b))   # {'x': 1, 'y': 3, 'z': 4}


# return sum of elements
def sum_of_elements(numbers):
    return sum(numbers)
print(sum_of_elements([5, 3, 9]))


# modify the list
def multiply_by_two(numbers):
    return [n * 2 for n in numbers]
print(multiply_by_two([5, 3, 9]))


# return union of sets
def get_union_sum(set1, set2):
    return sum(set1 | set2)
print(get_union_sum({2, 5, 7}, {5, 9, 2}))

# return second largest
def second_largest(numbers):
    uniq = sorted(set(numbers), reverse=True)
    return uniq[1] if len(uniq) > 1 else None
print(second_largest([3, 8, 99, 12, 21]))


# return True if the list is sorted
def is_sorted(numbers):
    return numbers == sorted(numbers)
print(is_sorted([1, 2, 3, 4]))
print(is_sorted([1, 3, 6, 4]))

# ------count the arguments
def count_arguments(*args):
    return len(args)

print(count_arguments())
print(count_arguments(35, 14))


# create 5 sublists
def create_sublists(n):
    my_list = [n]
    return [my_list] * 5
print(create_sublists("*"))
print(create_sublists(9))


# check datatype of input
def check_datatype(input):
    return type(input)
print(check_datatype(""))
print(check_datatype(1))


# number of trips:
def number_of_trips(seats):
    return 12 // seats
print(number_of_trips(3))



def identical_items(set1, set2):
    return set1 & set2

print(identical_items({1, 2, 3}, {2, 3, 4}))


def reverse_number(n):
    return float(str(n)[::-1])

print(reverse_number(123.45))
print(reverse_number(12.71))

# check if the letters are in order
def is_in_order(s):
    return list(s) == sorted(s)

print(is_in_order("abc"))
print(is_in_order("book"))


# calculate nth trianular number
def triangular_number(n):
    return n * (n + 1) // 2

print(triangular_number(5))

# or
def triangular_number_2(n):
    return sum(range(1, n + 1))

print(triangular_number_2(5))

# evaluate expresion as string
def evaluate_expression(expression):
    return eval(expression)

print(evaluate_expression("3 + 5 * 2"))
print(evaluate_expression("2 + 3 * 4 - 5"))


# ternary
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(check_even_odd(7))

# return Up or down 
def up_down(n):
    return "Up" if n > 0 else "Down" if n < 0 else "Zero"

print(up_down(2))
print(up_down(0))
print(up_down(-21))


# reverse a number
def reverse_number(n):
    return int(str(n)[::-1])
print(reverse_number(3245))

# print the largest from each list
def find_largest(lists):
    return [max(lst) for lst in lists]

print(find_largest([[1, 3, 1, 4], [3, 1, 5], [1, 7, 2, 9]]))
print(find_largest([[1, 3, 6, 4], [3, 1, 5], [1, 17, 2, 9]]))

# print the smallest from each list
def find_smallest(lists):
        return [min(lst) for lst in lists]
print(find_smallest([[1, 3, 1, 4], [3, 1, 5], [0, 7, 2, 9]]))

# count occurances in a tuple
def count_occurrences(item, tup):
    return tup.count(item)

print(count_occurrences(2, (1, 2, 3, 2, 4)))
print(count_occurrences("tea", ("tea", "tea", "coffee", "tea", "cola")))


# ---------Less Easy--------


# how many tallest candles
def tallest_candles(candles):
    return candles.count(max(candles))

print(tallest_candles([2, 4, 1, 3, 4]))
print(tallest_candles([2, 41, 1, 41, 3, 41]))



# return max from 2 numbers, either + or *
def max_value(s):
    a, b = map(int, s.split())
    return max(a + b, a * b)

print(max_value('3 4'))

# find the first letter, that occurs once
def single_occurrence(s):
    s = s.lower()
    for ch in s:
        if s.count(ch) == 1:
            return ch

print(single_occurrence("Hey guys, stay here"))


def replace_item(lst, old_item, new_item):
    return [new_item if x == old_item else x for x in lst]

print(replace_item([1, 2, 3, 2], 2, 9))
print(replace_item(["apples", "kiwi", "oranges"], "kiwi", "watermelon"))


# two identical letters
def has_consecutive_letters(s):
    return any(s[i] == s[i+1] for i in range(len(s)-1))

print(has_consecutive_letters("hello"))


# return the shortest word
def shortest_word(sentence):
    return min(sentence.split(), key=len)
# or max

print(shortest_word("The quick brown fox"))


# find the largest swap
def largest_swap(num):
    return max(num, int(str(num)[::-1]))

print(largest_swap(27))

# -----sum of digits
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total
print(sum_of_digits(9102821))

# or
def sum_of_digits_2(n):
    return sum(int(d) for d in str(abs(n)))
print(sum_of_digits_2(21345))
# print(sum_of_digits_2("33"))???



# ----check if a number is both a perfect square and a perfect cube
def is_cubic_square(n):
    if n < 0:
        return False  
    root = round(n ** (1 / 6))  # sixth-root gives integer if n is both square & cube
    return root ** 6 == n

print(is_cubic_square(64))   # True  (8² and 4³)
print(is_cubic_square(729))  # True  (27² and 9³)
print(is_cubic_square(50))   # False


# ----check if a number is both a perfect square and a perfect cube
def is_cubic_square(n: int) -> bool:
    if n < 0:                 
        return False
    root = round(n ** (1/6))
    # round-trip test to avoid fp rounding error
    return root ** 6 == n

print(is_cubic_square(50))   
print(is_cubic_square(64))  
print(is_cubic_square(729))  

# ----check if a letter is in a string
def check_letter(string, letter):
    if string.find(letter) != -1:
        return True
    else:
        return False
print(check_letter("hello", "e"))
print(check_letter("world", "a"))


# ----find the largest number in a list
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(find_largest([3, 5, 2, 8, 1]))

# ----sum all items in a list
def add_items(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(add_items([1, 2, 3, 4, 5]))


# ----convert number to reversed list of digits
def number_to_reversed_list(n):
     return [int(d) for d in str(abs(n))[::-1]]
print(number_to_reversed_list(12345))

# ----get day of the week from number
def day_of_week(n):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[n - 1] if 1 <= n <= 7 else "Invalid"
print(day_of_week(3))

# ----remove vowels from a string
def remove_vowels(string):
    vowels = set("aeiouAEIOU")
    return ''.join(ch for ch in string if ch not in vowels)
print(remove_vowels("Hello World"))  # Hll Wrld


# ---copy specific elements from a tuple based on given indices
def copy_elements(original_tuple, indices):
    return tuple(original_tuple[i] for i in indices)
print(copy_elements((10, 20, 30, 40, 50), [0, 2, 4])) 


# ----find the most common character in a string
def most_common_character(s):
    from collections import Counter
    if not s:
        return None
    counter = Counter(s)
    most_common = counter.most_common(1)[0][0]
    return most_common
print(most_common_character("hello world"))

# -----count paramters
def count_parameters(*args, **kwargs):
    return len(args) + len(kwargs)

print(count_parameters("A", "B", "C", "D", 12)) 

# or
def count_parameters_2(*args, **kwargs):
    return len(args) + len(kwargs)

print(count_parameters_2("A", "B", "C", "D", 12, x=99, y=42, mode="fast"))


# -----second largest
def second_largest(numbers):
    uniq = sorted(set(numbers), reverse=True)
    return uniq[1] if len(uniq) > 1 else None
print(second_largest([3, 5, 8, 12, 11]))


# -----the first -last index
def first_last_index(lst, n):
    return (lst.index(n), len(lst) - 1 - lst[::-1].index(n)) if n in lst else (None, None)

print(first_last_index([3, 7, 2, 12, 77, 4, 2, 33, 12, 33], 2))

# return first n vowels
def first_n_vowels(string, n):
    v = [c for c in string if c.lower() in 'aeiou'][:n]
    return v if v else "Not found"
print(first_n_vowels("I have a car in the garage", 5))


