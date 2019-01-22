#find the term of fibonacci series just less than 4 million
then = 1
now = 2
list1=[1,2]
result=2
for i in range(1,33):
    temp = now
    now = then + now
    then = temp
    if now<=4000000:
        list1.append(now)
    if now<=4000000 and now%2==0:
        result=result + now
print(list1)
print(len(list1))
print(result)
#correct answer is the result
#[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
#32
#4613732   --> answer

