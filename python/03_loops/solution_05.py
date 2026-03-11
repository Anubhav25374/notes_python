#first non repeating character

str = input("Enter string: ")
string = str.lower()
for char in string:
    if(string.count(char)==1):
        print("First non repeating character in string is : ", char)
        break