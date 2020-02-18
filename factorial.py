x = int(input("enter the num:"))
factorial =1
if x<0:
    print("the factorial does not exist for negative number")
elif x==0:
    print("the factorial of 0 is 1")
else:
 for i in range(1,x+1):
     factorial = factorial*i

 print("the factorial of",x,"is",factorial)