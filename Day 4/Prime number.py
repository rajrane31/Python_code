n=int(input("Enter any number:"))

isPrime=True  #Passing boolean value TRUE(1)isPrime variable

for i in range(2,n):
    if(n%i==0):
        isPrime=False # if remainder is zero pass false (0) value to isPrime variable
        break   # To break for loop

if(isPrime): # Here it by default checks for the True value. if(isPrime == True) is equivalent to if(isPrime):
    print("Prime Number")
else:
    print("Not Prime Number")
