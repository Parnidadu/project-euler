#problem 15, the possible number of direction for a grid  to reach to a destination
grid=(int(input("enter the size of grid")))
result=1
for i in range(0,grid):
    result=result*((grid*2)-i);
    result=result/(1+i);
print(result)
