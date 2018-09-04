# get length
# declare counter
# 
# 
# while counter is less than requested length
# 
# raise number 
# print number
# 
# last_number, secondlast_number = number, last_number
#
# number 1
# number 2
# number 3
# correct number = numbers 1 + 2 + 3
#


n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 0
number = 1
number1 = 0
number2 = 0
number3 = 0

while counter < n :
    if number >= 3 :
        number3 = number2
    number2 = number1
    number1 = number
    
    number = number3 + number2 + number1

    print(str(number))

    counter += 1