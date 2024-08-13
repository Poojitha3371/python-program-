n=input('Enter a string: ')
l=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in n:
    if i in l:
        count+=1
print(count)
