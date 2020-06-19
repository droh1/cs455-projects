
#   File: HW2.py
#   Homework: CSMC455 Squire
#   Author: Daniel Roh
#
#   Find the least suare fit from 3 to 17 degree polynomials and calculate the max, avg, and RMS errors
#

# least_square.py3  very simple  polyfit, polyval
from numpy import array
from numpy.linalg import solve
import math

def polyfit(order, n, x, y):
  # x and y input arrays length n, p polynomial coef length order+1 
  # can initialize an array to zero
  a   = array([[0.0 for j in range(order+1)] for i in range(order+1)])
  xx  = array([0.0 for i in range(order+1)])
  yy  = array([0.0 for i in range(order+1)])
  pwr = array([0.0 for i in range(order+1)])
  p   = array([0.0 for i in range(order+1)]) #  returned
  for k in range(n):  # each x,y input
    pwr[0] = 1.0
    for kk in range (1,order+1):
      pwr[kk] = pwr[kk-1]*x[k]    # 1, x, x^2, x^3, ...

    for i in range(order+1):
      for j in range(order+1):
        a[i][j] = a[i][j] + pwr[i]*pwr[j]
	   
      yy[i] = yy[i] + pwr[i]*y[k]

  p = solve(a,yy)
  return p
  
def polyval(order, p, x):     # return y = p(x) for n values
  # using Horner's rule
  y = p[order]*x
  for i in range(order-1,0,-1):
    y = (p[i]+y)*x
  y = p[0]+y
  return y

def f(x):
  return x*x*x*x + 2.0*x*x*x + 3.0*x*x + 4.0*x + 5.0
  
print("least_square.py3 running test")
n = 20
order = 4
power = 3

#EDIT THE n, n should increase the power not the number of items
while power < 18:

    xd = array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 0])
    yd = array([0.0, 6.0, 14.09, 5.6, 4.5, 4.5, 4.5, 4.3, 4.3, 4.24, 4.25, 4.25, 4.3, 4.25, 4.2, 4.3, 4.3, 4.2, 4.0, 0])
    p = array([0.0 for i in range(order+1)])

    for i in range(n):
      yd[i] = f(xd[i])
#while power < 18:
#Skip printing for cleaness 
#    print("xd=",xd)
#    print("yd=",yd)

   # print("n =",power,"  order =",order)
    #print("----------------------------------------------------------------------------------------------------")

    p = polyfit(order, n, xd, yd)
    #print("p=",p) #CHECK IF THIS NEEDS TO BE IN HERE
    # check p*xd^ = yd  for errors
    
    max_err = 0.0
    avg_err = 0.0
    rms_err = 0.0

    for k in range(n):
      y1 = polyval(order, p, xd[k]) 
      err = abs(y1-yd[k])
      max_err = max(max_err, err)
      avg_err = avg_err + err
      rms_err = rms_err + err*err

    avg_err = avg_err/n
    rms_err = math.sqrt(rms_err/n)
    print("n=",n," max_err=",max_err,"  avg_err=",avg_err,"  rms_err",rms_err)

#    print("----------------------------------------------------------------------------------------------------\n")
    #order = order + 1 #Go to next order
    #n = n + 1
    power = power + 1
print("least_square.py3 test finished")
# end least_square.py3
