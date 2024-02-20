import datetime

x=datetime.datetime.now()
# print(x)
# print(x.year)

# use the datetime() class constructor of the datetime module.

# you can pass 3 parameter y:m:d

# y=datetime.datetime(2003,3,1)
# print(y)

y=datetime.datetime.now()

# strftime() method

print(y.strftime("%B"))
print("Weekday, short version ",y.strftime("%a"))
print("Weekday, full version ",y.strftime("%A"))
print("Weekday as a number 0-6, 0 is Sunday ",y.strftime("%w"))
print("Day of month 01-31 ",y.strftime("%d"))
print("Month name, short version ",y.strftime("%b"))
print("Month as a number 01-12 ",y.strftime("%m"))
print("Year, short version, without century ",y.strftime("%y"))
print("Year, full version ",y.strftime("%Y"))
print("Hour 00-23 ",y.strftime("%H"))
print("Hour 00-12",y.strftime("%I"))
print("AM/PM ",y.strftime("%p"))
print("Minute 00-59 ",y.strftime("%M"))
print("Second 00-59 ",y.strftime("%S"))
print("Microsecond 000000-999999 ",y.strftime("%f"))
print("UTC offset ",y.strftime("%z"))
print("Timezone ",y.strftime("%Z"))