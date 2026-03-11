age = int(input("Enter age: \n"))
day = input("Enter day: \n")

price = 12 if age>13 else 8
if day.upper() == "WEDNESDAY":
    #price = price - 2
    price -= 2
print("Ticket prize is ", price)