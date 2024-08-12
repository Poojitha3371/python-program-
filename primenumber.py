n=int(input("Enter a value"))
if n==1:
    print("not a prime number")
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
        else:
            print("prime number")
else:
    print("Not a prime number")
  
