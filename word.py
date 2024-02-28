word = str(input())
couter1 = 0
couter2 = 0
a = 0
e = 0
i = 0
o = 0
u = 0
for y in range(len(word)):
    if word [y] in 'aeiouy':
        couter1 += 1
    elif word [y] in 'bcdfghjklmnpqrstvwxz':
        couter2 += 1
print("количество гласных =", couter1,"\nколичество согласных =", couter2)
for y in range(len(word)):
    if word [y] in 'a':
        a += 1
    elif word [y] in 'e':
        e += 1
    elif word [y] in 'i':
        i += 1
    elif word [y] in 'o':
        o += 1
    elif word [y] in 'u':
        u += 1
if a == 0 or e == 0 or i == 0 or o == 0 or u == 0:
    print("False")
else :
    print("a =", a,"\ne =", e,"\ni =", i,"\no =", o,"\nu =", u)
