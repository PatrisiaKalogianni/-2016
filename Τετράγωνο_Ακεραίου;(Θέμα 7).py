# p15049 Patrisia Kalogianni
# Lesson : "Introduction to Computer Science"
# Project 7 : Is the given number the square of an integer?


def intSquareRoot():
    x = float(raw_input('Give a number: '))
    sqroot = x ** 0.5                           # Find square root 
    if  (sqroot == int(sqroot)):                # Check if the square root has a fractional part
        print True
        return True
    else:
        print False
        return False
		
intSquareRoot()
