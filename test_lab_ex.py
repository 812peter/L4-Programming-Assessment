import pytest
from assessed_lab_exercises import *

### ex 1
def test_calculator():
    assert calculator("qwe", 0, "+") ==  "Error: invalid input."
    assert calculator([], None, "") ==  "Error: invalid input."
    assert calculator(0, 0, "$") ==  "Error: invalid operator."
    assert calculator(0, 0, "+") ==  0
    assert calculator(-100000, 0.000001, "+") == -99999.999999
    assert calculator(10, 5, "-") == 5
    assert calculator(5, -5, "-") == 10
    assert calculator(5, -5, "*") == -25
    assert calculator(-5, -5, "*") == 25
    assert calculator(5, 0, "*") == 0
    assert calculator(5, 0, "/") == "Error: division by 0 is not allowed."
    assert calculator(5, 5, "/") == 1
    assert calculator(5, 4, "%") == 1
    assert calculator(2, 4, ">") == False
    assert calculator(2, 3, ">=") == False
    assert calculator(2, 4, "<") == True
    assert calculator(2, 2, "<") == False
    assert calculator(2, 2, "<=") == True

### ex 2
def test_max_of_three():
    assert max_of_three("qwe", 20, 30) == "Error: invalid input."
    assert max_of_three(10, 10, 30) == 30
    assert max_of_three(10, 10, 10) == 10
    assert max_of_three(-10, -20, -20) == -10

### ex 3
def test_winning_numbers():
    assert winning_numbers([5, 14, 17], [5, 14, 6]) == "Second."
    assert winning_numbers([1, 2, 3], [1, 2, 3]) == "First."
    assert winning_numbers([4, 7, 9], [0, 7, 2]) == "Third."
    assert winning_numbers([10, 20, 30], [1, 2, 3]) == "No."
    assert winning_numbers([10, 20, 30], [10, 10, 10]) == "Error: invalid amount of inputs or used duplicates."
    assert winning_numbers([[], 20, 30], ["qwe", 2, 3]) == "Error: only integers must be used."

### ex 4
def test_sum_of_evens():
    assert sum_of_evens("qwe", 20) == "Error: inputs must be integers."
    assert sum_of_evens(12, -20) == "Error: inputs must be positive."
    assert sum_of_evens(12, 21) == 80
    assert sum_of_evens(21, 12) == 80

### ex 5
def test_calculate_average():
    assert calculate_average([]) == "Error: empty list."
    assert calculate_average(["qwe", 2, 3]) == "Error: only numbers must be entered."
    assert calculate_average([1]) == 1
    assert calculate_average([1, 4, 5, 6]) == 4
    assert calculate_average([1, 1.5, 2]) == 2

### ex 6
def test_calculate_weekly_pay():
    assert calculate_weekly_pay("qwe") == "Error: input should be a positive integer."
    assert calculate_weekly_pay(0) == "Error: input should be a positive integer."
    assert calculate_weekly_pay(-1) == "Error: input should be a positive integer."
    assert calculate_weekly_pay(30) == 360
    assert calculate_weekly_pay(36) == 438

### ex 7
def test_is_prime():
    assert is_prime(0) == "Error: input should be a positive integer."
    assert is_prime(-1) == "Error: input should be a positive integer."
    assert is_prime(1) == False
    assert is_prime(21) == False
    assert is_prime(5) == True

### ex 8
def test_are_anagrams():
    assert are_anagrams("", "EARTH") == "Error: input cannot be empty."
    assert are_anagrams(1, "EARTH") == "Error: input should only contain letters."
    assert are_anagrams("HEART", "earth") == True
    assert are_anagrams("help", "self") == False

### ex 9
def test_count_vowels():
    assert count_vowels("") == "Error: input cannot be empty."
    assert count_vowels(1) == 0
    assert count_vowels("Hello World") == 3
    assert count_vowels("Are you okay?") == 6

### ex 10
def test_sort_list():
    assert sort_list(1) == "Error: input should be a list."
    assert sort_list([]) == "Error: list cannot be empty."
    assert sort_list(["qwe", 2, 3]) == "Error: a list of numbers must be used."
    assert sort_list([5, 6, 9, 0]) == [0, 5, 6, 9]
    assert sort_list([1.2, 2, 1]) == [1, 1.2, 2]
    assert sort_list([-1, 9, -10]) == [-10, -1, 9]

### ex 11
def test_sum_of_digits():
    assert sum_of_digits("qwe") == "Error: input should be a positive integer."
    assert sum_of_digits(-1) == "Error: input should be a positive integer."
    assert sum_of_digits(1.2) == "Error: input should be a positive integer."
    assert sum_of_digits(0) == 0
    assert sum_of_digits(123) == 6

### ex 12
def test_is_palindrome():
    assert is_palindrome(123) == False
    assert is_palindrome("Radar") == True
    assert is_palindrome("python") == False

### ex 13
def test_password_strength():
    assert password_strength("") == "Error: password cannot be empty."
    assert password_strength("abc") == "Weak password."
    assert password_strength(123) == "Weak password."
    assert password_strength("Abc@12") == "Medium password."
    assert password_strength("MyPass$2025") == "Strong password."

### ex 14
def test_letter_grade():
    data_input = [
        {"subject": "Math", "score": 90, "credits": 40},
        {"subject": "History", "score": 75, "credits": 20},
        {"subject": "English", "score": 60, "credits": 20},
        {"subject": "Science", "score": 85, "credits": 40},
        {"subject": "Art", "score": 50, "credits": 40}
    ]
    assert letter_grade({}) == "Error: input cannot be empty."
    assert letter_grade(data_input) == (73.125, "B")

    data_input[0]["score"] = -1
    assert letter_grade(data_input) == "Error: score needs to be between 0 and 100."

    data_input = [
        {"subject": "Math", "score": 90, "credits": 0},
        {"subject": "History", "score": 75, "credits": 0}
    ]
    assert letter_grade(data_input) == "Error: total credits cannot be zero."
    
### ex 15
def test_maximum_gap():
    assert maximum_gap("qwe", [1, 2]) == "Error: enter two lists of integers."
    assert maximum_gap([], [1, 2]) == "Error: enter two lists of integers."
    assert maximum_gap([1, 2.2], [1, 2]) == "Error: enter two lists of integers."
    assert maximum_gap([1, 5, 600], [100, 7, 3, 29, 39]) == 597
    assert maximum_gap([1, 5, 600], [100, 7, 3, 602, 39]) == 601

### ex 16
def test_cipher_text():
    cipher = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$"
    key = 3
    assert cipher_text(cipher, key) == "Each error you make in programming is an opportunity to become a better developer!"
    key += 256
    assert cipher_text(cipher, key) == "Each error you make in programming is an opportunity to become a better developer!"
    assert cipher_text(cipher, 0) == "Error: key should be a positive integer."
    assert cipher_text(cipher, "qwe") == "Error: key should be a positive integer."

### ex 17
def test_net_annual_income():
    assert net_annual_income(-1) == "Error: input should be a positive number."
    assert net_annual_income(0) == "Error: input should be a positive number."
    assert net_annual_income(60000) == 48568

### ex 18
def test_my_split():
    assert my_split("apple,banana,orange", ",") == ["apple", "banana", "orange"]
    assert my_split("apple banana orange", " ") == ["apple", "banana", "orange"]

### ex 19
def test_longest_repetition():
    assert longest_repetition("") == ("", 0)
    assert longest_repetition(123) == ("1", 1)
    assert longest_repetition("abc") == ("a", 1)
    assert longest_repetition("aaabbcaaa") == ("a", 3)
    assert longest_repetition("hellooooo") == ("o", 5)

### ex 20
def test_closest_pair_under_budget():
    items = [("tv", 300), ("mobile phone", 800), ("laptop", 600), ("headphones", 200)]
    budget = 1000
    assert closest_pair_under_budget(items, budget) == ["mobile phone", "headphones"]
    assert closest_pair_under_budget(items, 400) == None
    assert closest_pair_under_budget([], budget) == "Error: input cannot be empty."
    assert closest_pair_under_budget(items, -10) == "Error: budget must be a positive number."
    assert closest_pair_under_budget(("tv", 300), budget) == "Error: items must be presented in a list."
    assert closest_pair_under_budget([("tv", -10), ("mobile phone", 800)], budget) == "Error: price should be a positive number."
    assert closest_pair_under_budget([["tv", -10], ("mobile phone", 800)], budget) == "Error: invalid list of items."


pytest.main()