print()

### ex 1
def calculator(num1, num2, operator):
    try: # check if inputs are float
        num1 = float(num1)
        num2 = float(num2)
    except:
        return "Error: invalid input."

    if operator == "+": # cases for each allowed operation
        return num1 + num2 
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: division by 0 is not allowed."
    elif operator == "%":
        return num1 % num2
    elif operator == ">":
        return num1 > num2
    elif operator == ">=":
        return num1 >= num2
    elif operator == "<":
        return num1 < num2
    elif operator == "<=":
        return num1 <= num2
    else:
        return "Error: invalid operator."


### ex 2
def max_of_three(num1, num2, num3):
    try: # check if inputs are float
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
    except:
        return "Error: invalid input."
    
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3      
    return max_num


### ex 3
def winning_numbers(winning_list, guessed_list):
    for num in winning_list: # check if inputs are int
        if type(num) != int:
            return "Error: only integers must be used."
    for num in guessed_list:
        if type(num) != int:
            return "Error: only integers must be used."

    winning_set = set(winning_list) # check if 3 ints per list and if there are any duplicates
    guessed_set = set(guessed_list)
    if len(winning_set) != 3 or len(guessed_set) != 3:
        return "Error: invalid amount of inputs or used duplicates."

    right_guesses = 0
    if guessed_list[0] in winning_list:
        right_guesses += 1
    if guessed_list[1] in winning_list:
        right_guesses += 1
    if guessed_list[2] in winning_list:
        right_guesses += 1

    if right_guesses == 1:
        return "Third."
    elif right_guesses == 2:
        return "Second."
    elif right_guesses == 3:
        return "First."
    else:
        return "No."


### ex 4
def sum_of_evens(min_num, max_num):
    if type(min_num) != int or type(max_num) != int: # check if inputs are int
        return "Error: inputs must be integers."

    if min_num <= 0 or max_num <= 0: # check if inputs are positive (0 isnt positive)
        return "Error: inputs must be positive."

    if max_num < min_num: # swap inputs if mistake was made while entering parameters, 
                          # and the greater integer was entered first
        temp = max_num
        max_num = min_num
        min_num = temp
        del temp # free up space

    sum = 0
    for num in range(min_num, max_num + 1): # "max_num + 1" as inclusive
        if num % 2 == 0: # check if even
            sum += num
    return sum


### ex 5
def calculate_average(numbers_list):
    # check if all inputs in a list are numbers;
    # floats are accepted, as exercise asked for "numbers", not "integers"
    if not numbers_list:
        return "Error: empty list."
    
    for num in numbers_list:
        if type(num) != int and type(num) != float:
            return "Error: only numbers must be entered."
        
    sum = 0
    count = 0
    for num in numbers_list:
        sum += num
        count += 1    

    return int(round((sum)/count, 0)) # rounding, not truncating


### ex 6
def calculate_weekly_pay(hours):
    if type(hours) != int or hours <= 0: # check if input is positive integer
        return "Error: input should be a positive integer."

    regular_rate = 12
    overtime_rate = 18

    if hours <= 35:
        return hours * regular_rate
    else:
        overtime_hours = hours - 35
        hours = hours - overtime_hours
        return overtime_hours * overtime_rate + hours * regular_rate


### ex 7
def is_prime(num):
    if type(num) != int or num <= 0: # check if input is positive integer
        return "Error: input should be a positive integer."
    
    if num == 1: # 1 isnt prime
        return False
    
    count_of_factors = 0 
    for i in range (1, num + 1):
        if num % i == 0:
            count_of_factors += 1

    if count_of_factors == 2: # integer is prime if only 2 factors: 1 and itself
        return True
    else:
        return False


### ex 8
def are_anagrams(word1, word2):
    word1 = str(word1).lower(); word2 = str(word2).lower()

    if not word1 or not word2: # check if inputs are empty
        return "Error: input cannot be empty."

    word1_list, word2_list = [], []

    allowed_chrs = "abcdefghijklmnopqrstuvwxyz" # only allow these characters
    for chr in word1:
        if chr not in allowed_chrs:
            return "Error: input should only contain letters."
        word1_list.append(chr)
    for chr in word2:
        if chr not in allowed_chrs:
            return "Error: input should only contain letters."
        word2_list.append(chr)

    word1_list.sort(); word2_list.sort()
    
    if word1_list == word2_list:
        return True
    else:
        return False

    
### ex 9
def count_vowels(text):
    text = str(text).lower()

    if not text: # check if inputs are empty
        return "Error: input cannot be empty."
    
    vowels = "aeiou"
    count = 0

    for chr in text:
        if chr in vowels:
            count += 1
    
    return count
    
    
### ex 10
def sort_list(unsorted_list):

    try: # check if input is a list
        unsorted_list = list(unsorted_list)
    except:
        return "Error: input should be a list."
    
    if not unsorted_list: # check if list is empty
        return "Error: list cannot be empty."
    
    for num in unsorted_list: # check for invalid characters
        if type(num) != float and type(num) != int:
            return "Error: a list of numbers must be used."

    unsorted = True
    while unsorted: # bubble sort until sorted
        number_of_changes = 0

        for i in range(0, len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i+1]: # put greater numbers after smaller ones
                number_of_changes += 1
                temp = unsorted_list[i+1]
                unsorted_list[i+1] = unsorted_list[i]
                unsorted_list[i] = temp
                del temp # free up space
                
        if number_of_changes == 0: # sorted if no swaps
            unsorted = False
    
    sorted_list = unsorted_list
    return sorted_list

### ex 11
def sum_of_digits(num):
    try: # check if input is a positive integer
        num_int = int(num)
        if num_int < 0:
            return "Error: input should be a positive integer."
        
        sum_num = 0
        num = str(num)
        for digit in num:
            sum_num += int(digit)
        return sum_num
    except:
        return "Error: input should be a positive integer."

### ex 12
def is_palindrome(text):
    # no checking of input, as assuming string contains only letters and no spaces or punctuation
    text = str(text)
    return text.lower() == text.lower()[::-1]

### ex 13
def password_strength(password):
    if not password: # check if password is empty
        return "Error: password cannot be empty."
    
    password = str(password)
    password_len = len(password)
    special_chars, special_chars_used = "@$£", False
    count_uppercase = 0  

    for char in password: # check if any special characers and count how many uppercase letters
        if char in special_chars:
            special_chars_used = True
        else:
            if char == char.upper():
                count_uppercase += 1

    if password_len < 6 or not special_chars_used or count_uppercase == 0:
        return "Weak password."
    elif 6 <= password_len <= 10:
        return "Medium password." 
    else:
        return "Strong password." 

### ex 14
def letter_grade(input):
    numerator, denominator = 0, 0
    grade = ""

    try:
        if not input: # check if input empty
            raise ValueError("input cannot be empty")
        
        for item in input:
            if 0 <= item["score"] <= 100: # check if scores between 0 and 100
                numerator += item["score"] * item["credits"]
                denominator += item["credits"]
            else:
                raise ValueError("score needs to be between 0 and 100")

        if denominator == 0: # handle zero division error
            raise ValueError("total credits cannot be zero")

        average = numerator/denominator
        
        if average < 50:
            grade = "F"
        elif 50 <= average < 60:
            grade = "D" 
        elif 60 <= average < 70:
            grade = "C" 
        elif 70 <= average < 90:
            grade = "B" 
        else:
            grade = "A" 
        return (round(average, 4), grade)
    
    except Exception as e:
        return f"Error: {e}."

### ex 15
def maximum_gap(list1, list2):
    if type(list1) != list or type(list2) != list: # check if two inputs are lists
        return "Error: enter two lists of integers."
    
    if not list1 or not list2:
        return "Error: enter two lists of integers."
    
    max_gap = 0

    for num1 in list1: # check gap between every number in list1 & list2
        if type(num1) == int: # check if int
            for num2 in list2:
                if type(num2) == int: # check if int
                    if max_gap < abs(num1 - num2): # absolute as gap cannot be negative
                        max_gap = abs(num1 - num2) 
                else:
                    return "Error: enter two lists of integers."    
        else:
            return "Error: enter two lists of integers."  
        
    return max_gap

### ex 16
def cipher_text(encrypted_txt, key):
    if type(key) != int: # check if key is int
        return "Error: key should be a positive integer."
    if key <= 0: # check if key is positive
        return "Error: key should be a positive integer."
    
    encrypted_txt = str(encrypted_txt)
    decrypted_txt = ""
    for char in encrypted_txt:
        char = ord(char) # convert char to ascii
        char -= key
        char = char % 256 # keep it in valid ascii range
        char = chr(char) # convert back to char
        decrypted_txt += char

    return decrypted_txt

### ex 17
def net_annual_income(gross_salary):
    try: # check if input is a positive number
        gross_salary = float(gross_salary)
        if gross_salary <= 0:
            raise
    except:
        return "Error: input should be a positive number."
    
    gross_salary_copy = gross_salary # create a copy for later calculation of net income
    personal_allowance = 12570
    basic_rate_lim = 50270
    higher_rate_lim = 125140
    total_tax = 0

    if gross_salary > higher_rate_lim: # calculate tax for each portion
        total_tax += (gross_salary - higher_rate_lim) * 0.45
        gross_salary = higher_rate_lim
    
    if gross_salary > basic_rate_lim:
        total_tax += (gross_salary - basic_rate_lim) * 0.40
        gross_salary = basic_rate_lim

    if gross_salary > personal_allowance:
        total_tax += (gross_salary - personal_allowance) * 0.20
    
    return gross_salary_copy - total_tax

### ex 18
def my_split(s, sep):
    s, sep = str(s), str(sep)
    my_list = []
    temp = ""

    for char in s:
        if char != sep:
            temp += char
        else:
            my_list.append(temp)
            temp = ""
    
    my_list.append(temp) # append last item
    
    return my_list

### ex 19
def  longest_repetition(text):
    text = str(text)
    if not text: # check if input empty
        return ("", 0)

    repeated_char = text[0]
    max_char = text[0]
    count = 1
    max_count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_char = text[i - 1]
            count = 1  # reset counter

    if count > max_count: # check last sequence
        max_count = count
        max_char = text[-1]

    return (max_char, max_count)

### ex 20
def closest_pair_under_budget(prices, budget):
    if not prices or not budget: # check if inputs empty
        return "Error: input cannot be empty."

    try: # check if budget is positive number
        budget = float(budget)
        if budget <= 0:
            raise
    except:
        return "Error: budget must be a positive number."
    
    if type(prices) != list: # check if items in a list
        return "Error: items must be presented in a list."

    for item in prices: # check if prices are valid
        try: 
            if type(item) != tuple:
                raise

            if float(item[1]) <= 0:
                return "Error: price should be a positive number."
        except: 
            return "Error: invalid list of items."

    best_pair = None # to return None if no pair fits under budget
    best_sum = 0

    for i in range(len(prices)): # check each unique pair
        for j in range(i + 1, len(prices)):

            item1, price1 = prices[i] # extract name and price
            item2, price2 = prices[j]

            total = price1 + price2

            if total <= budget and total > best_sum:
                best_sum = total
                best_pair = [item1, item2]
    
    return best_pair



print()