answer=0
listing=[]
for i in range(1,1000000):
    answer=answer+i;
    if len(listing)==500:
        break
    listing=[]    
    for j in range(1,answer+1):
        if answer%j==0:
            listing.append(j)
print(answer)
