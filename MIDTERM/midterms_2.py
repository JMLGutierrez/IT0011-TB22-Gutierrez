#Create a program that will translate a given date format in mm/dd/yyyy to more human readable
#format like January 1, 2023

date=input("Enter the Date (mm/dd/yyyy): ")
partition=date.split('/')
month=int(partition[0])
day=int(partition[1])
year=partition[2]

if month==1:wordm="January"
elif month==2:wordm="February"
elif month==3:wordm="March"
elif month==4:wordm="April"
elif month==5:wordm="May"
elif month==6:wordm="June"
elif month==7:wordm="July"
elif month==8:wordm="August"
elif month==9:wordm="September"
elif month==9:wordm="October"
elif month==11:wordm="November"
elif month==12:wordm="December"
else:print("invalid date")

print("Date Output: {0} {1}, {2}".format(wordm, day, year))
