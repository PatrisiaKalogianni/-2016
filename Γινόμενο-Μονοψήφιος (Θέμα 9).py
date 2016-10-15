# p15049 Patrisia Kalogianni
# Lesson : "Introduction to Computer Science"
# Project 9 : How many times must the digits of the given number be multiplied so that
#             the result is a single-digit number?


def multiply(n):                        #
    mul = 1                             #
    stringIt = str(n)                   # This function multiplies the digits of number
    for i in  stringIt :                #
        mul = mul * int(i)              #
    return mul                          #


def check():
    number = raw_input("Give a number:\t")
    newNumber = multiply(number)
    times =0
    while (newNumber >= 0):
        if (newNumber < 10):       
            times +=1
            if times == 1 :
                print "The digits of the given number must be multiplied ~%d~ time with eachother to give a one-digit number!" %(times)
            else:
                print "The digits of the given number must be multiplied ~%d~ times with eachother to give a one-digit number!" %(times)
            break
        else:
            times += 1
            newNumber = multiply(newNumber)
         
    
check()
