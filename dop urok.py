
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word.
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
def smash(words):
    return ' '.join(words)
print(smash(['che', 'to']))



# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

print(paperwork(34, 56))



# Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents.
# With so many passengers wanting to get aboard his bus
# he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.
# Task Overview:
# You have to write a function that accepts three parameters:
#     cap is the amount of people the bus can hold excluding the driver.
#     on is the number of people on the bus excluding the driver.
#     wait is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
def trolleybus(cap, on, wait):
     return max(0, - cap - (on - wait))

print(trolleybus(23, 4, 17))



def get_score(n1, n2, n3):
    score = n1 + n2 + n3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 70:
        return "B"
    elif 70 <= score <= 60:
        return "C"
    elif 60 <= score <= 50:
        return "D"
    else:
        return "F"



# You are going to make toast fast, you think that you should make multiple pieces of toasts and once.
# So, you try to make 6 pieces of toast.
# You forgot to count the number of toast you put into there, you don't know if you put exactly six pieces of toast into the toasters.
# Define a function that counts how many more (or less) pieces of toast you need in the toasters.
# Even though you need more or less, the number will still be positive, not negative.
# You must return the number of toast the you need to put in (or to take out). In case of 5 you can still put 1 toast in:
# six_toast(5) == 1
# And in case of 12 you need 6 toasts less (but not -6):
# six_toast(12) == 6
# Good luck!
def modulL(num):
    return abs(num - 0)

print(modulL(-2))



# Wilson primes satisfy the following condition. Let P represent a prime number.
# Then ((P-1)! + 1) / (P * P) should give a whole number.
# Your task is to create a function that returns true if the given number is a Wilson prime.
def i_am_wilson(n):
    return n in (2, 34, 5, 7)

print(i_am_wilson(2))



# The purpose of this kata is to work out just how many bottles of duty free whiskey
# you would have to buy such that the saving over the normal high street price would effectively cover the cost of your holiday.
# You will be given the high street price (normPrice), the duty free discount (discount) and the cost of the holiday.
# For example, if a bottle cost £10 normally and the discount in duty free was 10%, you would save £1 per bottle.
# If your holiday cost £500, the answer you should return would be 500.
# All inputs will be integers. Please return an integer. Round down.
def discount(price, discount, holiday):
    saving = price * discount / 100.0
    return int(holiday/saving)

print(discount(334, 45, 23))



# Write a function which converts the input string to uppercase.
def make_upper(strng):
    return strng.upper()

print(make_upper('kdjhfhf'))



# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
# For example, update_light('green') should return 'yellow'.
# Note: Use "" instead of '' in C++.
def trafficlight(current):
    return {'red': 'yellow', 'yellow': 'green', 'green': 'red'}[current]
print(trafficlight('green'))



# This function should test if the factor is a factor of base.
# Return true if it is a factor or false if it is not.
# About factors
# Factors are numbers you can multiply together to get another number.
# 2 and 3 are factors of 6 because: 2 * 3 = 6
#     You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
#     You can use the mod operator (%) in most languages to check for a remainder
# For example 2 is not a factor of 7 because: 7 % 2 = 1
# Note: base is a non-negative number, factor is a positive number.
def testbase(base, factor):
    return base % factor == 0

print(testbase(45, 5))




# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
def quater_of(month):
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4

print(quater_of(12))




# Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value.
# Output should be the length of the longest word, as a number.
# There will only be one 'longest' word.
def find_longest(strng):
    return max(len(b) for b in strng.split())

print(find_longest('euhfhf ehfwncenfeuhf3o4uhf34uhf 3nh4fu o3'))


# Write a function, gooseFilter / goose-filter / goose_filter / GooseFilter,
# that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.
# The geese are any strings in the following array, which is pre-populated in your solution:
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument:
# ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Your function would return the following array:
# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed. Note that all of the strings will be in the same case as those provided, and some elements may be repeated.
geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
print(goose_filter('fly'))



# Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him
# Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)
#     If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
#     If he doesn't get 10 hoops, return the string "Keep at it until you get it".
def hulaHoop(n):
    if n < 0:
        return 'its very bad'
    elif n < 10:
        return 'good job'
    else:
        return 'try one more time'

print(hulaHoop(43))



# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

def find_average(array):
    return sum(array) / len(array) if array else 0

print(find_average([23]))




# You were camping with your friends far away from home, but when it(('s time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! '
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not.')
# Function should return true (1 in Prolog and NASM) if it is possible and false (0 in Prolog and NASM) if not. The input values are)
def nasm(distance,mpg, fluel):
     return distance <= mpg * fluel

print(nasm(4, 1, 2))



# This is a spin off of my first kata.
# You are given a string containing a sequence of character sequences separated by commas.
# Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.
# If the input string is empty or the removal of the first and last items would cause the resulting string to be empty, return an empty value (represented as a generic value NULL in the examples below).
# Examples

def spinn_off(strng):
    return ''.join(strng.split(','))[1: -1] or None
print(spinn_off('egfiue'))

# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_smtg(a):
    return a[-1: 1]

print(remove_smtg('lnjbkhvgcfrdgvjhbk'))



# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# double_char("String") ==> "SSttrriinngg"
# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
# double_char("1234!_ ") ==> "11223344!!__  "
# Good Luck!

def double_char(a):
    return ''.join(c * 2 for c in a)

print(double_char('jkhnkjhnjk'))

# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon.
# There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true (1 in Prolog and NASM) if it is possible and false (0 in Prolog and NASM) if not. The input values are always positive.
def money(uan):
    denga = uan * (6.75)
    return denga

print(money(3))



# In this simple exercise, you will create a program that will take two lists of integers, a and b.
# Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.
# Your function will be tested with pre-made examples as well as random ones.
# If you can, try writing it in one line of code.

def find_diff(a, b):
        return abs(a[-1] * a[-2] * a[0] + b[1] * b[2] * b[0])
print(find_diff([9, 8]))



# Write a function, gooseFilter / goose-filter / goose_filter / GooseFilter,
# that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.
# The geese are any strings in the following array, which is pre-populated in your solution:
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument
# ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Your function would return the following array:
# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese'
# removed. Note that all of the strings will be in the same case as those provided, and some elements may be repeated.
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    ans = []
    for bird in birds:
        if not bird in geese:
            ans.append(bird)
    return ans

print(goose_filter('bird'))









