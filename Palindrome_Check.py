#pl lab3,4 Q3

str=input("Enter the string:")
if(list(str.casefold()))==(list(reversed(str.casefold()))):
    print("Yes, the string is a palindrome.")
else:
    print("Sorry, not a palindrome.")