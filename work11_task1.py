def fact_num():
    num = int(input())
    factorial = 1
    i = 1
    my_list = []
    while i <= num:
        factorial *=  i
        i += 1
        my_list.append(factorial)
    my_list.reverse()
    print(my_list)


fact_num()
