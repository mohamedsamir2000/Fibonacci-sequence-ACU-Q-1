# Program to display the Fibonacci sequence up to n-th term
print("hi ")
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0


if nterms <= 0:
       print("Please enter a positive integer")
if nterms == 1:
       print("Fibonacci sequence:",nterms,":")
       print(n1)

       
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
 