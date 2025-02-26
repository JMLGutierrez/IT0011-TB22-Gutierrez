#given the file currency.csv (currency exchange from 1 USD), create a program that will convert a certain input currency given the dollar to be converted.

import csv 

convert={
  "Code":[],
  "Name":[],
  "Rate":[]
}


f=open('currency.csv', mode='r', encoding='latin-1')
#https://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte
csvFile = csv.reader(f)
next(csvFile)
for lines in csvFile:
    convert["Code"].append(lines[0])
    fRate = float(lines[2])  
    convert["Rate"].append(fRate)
    convert["Name"].append(lines[1])

choice='Y'

while choice!='N':
  print("--------Currency Converter--------\n")
  money=input("How much dollar do you have? ")
  (currcode)=input("What currency you want to have? ").upper()
  for i in range(len(convert["Code"])):
    if currcode==convert["Code"][i]:
      conmoney=float(money)*convert["Rate"][i]
      print("Dollar: ", money)
      print(convert["Name"][i],":",conmoney)
       
  choice=input("Convert Again? Y/N: ").upper()
  print("\n")
