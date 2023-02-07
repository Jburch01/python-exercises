# 5.
def build_movie(a):
    return dict(time_rented_days = a)


The_Little_Mermaid = build_movie(3)
Brother_Bear = build_movie(5)
Hercules = build_movie(1)

rented_movie_list =[The_Little_Mermaid, Brother_Bear, Hercules]
daily_fee = 3
total_days = 0
for movie in rented_movie_list:
   total_days += movie["time_rented_days"]

total_fee = total_days * daily_fee
print("5.", total_fee)

# 6.

def build_job(a):
   return dict(hourly_rate=a)

google = build_job(400)
Amazon = build_job(380)
Facebook = build_job(350)

google_hours = 6
Amazon_hours = 4
Facebook_hours = 10

google_total = google['hourly_rate'] * google_hours
Amazon_total = Amazon['hourly_rate'] * Amazon_hours
Facebook_total = Facebook['hourly_rate'] * Facebook_hours

weekly_total = google_total + Amazon_total + Facebook_total
print('6.', weekly_total)

# 7.
class_full = False
schedule_conflict = False

can_enroll = not class_full and not schedule_conflict
print(can_enroll)

# 8.
min_items = True
offer_exp = False
premium_member = True

can_get_promotional_offer = not offer_exp and min_items or premium_member
print(can_get_promotional_offer)


#9.
username = 'codeup'
password = 'notastrongpassword'

min_pass_len = len(username) >=5
max_username_len = len(password) <= 20
user_name_not_password = username != password
print(min_pass_len, max_username_len, user_name_not_password )
