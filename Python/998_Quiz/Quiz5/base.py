x = str(input("What is your favorite number? "))
y = int(input("Whats your top favorite number?  "))
a = int(input("Whats your age? "))
j = x[0:len(x)]
for i in range(0,len(x)) :
    print(j[i:i+1])
print(a*y)

