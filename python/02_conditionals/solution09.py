year = int(input("Enter a year! \n"))

if( (year%400)==0 or (year%4)==0  and (year%100)!=0):
    print("its a leap year")
else:
    print("Sorry its not a leap year")   