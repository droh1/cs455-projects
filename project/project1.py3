#Project (Find minimum)
#CS455
#Daniel Roh
#Find the global minium of exp(sin(50.0*x)) + sin(60.0*exp(y)) + sin(70.0*sin(x)) + sin(sin(80.0*y)) - sin(20.0*(x+y)) + (x*x+y*y)/4.0

from mpmath import *
 
#The function that needs to be solved
def solver(x, y):
  return exp(sin(50.0*x)) + sin(60.0*exp(y)) + sin(70.0*sin(x)) + sin(sin(80.0*y)) - sin(20.0*(x+y)) + (x*x+y*y)/4.0

#Optimizes by comparing to the 8 spots around the current best spot
def optimizer(newX, newY, newLow, change, count):
    count = count + 1
    optiX = newX - change
    optiY = newY - change
     
    if (optiX < -1.0):
        optiX = -1.0
    elif (optiX > 1.0):
        return newLow, newX, newY
     
    while(optiX <= newX + change):
        optiY = newY - change
        if (optiY < -1.0):
            optiY = -1.0
        elif (optiY > 1.0):
            return newLow, newX, newY
 
        while(optiY <= newY + change):
            z = solver(optiX, optiY)
            
            if (z < newLow):
                print("Optimizer success")
                newLow = z
                tempX = optiX
                tempY = optiY
                
                if (count < 990):
                    print(count, "Optimizer shifting to: ", tempX, ",", tempY, ",", z)
                    z, tempX, tempY = optimizer(tempX, tempY, newLow, change, count) #Recurse with better x and y to keep shifting around
                    
                if (z < newLow):
                    newLow = z
                    newX = tempX
                    newY = tempY
                return newLow, newX, newY
             
            optiY += change
        optiX += change

    return newLow, newX, newY
 
#Function taken and modifyed from test_spiral.py
def run_range(spiralX, spiralY, change, zmin):
  n = 101
  xmin = spiralX - change
  xmax = spiralX + change
  ymin = spiralY - change
  ymax = spiralY + change
   
  xh = (xmax-xmin)/n
  yh = (ymax-ymin)/n
 
  atx = xmin
  aty = ymin
 
  for i in range(n):
    x = xmin+i*xh
    for j in range(n):
      y = ymin+j*yh
      z = solver(x, y)
      
      if z<zmin: #See if a new min if found
        zmin = z
        atx = x
        aty = y
 
  return zmin, atx, aty

#Main starts here
def main():
  x, y, xMax, yMax = -1.0, -1.0, 1.0, 1.0
  minX, minY = -1.0, -1.0
  mainChange = 0.001
  change = 0.0001 #used for run_range
  lowestZ = 99.99
  count = 0
  
  print("Starting global search for local minimum for: exp(sin(50.0*x)) + sin(60.0*exp(y)) + sin(70.0*sin(x)) + sin(sin(80.0*y)) - sin(20.0*(x+y)) + (x*x+y*y)/4.0") #DEBUG

  while (x <= xMax):
    y = -1.0
    
    while (y <= yMax):
      z = solver(x, y)
      
      if (z < lowestZ): #Check with the last min to see if z is smaller one is found
        print("A new local minimum found (", x, ",", y, ")", z) #DEBUG
        lowestZ = z
        minX = x
        minY = y
        
      y = y + mainChange
    x = x + mainChange
 
  #Set the precision to 100 places
  mpf.dps = 101
  mp.dps = 101
     
  minima = 5 #Defualt times to optimize
  print("***************************************************************")
  print("Setting high percision and checking mins again") #DEBUG

  while (minima > 0 and change > mpf(1.0e-100)): #0.0000000000000000001): #Make sure minima is not 0 and the change is not too small
    z, tempX, tempY = run_range(minX, minY, change, lowestZ)
    
    if (z < lowestZ): #Check if a new min is found
      print("A new local minimum found: Z =", z, "(", tempX, ",", tempY, ")") #DEBUG
      lowestZ = z
      minX = tempX
      minY = tempY
      minima = minima + 1 #Add 1 to check next level
      change = change * 0.9
    else:
      minima = minima - 1 #Remove 1 to avoid wasting time
      change = change * 0.7

    xMin = minX - change
    xMax = minX + change
    yMin = minY - change
    yMax = minY + change
    
    if (z < lowestZ): #If optm found a smaller min
      print("A new minimum found Z =", z, "(", tempX, ",", tempY, ")") #DEBUG
      lowestZ = z
      minX = tempX
      minY = tempY
      minima = minima + 1 #Add 1 to check next level
    else:
      thing = 0
      
  print("\n\nGlobal minimum: ", lowestZ, "(", minX, ",", minY, ")")
 
main()