N = int(input("введіть число N: "))

print(f"числа, які не перевищують {N} і діляться на всі свої цифри:")

for num in range(10, N + 1):
    digits = [int(d) for d in str(num)]
    
    if 0 in digits:
        continue
    
    if all(num % d == 0 for d in digits):
        print(num)
