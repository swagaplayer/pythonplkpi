n = int(input("введіть n: "))
if n < 0:
    print("doesn't exist")
else:
        a, b = 0, 1
        result = []
        while a <= n:
            result.append(str(a))
            a, b = b, a+b
        print(" ".join(result))
