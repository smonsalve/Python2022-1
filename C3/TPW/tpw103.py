# Exercise 103: Magic Dates
# A magic date is a date where the day multiplied by the month is equal to the two digit year. 
# For example, June 10, 1960 is a magic date because June is the sixth month, and 6 times 10 is 60, which is equal to the two digit year.
# Write a function that determines whether or not a date is a magic date. 
# Use your function to create a main program that finds and displays all of the magic dates in the 20th century. You will probably
# find your solution to Exercise 100 helpful when completing this exercise.

from datetime import datetime


def magic_date(fecha):
    d = int(str(fecha.date))
    m = int(str(fecha.month))

    print(d*m)
    #print(str(fecha.year)[2:])
    #return True if(int(fecha.date)*int(fecha.month) == int(str(fecha.year)[2:])) else False


if __name__ == "__main__":

    date1 = datetime(1986,6,10)
    date2 = datetime(1960,6,10)


    print(date1, magic_date(date1)) 
    print(date2, magic_date(date2)) 