n =  input ("enter the number of string1")
v =  input ("enter the number of string2") 
c=len(n)
k=c//2
m=n[:k]+v+n[k:c+1]
print(m)