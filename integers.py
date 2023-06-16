num = [-3, 9, -4, 8, 5, 9 ,5]
total = 0
for i in num:
    if i < 0:
        continue
    if i > 0:
        total = total + i
print(total)
