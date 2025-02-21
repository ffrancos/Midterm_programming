#Question number 1
a = 16

a = a // 2

print(a**2)

a = a + 11

print(a+1)

a = a - 3
print(a)
#Question number 2
print((2+3)*6/2 and 18.0)

#Question number 3
import datetime
a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
print(a)
print(b)
c=a+b
d = "xyz" * (c//3)
print(d)
#Question number 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome("9847255590886266818998186626880955527489"))
print(palindrome("1414884937242655719669145562427394884141"))
6800923757255865070000705685527573290086
print(palindrome("6800923757255865070000705685527573290086"))
print(palindrome("6892149109325320763773670235239019412986"))

#Question number 5
import sys
import string

def matches_of_un_an(name_of_file):
    """
    :param name_of_file: the name of the file of text
    :return: number of words where 'un' is followed by 'an'
    """
    count = 0

    with open(name_of_file, "r" ) as f:
        for line in f:

            for p in string.punctuation:
                line = line.replace(p, " ")

            words = line.split()

            for word in words:
                i = 0

                while i < len(word) - 1:
                    if word[i:i + 2] == "un":
                        j = i + 2

                        while j < len(word) - 1:
                            if word[j:j + 2] == "an":
                                count += 1
                                break
                            j += 1
                    i += 1

    return count
#Question number 6
my_list = [1, 2, 3]
my_list[2]=5
print(my_list)
my_string="hello world"
print(my_string)
#my_string[0]="bye"
#print(my_string)
#Question number 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
i=len(random_numbers)-1
while i>0:
    if random_numbers[i]%2!=0:
        random_numbers.pop(i)
    else:
        random_numbers[i]*=2

    i-=1
print(random_numbers)
#Question number 8
url=input("Please give me an url")# ASKS THE USER FOR A URL
def is_the_url_valid(url):
    valid = False #ASSUMES THAT THE URL IS INVALID
    if url.startswith("http://") or url.startswith("https://"):#CHECKS THE START
        if "." in url and " " not in url: #AN URL CAN'T HAVE SPACES'
            parts = url.split(".")
            if len(parts[-1]) > 0:
                valid = True
    return valid

if is_the_url_valid(url):  # Call the function and check its return value
    print(f"{url} IS VALID")
else:
    print(f"{url} IS NOT VALID")
#Question number 9
def days_since_birth(birthday):
    day, month, year = birthday.split("-") #SPLITS IT INTO FORMAT
    birth_year = int(year)  # CONVERTS IT INTO INTEGER

    #
    today_year = 2025

    # We only count full years: 2005 to 2024
    start_year = birth_year + 1  # 2005
    end_year = today_year - 1  # 2024

    total_days = 0

   #SEARCH FOR EVERY YEAR
    for year in range(start_year, end_year + 1):
        # FINDS LEAP YEAR
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    return total_days
#Question number 10