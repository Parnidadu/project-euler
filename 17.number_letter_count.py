#problem17
dict1={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:''}
#print(dict1[1])
flag=0
for i in range(1,1001):
    while(i!=0):
        temp=int(i%10);
        s=dict1[temp]
        for j in str(s):
            flag=flag+1;
        i=i/10    
print(flag)        
