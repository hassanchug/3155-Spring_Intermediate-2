# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

# Links below indicate help found online
# https://docs.python.org/3/library/time.html

import time
start = time.time()

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

number = 35

print("fib(" + str(number) + ") = " + str(fibonacci(number)))

end = time.time()

print("fib(" + str(number) + ") took " + str(end-start) + " seconds")