
def compute_lcm(x,y):
   if x>y:
     greater = x
   else:
     greater = y
   while True:
      if (greater % x == 0) and (greater%y==0):
          lcm =greater
          break
      greater+=1
   return lcm
l=int(input("enter the value of l:"))
m=int(input("enter the value of m:"))
print("the lcm is ",compute_lcm(l,m))
