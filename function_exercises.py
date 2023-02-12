1.
def is_two(num):
    return num == 2 or num == '2'


# number = is_two('2')
# print(number)


#2.
import re
def is_vowel(letter):
    if re.search("[aeiouAEIOU]", letter):
        return True
    else:
        return False

# x = is_vowel("U")
# print(x)

#3.


def is_consonant(letter):
    return not is_vowel(letter)


# x = is_consonant("t")
# print(x)

#4.

def cap_const_word(string):
    if not is_vowel(string[0]):
        return string.capitalize()
    else:
        return string


# x = cap_const_word("animal")
# y = cap_const_word("letter")
# print(x, y)

#5.

def calculate_tip(tip_percent, bill):
    '''Returns bill plus tip as a float. positional tip percent first then bill'''
    return round((bill * tip_percent + bill), 2)


# bill_plus_tip = calculate_tip(0.18, 45.67)
# print(bill_plus_tip)

#6

def apply_discount(orginal_price, percent_off):
    '''calculates price after discount. Put discount arg as float'''
    discount = orginal_price * percent_off
    return round(orginal_price - discount, 2)

# total_after_discount = apply_discount(167.99, 0.40)
# print(total_after_discount)

#7

def handle_commas(string):
    x = re.sub("\,", "", string)
    return x

# number = handle_commas("1,000,000")
# print(number)

#8

def get_letter_grade(grade):
    if grade >= 88:
        return("A")
    elif grade >= 80:
        return('B')
    elif grade >= 67:
        return("C")
    elif grade >= 60:
        return("D")
    else:
        return("F")

# letter_grade = get_letter_grade(61)
# print(letter_grade)

#9

def remove_vowels(string):
    vowels = re.findall("[aeiouAEIOU]", string)
    for letter in string:
        if letter in vowels:
            string = string.replace(letter, '')
    return string

# no_vowels = remove_vowels("AnImal")
# print(no_vowels)

#10

def normalize_name(string):
    special_characters = ['@', '#', '$', '*', '&', '%']
    for char in string:
        if char in special_characters:
            string = string.replace(char, '')
    string = string.lower()
    string = string.strip()
    string = string.replace(" ", "_")
    return string


# example_string = normalize_name("$2,097.02")
# print(example_string)



#11

def cumulitive_list(list):
    a = 0
    new_list = []
    for num in list:
        a += num
        new_list.append(a)
    return new_list


# sample_list = cumulitive_list([1, 2, 3, 4])
# print(sample_list)

