number = int(input("Enter: "))

sum = 0
for i in range(number):
    if((i%2)==0):
        sum = sum + i
print(sum)        