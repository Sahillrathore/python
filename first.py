limit = int(input("Enter Number : "))

num = 1

while num <= limit:
    num2 = 1
    while num2 <= num:
        print(num2, end="")
        num2 = num2 + 1
    print('')
    num = num + 1


limitR = int(input("Enter Number : "))

r = 1

while r <= limitR:
    num2 = limitR
    while num2 >= r:
        print(num2, end="")
        num2 = num2 - 1
    print('')
    r = r + 1