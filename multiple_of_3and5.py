#find the sum of number which are multiple of 3 and 5

#the problem statement is from project euler
add = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        add=add+i
           
print(add)   

#answer is= 233168
