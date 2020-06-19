#HW3 part 2
#CSMC 455
#Daniel Roh
#Use Gauss Legendre method with 8 and 16 points

# test_gaulegf.py  test  gaulegf.py  function gaulegf
from gaulegf import gaulegf
import math

def f(p):
  return math.sin(x)
  #return p*p

#Main
#for 8
error = 1 - math.cos(1)
print ("calling x,w = gaulegf(0.0, 1.0, 8)")
n = 8
x,w = gaulegf(0.0, 1.0, n)
#print ("x=", x)
#print x
#print ("w=", w)
#print w

area = 0.0
for i in range(1, n+1):
  #area += w[i]*f(x[i])
  area = area + (w[i] * math.sin(x[i]))
print ("area=",area)
print ("actual=", error)
print ("error=", area - error)


#for 16
print ("\ncalling x,w = gaulegf(0.0, 1.0, 16)")
n = 16
x,w = gaulegf(0.0, 1.0, n)
#print ("x=",x)
#print x
#print ("w=",w)
#print w

area = 0.0
for i in range(1, n+1):
  #area += w[i]*f(x[i])
  area = area + (w[i] * math.sin(x[i]))
print ("area=", area)
print ("actual=", error)
print ("error=", area-error)
#print  area
