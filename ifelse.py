# Finding the greatest num amonng three nums

num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
num3 = int(input("Enter Third Num: "))

if num1 > num2:
    if num1 > num3:
        print("First Num is Greatest", num1)
    else:
        print("Third Num is Greatest", num3)
elif num2 > num3:
    if num2 > num1:
        print("Second Num is Greatest", num2)
    else:
        print("First Num is Greatest", num1)

elif num3 > num2:
    if num3 > num1:
        print("Third Num is Greatest", num3)
    else:
        print("First Num is Greatest", num1)