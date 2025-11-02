rozv=[]

for X in range(1, 15):
    if (X+X-9==4 and X-X*X==4 and X+X-X==4 and X+X/X==4 and 9-X-X==4):
        rozv.append(X)

if rozv:
    print(f"можливий розв'язок: {rozv}")
else:
    print("розв'язків немає")
