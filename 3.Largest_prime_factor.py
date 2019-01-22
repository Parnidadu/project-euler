#finding the largest prime factor of a number
num=600851475143
loop=num**0.5
loop=loop/2
#print(loop)
j=1
list2=[]
for i in range(1,int(loop)):
    if num%i==0:
        #print(i)
        list2.append(i)
    else:
        pass
for i in list2:
    j=j*i;
    if(j==num):
        print(i)
        #i is the result
