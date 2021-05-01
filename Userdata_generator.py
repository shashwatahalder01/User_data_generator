import os
import sys
import pathlib

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.ExcelUtils import *
from randomuser import RandomUser
import re

user = RandomUser()

user_list = RandomUser.generate_users(100)
ll = [["First_name", "Last_name", "Email", "Phone_number", "Username", "Password"]]
for u in user_list:
    l = []
    if re.match(r'[\u0600-\u06FF]', u.get_first_name()):
        l.append(user.get_first_name())
        l.append(user.get_last_name())
    else:
        l.append(u.get_first_name())
        l.append(u.get_last_name())
    l.append(u.get_email())
    l.append(u.get_phone())
    l.append(u.get_username())
    l.append(u.get_password())
    ll.append(l)

# print(ll)
# print(tabulate(ll))


path = pathlib.Path(__file__).parent / "utils/a.xlsx"
writelistoflist(path, "userdata", ll)

# for u in user_list:
#     print(u.get_first_name())
#     print(u.get_last_name())
#     print(u.get_email())
#     print(u.get_phone())
#     print(u.get_username())
#     print(u.get_password())


# print(user.get_first_name())
# print(user.get_last_name())
# print(user.get_full_name())
# print(user.get_email())
# print(user.get_username())
# print(user.get_password())
# print(user.get_phone())
# print(user.get_gender())
# print(user.get_picture())
# print(user.get_id())
# print(user.get_id_number())
# print(user.get_id_type())
# print(user.get_info())
# print(user.get_login_md5())
# print(user.get_login_salt())
# print(user.get_login_sha1())
# print(user.get_login_sha256())
# print(user.get_nat())
# print(user.get_registered())
# print(user.get_cell())
# print(user.get_dob())
# print(user.get_city())
# print(user.get_state())
# print(user.get_street())
# print(user.get_postcode())
# print(user.get_zipcode())
