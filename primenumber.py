n=int(input("Enter a value"))
flag=False
if n==1:
    print("not a prime number")
if n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
if flag:
    print("prime number")
else:
    print("Not a prime number")
  
