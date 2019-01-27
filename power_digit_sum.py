#calculating power of 2 to thousand
n=1
a=2

while(n<1000):
    a=a*2
    n=n+1
print(a)   
if a==2**1000:
    print('true')
else:
    print('false')
answer=0
while(a!=0):
    answer=answer+a%10
    a=int(a/10)
print(answer)    
