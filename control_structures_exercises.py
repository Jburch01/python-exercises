# 1.
# A.
# day_of_week = input("What day is it today? ")
#
# if day_of_week == 'monday':
#     print("It is Monday")
# else: print("Nope not Monday")
#
# # B.
# weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
# if day_of_week in weekdays:
#     print("its a weekday")
# else: print("it's the weekend!")

# C.
# weekly_hours_worked = 41
# amount_paid_hourly = 29
# over_time_hours = weekly_hours_worked - 40
# over_time_pay = amount_paid_hourly + amount_paid_hourly / 2
#
#
#
# if weekly_hours_worked <= 40:
#     week_total_amount = weekly_hours_worked * amount_paid_hourly
# elif weekly_hours_worked > 40:
#     week_total_amount = (weekly_hours_worked - over_time_hours) * amount_paid_hourly + over_time_pay
#
# print(week_total_amount)

# 2.
    # A.
i = 5
# while i < 16:
#     print(i)
#     i += 1
#
# a = 0
# while a < 102:
#     print(a)
#     a += 2
#
# b = 100
# while b > -15:
#     print(b)
#     b -= 5

# c = 2
# while c < 1000000:
#     print(c)
#     c**=2

# d = 100
# while d >= 5:
#     print(d)
#     d -= 5

# B. FOUR LOOPS

#1.
# user_num = int(input("input a number "))
# for num in range(10):
#     print(f"{user_num} * {num + 1} = {user_num * (num + 1)}")

#2.
# for num in range(1, 10):
#     print(str(num) * num)

# C Breaks and continue
#1.

# user_pos_num = int(input("type positive number "))
# for num in range(user_pos_num):
#     print(user_pos_num)
#     user_pos_num -= 1
#     if user_pos_num == 0:
#         break

# 2.
# user_number = int(input("type a number "))
#
# for num in range(user_number + 1):
#     print(num)

#3.
# user_odd_num = input("type an odd number less than 50 ")
# if not user_odd_num.isdigit():
#     print("Not a number!!")
# elif int(user_odd_num) > 50:
#     print("Can you not read?? PICK A NUMBER LESS THAN 50!!")
# elif int(user_odd_num) % 2 == 0:
#     print("this is an even number!! I said type an ODD number!")
# else:
#     for num in range(1, 50):
#         if num == int(user_odd_num):
#             print(f"Yikes! skiping number: {user_odd_num}")
#             continue
#         if num % 2 != 0:
#             print(num)

#3. FIZZ BUZZ

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FIZZBUZZ")
#     elif num % 3 == 0:
#         print("FIZZ")
#     elif num % 5 == 0:
#         print("BUZZ")
#     else: print(num)


#4. Display Table of Powers

#5. LETTER GRADES
# get_letter_grade = True
#
# while get_letter_grade:
#     your_grade = int(input("Put in your number for letter grade "))
#     if your_grade >= 88:
#         print("A")
#     elif your_grade <= 87 and your_grade >= 80:
#         print('B')
#     elif your_grade <= 79 and your_grade >= 67:
#         print("C")
#     elif your_grade <= 66 and your_grade >= 60:
#         print("D")
#     else: print("F")
#     quit = input("Would you like to continue? Type 'y' or 'n' ")
#     if quit == "n":
#         get_letter_grade = False

#6. DICTIONARIES

def create_book_dict(T, A, G):
    return dict(Title = T, Author = A, Genre = G)


Harry_Potter = create_book_dict("Harry Potter And The Sorcerer's Stone", "JK Rowling", "Fantasy")
The_Hunger_Games = create_book_dict("The Hunger Games", "Suzanne Collins", "Post Apocalypse")
Gregor_the_Overlander = create_book_dict("Gregor The Overlander", "Suzanne Collins", "Fantasy")

book_list = []
book_list.append(Harry_Potter)
book_list.append(The_Hunger_Games)
book_list.append(Gregor_the_Overlander)

for book in book_list:
    print(book)

genre = input("The genre's I've read are  Fantasy, Post Apocalypse' choose a genre. ")
for book in book_list:
    if genre != book["Genre"]:
        pass
    elif genre == book["Genre"]:
        print(book["Title"])

    else: print("sorry I haven't read that genre")


