#A program that will display the number of vowels, consonants, spaces, and other characters given an input string. (use for loop and some operators under module 1 and 2)
num=input("Enter String: ") 
checkV="aeiouAEIOU" 
checkC="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM" 
checkSp=" " 
countV=0 
countC=0 
countSp=0 
countO=0 

  

for x in num: 
    if x in checkV: 
        countV+=1 
    elif x in checkC: 
        countC+=1 
    elif x in checkSp: 
        countSp+=1 
    else: 
        countO+=1 


print("Vowels: ", countV) 
print("Consonants: ", countC) 
print("Spaces: ", countSp) 
print("Other Character: ", countO) 
