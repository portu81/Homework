num = int(input())
if num > 0 and num % 2 == 0:
    print("положительное четное число")
elif num > 0 and num % 2 != 0:
    print("положительное нечетное число\nчисло не является четным")
elif num < 0 and num % 2 != 0:
    print("отрицательное нечетное число\nчисло не является четным")
elif num < 0 and num % 2 == 0:
    print("отрицательное четное число")
else :
    print("нулевое число")
