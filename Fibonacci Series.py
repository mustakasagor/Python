# WAP to Display The First to Terms of a Fibonacci Seriess

n = int(input("Enter The Number of Terms: "))

if n <= 0:
    print("Please Enter a Positive Integer.")
else:
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
