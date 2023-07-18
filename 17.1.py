count = []
for wife in range(1, 10001):
    s = 0
    for j in str(wife):
        s += int(j)
    if s % 5 == 0:
        count.append(wife)
print(len(count), count[-1])
