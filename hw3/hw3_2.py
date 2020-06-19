#HW3 part 2
#CSMC 455
#Daniel Roh
#Find the are of 3 intersecting circles

import math

def incircle(x, y, xc, yc, zy):
    if((math.pow((x-xc), 2) + math.pow((y-yc),2)) <= (math.pow(zy, 2))):
        return True
    return False

#Main

#x = location in x,
#y = location in y,
#z = raduis
x1, y1, z1 = 2, 2, 1 #Circle 1
x2, y2, z2 = 0, 2, 2 #Circle 2
x3, y3, z3 = 0, 0, 3 #Circle 3
count = 0.1

print("Beginning Calculation")

while (count >= 0.001):
    print("\nCalculating area by every ", count, " spaces:")
    area = 0.0
    points = 0
    square = count * count

    x, y = -2.0, 0 #start looking for the area in the middle of circle 2

    while(x <= 2.0):
        while (y <= 3.0):
            if(not incircle(x, y, x1, y1, z1)): #check if the location is outside of circle 1
                if(incircle(x, y, x2, y2, z2)): #check if location is in circle 2
                    if(incircle(x, y, x3, y3, z3)): #check if location is in circle 3
                        area = area + square
                    #
                #
            #
            points = points + 1 #A point is in the square
            y = y + count
        #
        y = 0
        x = x + count
    #
    print("Points counted:", points)
    print("Square Area:", square)
    print("Area in circle 2/3 but not 1:", area)

    count = count * 0.1 #move to the next decimal 
#End of main
