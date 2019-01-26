#problem number 14;
def function(n):
    list1=[]
    while(n!=1):
        if n%2!=0:
            n=3*n+1;
            list1.append(n)
        else:
            n=n/2;
            list1.append(n)
            
    return(len(list1))   

num=1000000
#num=int(input("enter the number"));
length=0
for i in range(num,1,-1):
    length1=function(i);
    if length<length1:
        length=length1;
        flag=i;
    else:
        pass
print(length) 
print(flag)
