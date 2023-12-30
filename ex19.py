month_code = {
    1:1,
    2:4,
    3:4,
    4:0,
    5:2,
    6:5,
    7:0,
    8:3,
    9:6,
    10:1,
    11:4,
    12:6
}
# this algorithm is based on a method I know to calculate the day of the week
# the method is explained here: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
month = 1
year = 1901
count = 0
day_of_week = 1
while year < 2_001:
    if year < 2_000:
        day_of_week = (1 + month_code[month] + (year % 100) + ((year % 100) // 4)) % 7
    else:
        day_of_week = (1 + 6 + month_code[month] + (year % 100) + ((year % 100) // 4)) % 7
    if (month == 1 or month == 2) and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        day_of_week = (day_of_week - 1) % 7
    if day_of_week == 1:
        print(f"day: 1, month: {month}, year: {year}")
        count += 1
    month += 1
    if month == 13:
        month = 1
        year += 1
print(count)