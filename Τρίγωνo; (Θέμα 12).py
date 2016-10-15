# p15049 Patrisia Kalogianni
# Lesson : "Introduction to Computer Science"
# Project 12 : Can the given numbers creat a triangle? And if so, what type of tringle
#              is it, based on it's angles?

def triangleType():
    a = int(raw_input("Give first number:\t"))
    b = int(raw_input("Give second number:\t"))
    c = int(raw_input("Give third number:\t"))
    x=[a,b,c]                                      # Creat list to find the largest number
    x.sort()                                       # #n order from smallest to largest
    mx=x.pop()
    mx2=x.pop()
    x=x.pop()
	
    if (mx2-x <= mx) and (mx <= mx2+x):            # Triangle Inequality
        
        if (mx*mx < (mx2*mx2+x*x)):                #
            print 1                                # An Acurate tringle can be created
            return 1                               #
			
        elif (mx*mx > mx2*mx2+x*x):                #
            print 2                                # An Obtuse triangle can be created
            return 2                               #
			
        else:                                      #
            print 3                                # A Right tiangle can be created
            return 3                               #
			
    else:                                          #
        print -1                                   # No triangle can be created
        return -1                                  #
    
triangleType()
