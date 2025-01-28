#A program that will display the following given output. (for a. use nested for statement and for b. use nested while statement)
for i in range(1,7,1): 
    for x in range(7,i,-1): 
        print(" ", end="") 
    for y in range(1,i,1): 
        print(y, end="") 
    print("") 
