# WAP to Find Out The Factorial of a Number

num = int(input("Enter a Number : "))
factorial = 1
if num < 0:
    print(" ")
else:
    for i in range(1, num + 1):
        factorial *= i
        print(f"Factorial of {num} is {factorial}")