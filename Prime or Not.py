#WAP to Check Weather a Number is Prime or Not

num = int(input("Enter a Number: "))

if num <= 1:
    print(f"{num} is not a Prime Number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is Not a Prime Number.")
            break
    else:
        print(f"{num} is a Prime Number.")
