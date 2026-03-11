num = int(input("Enter a number: "))

is_prime = True

if(num > 1):
    for i in range (2, (num//2)):
        if((num % i)==0):
            is_prime = False
            break

if(is_prime == 1 ):
    print("its a prime baby")  
else:
    print("go f**k your self")         