#3. Ron has been given 10 numbers which includes both positive and negative values by his teacher. His task is to tell the total of positive and negative numbers separately. Our task is to help him in this task. 

#Sample Input:
#10
#50
#-30
#15
#-45
#-96
#5
#78
#-99
#253

#Expected Output:
#Sum of Positive Numbers = 411 Sum of Negative Numbers =-270
i=1
p=0
ne=0

for i in range(10):
    n=int(input("enter number"))
if n>0:
    p=p+n
elif n<0:
    ne=ne+n
    print("sum of negitives.",ne)
    print("sum of postive number.",p)
        

