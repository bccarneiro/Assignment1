l = []
for i in list(range(2000,3201)):
    if i % 5 == 0:
        continue
    elif i % 7 == 0:
        l.append(i)
print(l)
