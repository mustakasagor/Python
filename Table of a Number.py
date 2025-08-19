# WAP to Print Table of Number

num = int(input("Enter a Number: "))
print(f"\nTable of {num}: ")
for i in range(1, 11):
    print(f"{num} {i} = {num - i}") 