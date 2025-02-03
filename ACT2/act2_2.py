# Create a program will show if the given input number is a prime number (a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 e.g. 2, 3, 5, 7, 11). Use looping statement to solve the problem.

numinpt=int(input("Enter a Number: "))
if numinpt > 1:
    for i in range(2, numinpt):
        if (numinpt % i) == 0:
            print(numinpt, "is not a prime number")
            break
    else:
        print(numinpt, "IS a prime number! :D")
else:
    print(numinpt, "IS NOT a prime number! D:")
    
