#program that determines whether a year entered by the user is a lesp year Or not using ifelifelse statement. 

year = int(input("Enter year:"))

if year % 4 == 0 and year % 100 ! = 0:
print(year, "Is a leap year")
elif year % 100 == 0:
print(year, " is not a leap year")
elif year % 400 == 0:
print(year, "Is a leap year")
else:
print(year, " is not a leap year")