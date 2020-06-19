#HW3 part 1
#CSMC 455
#Daniel Roh
#Compute error using trapizodal integration

import math

def f(x):
  return math.sin(x)
  #return x*x

def trap_int(f, xmin, xmax, nstep): # integrate f(x) from xmin to xmax
  area=(f(xmin)+f(xmax))/2.0
  #h = (xmax-xmin)/nstep #this shouldent matter due to 1-0 = 1
  h = xmax / nstep
  for i in range(1,nstep):
    x = xmin+i*h
    area = area + f(x)

  return area*h # trapezoidal method

#Main

error = 1 - math.cos(1.0)
print("Computing Trapizodal Error")


#loop for 16, 32, 64, 128 points
n = 16
while n < 129:
#for x in range(16, 128, x * 2):
    #


    print("\nCalculating n = ",n, " from 0.0 to 1.0")
    xmin = 0.0
    xmax = 1.0
    area = trap_int(f, xmin, xmax, n)
    print ("Area:", area)
    print ("Actutal:",error)
    print ("Error:", (area - error))
    n = n * 2
    
#xmin = 1.0
#xmax = 2.0
#n = 10
#area = trap_int(f, xmin, xmax, n)
#print "trap_int area under x*x from ",xmin," to ",xmax," = ",area
