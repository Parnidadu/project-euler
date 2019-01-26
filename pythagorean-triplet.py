#finding the pythagoras triplets
for i in range(20,500):
    for j in range(30,500):
        for k in range(40,500):
            if(i**2+j**2==k**2):
                if(i+j+k==1000):
                    print(i,j,k)
                    
"""result are : 200 375 425
375 200 425"""     
#and the answer would be the multiple of the triplet and that is 31875000
