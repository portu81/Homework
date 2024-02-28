a = float(input())
b = float(input())
min_invest = float(input())
if a >= min_invest and b >= min_invest:
    print("2")
elif a >= min_invest and b < min_invest:
    print("Maik")
elif a < min_invest and b >= min_invest:
    print("Ivan")

elif a < min_invest and b < min_invest and (a + b) > min_invest:
    print("1")
else:
    print("0")
