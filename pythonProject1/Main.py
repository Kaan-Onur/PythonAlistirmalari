liste = [2, 1, 10, 2, 23, 1, 56, 3]

total = 0
for i in liste:
    if (not (i % 2 == 0)):
        total += i

print(total)