# Scriptism – Simple

# Math & List Snippets

A no-dependency collection of tiny, copy-paste-ready Python helpers for everyday math, string and list tasks.

---

## Quick-start
```python
from snippets import *
print(cube_number(4))            # 64
print(sum_of_evens([1,2,3,4]))   # 6

| Topic                | Functions                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basic math**       | `cube_number`, `find_square_root`, `calculate_power`, `simple_interest`, `calculate_profit_loss`, `time_saved`, `power_of_two`, `calculate_hypotenuse`, `sum_of_digits`, `is_cubic_square`                                                                                                                                      |
| **Lists & tuples**   | `sum_of_evens`, `eliminate_odd_numbers`, `second_largest`, `is_sorted`, `find_largest`, `add_items`, `sum_of_squares`, `multiply_by_two`, `sum_greater_than`, `create_sublists`, `copy_elements`, `filter_integers`, `replace_item`, `sum_of_min_values`, `find_largest`, `tallest_candles`, `fruit_salad`, `concatenate_lists` |
| **Sets & dicts**     | `identical_items`, `symmetric_difference`, `is_subset`, `merge_dictionaries`, `is_empty`, `key_exists`                                                                                                                                                                                                                          |
| **Strings**          | `reverse_string`, `remove_vowels`, `most_common_character`, `first_n_vowels`, `has_spaces`, `check_letter`, `convert_to_titlecase`, `string_to_list`, `repeat_last_char`, `replace_smiley`, `shortest_word`, `single_occurrence`, `has_consecutive_letters`, `is_in_order`                                                      |
| **Numbers & digits** | `reverse_number`, `largest_swap`, `last_digit`, `triangular_number`, `number_to_reversed_list`, `check_even_odd`, `up_down`                                                                                                                                                                                                     |
| **Utilities**        | `evaluate_expression`, `count_arguments`, `count_parameters`, `check_datatype`, `day_of_week`, `swap_values`, `add_numbers`, `add_numbers2`, `pin_extractor`                                                                                                                                                                    |


cube_number(n)                     # n ** 3
find_square_root(n)                # math.sqrt(n)
calculate_power(base, exponent)    # base ** exponent
simple_interest(p, r, t)           # (p*r*t)/100
calculate_profit_loss(cp, sp)      # "Profit: x" or "Loss: x"
time_saved(d, s1, s2)              # hours saved when speed increases
power_of_two(n)                    # 2^n
calculate_hypotenuse(a, b)         # math.hypot(a, b)
sum_of_digits(n)                   # cross-sum of absolute digits
is_cubic_square(n)                 # True if n is both perfect square & cube

sum_of_evens(nums)                 # ∑ even numbers
eliminate_odd_numbers(nums)        # list without odds
second_largest(nums)               # 2nd biggest unique value
is_sorted(nums)                    # True if ascending
find_largest(nums)                 # max element
add_items(nums)                    # ∑ all items
sum_of_squares(nums)               # ∑ n²
multiply_by_two(nums)              # [n*2 ...]
sum_greater_than(nums, n)          # ∑ items > n
create_sublists(item)              # [[item]] * 5
copy_elements(tup, indices)        # tuple with picked indices
filter_integers(mixed)             # ints only
replace_item(lst, old, new)        # new replaces old
sum_of_min_values(nested)          # ∑ min of each sub-list
tallest_candles(candles)           # how many max values
fruit_salad(a, b)                  # concat two lists
concatenate_lists(a, b)            # a + b

identical_items(a, b)              # set intersection
symmetric_difference(a, b)         # elements in exactly one set
is_subset(a, b)                    # True if a ⊆ b
merge_dictionaries(d1, d2)         # d1 | d2 (Py 3.9+)
is_empty(d)                        # len(d) == 0
key_exists(d, k)                   # k in d

reverse_string(s)                  # s[::-1]
remove_vowels(s)                   # string without a e i o u
most_common_character(s)           # highest freq char
first_n_vowels(s, n)               # first n vowels or "Not found"
has_spaces(s)                      # ' ' in s
check_letter(s, ch)                # True if ch in s
convert_to_titlecase(s)            # s.title()
string_to_list(s)                  # s.split()
repeat_last_char(s, n)             # s + last*n
replace_smiley(text)               # ":)" → "😊"
shortest_word(sentence)            # min(word, key=len)
single_occurrence(s)               # first unique letter
has_consecutive_letters(s)         # True if any double letter
is_in_order(s)                     # letters non-decreasing

reverse_number(n)                  # int(str(n)[::-1])
largest_swap(num)                  # max(num, reversed)
last_digit(n)                      # abs(n) % 10
triangular_number(n)               # n(n+1)/2
number_to_reversed_list(n)         # [int(d) for d in str(abs(n))[::-1]]
check_even_odd(n)                  # "Even" / "Odd"
up_down(n)                         # "Up" / "Down" / "Zero"

evaluate_expression(expr)          # safe eval to number
count_arguments(*args)             # len(args)
count_parameters(*args, **kwargs)  # len(args) + len(kwargs)
check_datatype(obj)                # type(obj)
day_of_week(n)                     # Monday…Sunday for 1…7
swap_values(a, b)                  # (b, a)
add_numbers(n1, n2)                # str(n1)+str(n2)+str(n1+n2)
add_numbers2(n1, n2)               # same, but returns 0 if sum == 0
pin_extractor(poems)               # list of numeric codes per poem


License
Public domain – do whatever you want.


```bash
python main.py
```
