number = int(input("Enter: "))

for i in range(1,11):
    if i==5:
        continue
    else:
        print(number," * ",i," = ",number*i)    