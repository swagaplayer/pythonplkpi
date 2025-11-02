age = int(input("введіть ваш вік: "))

if 1 <= age <= 120:
    if age % 10 == 1 and age % 100 != 11:
        word = "рік"
    elif age % 10 in [2, 3, 4] and not (12 <= age % 100 <= 14):
        word = "роки"
    else:
        word = "років"
    
    print(f"{age} {word}")
else:
    print("брехло кукурудзяне! вам точно не більше 120.")
