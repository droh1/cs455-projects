#CMSC455
#Daniel Roh
#Calculate the number of ways to arrange a deck of cards in a line

n = 52 #Number of cards
total = 1

print("Calculating 52! factorial")

for i in range(1, n+1): #Calculate factorial
    total = total * i

print("It is: ", (total))