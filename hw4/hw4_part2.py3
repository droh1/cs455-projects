#CSMCS455
#Daniel Roh
#Calculate the number of ways 5 cards can be selected

#Calculate the factorial of n
def factorial(n):
    total = 1

    for i in range(1, n + 1):
    	total = total * i

    return total


#Main starts here
n = 52 #number of cards
m = 5 #cards to be chosen

print("Calculating 5 choose 52")

value = ((factorial(n)) / (factorial(n - m) * factorial(m)))

print("Value: ", value)
