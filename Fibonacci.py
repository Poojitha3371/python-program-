n=int(input())
a=0
b=1
print(a)
print(b)
i=0
for i in range(n-2):
    c=a+b
    print(c)
    a=b
    b=c
