import random
x = int(input("How many numbers do you want? "))
mynums = [1,2,3,4,5,6,7,8,9,10]
for w in range(0,x):
    r = random.randrange(10)
    print(mynums[r])