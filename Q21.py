date = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    days_in_month[1] = 29

if date < days_in_month[month-1]:
    date += 1
else:
    date = 1
    month += 1

    if month > 12:
        month = 1
        year += 1

print("Next date is:", date, "/", month, "/", year)
