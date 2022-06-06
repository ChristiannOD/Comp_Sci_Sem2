symbol = input("Please choose a symbol: ")
w = int(input("Whats the width of your box? "))
h = int(input("Whats the height of your box? "))

for x in range(0,h):
    for y in range(0,w):
        print(symbol, end='')
    print()