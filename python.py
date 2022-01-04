n =  input ("enter the number of string") 
b=len(n)
print(b)
if b>=7:
    if b%2!=0:
        c=b//2
        print(n[c-1:c+2])
else:
    print("length is less than 7",n)