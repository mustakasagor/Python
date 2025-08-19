# WAP to Calculate The Sum of First in Natural Number

n = int(input("Enter a Number: "))

sum_formula = n * (n + 1) // 2

sum_loop = 0
for i in range(1, n + 1):
    sum_loop += i

print(f"\nUsing formula: Sum of First {n} natural numbers = {sum_formula}")
print(f"Using loop: Sum of First {n} natural numbers = {sum_loop}")
