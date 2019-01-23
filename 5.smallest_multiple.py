#finding the smallest number which is evenly divisible by the first twenty natural numbers
result=0
def check(num):
    if num%2==0 and num%3==0 and num%4==0 and  num%5==0 and  num%6==0 and  num%7==0 and  num%8==0 and  num%9==0 and  num%10==0 and  num%11==0 and  num%12==0 and  num%13==0 and  num%14==0 and  num%15==0 and  num%16==0 and  num%17==0 and  num%18==0 and num%19==0 and  num%20==0:
        return 1;
for i in range(1,1000000000,1):
    result=check(i)
    if(result):
        print(i)
# result take time so i just comment the answer and the answer is 232792560  
