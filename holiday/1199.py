p=3.14

def ploscha_kruga(p, radius):
    return p * radius ** 2
def ploscha_pryamokutnyka(a, b):
    return a * b
def ploscha_trykutnyka(osnova, visota):
    return 0.5 * osnova * visota

print("оберіть фігуру:")
print("1 - коло")
print("2 - прямокутник")
print("3 - трикутник")

choice = input("(1/2/3): ")

if choice == '1':
    radius = float(input("введіть радіус кола: "))
    print(f"площа кола = {ploscha_kruga(p, radius)}")

elif choice == '2':
    a = float(input("введіть довжину: "))
    b = float(input("введіть ширину: "))
    print(f"площа прямокутника = {ploscha_pryamokutnyka(a, b)}")

elif choice == '3':
    osnova = float(input("введіть основу трикутника: "))
    visota = float(input("введіть висоту трикутника: "))
    print(f"площа трикутника = {ploscha_trykutnyka(osnova, visota)}")

else:
    print("нєнєнє.")
