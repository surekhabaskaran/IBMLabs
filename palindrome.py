x = str(input("enter the value:"))
x =x.casefold()
rev = x[::-1]
print (rev)
if rev==x:
    print("this is palindrome")
else:
    print("this is not palindrome")