num = int(input("Enter a number: "))
min = num

while num != 0:
    num = int(input("Enter a number: "))

    if (num < min):
        min = num

    # termination
    if num == 0:
        break

print("Minimum is: ", min)
