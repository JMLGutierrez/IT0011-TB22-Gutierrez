#A program that will display the following given output. (for a. use nested for statement and for b. use nested while statement)
for i in range(1,6,1): 
    for x in range(6,i,-1): 
        print(" ", end="") 
    for y in range(1,i+1,1): 
        print(y, end="") 
    print("") 
