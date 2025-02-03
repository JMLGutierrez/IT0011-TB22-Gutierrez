#Create a program that will compute the sum of the numbers from 1st term up to the last term input by the user.

tem1=int(input("Enter First Term Number: "))
tem2=int(input("Enter Last Term Number: "))
ttl=0
for x in range(tem1, tem2):
    ttl=ttl+x;
ttl=ttl+tem2
print("The sum of the numbers from ",tem1," to ",tem2," is ", ttl)
    
  
