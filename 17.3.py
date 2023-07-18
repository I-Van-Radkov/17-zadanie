numbers = []
for i in range(1000, 10000):
    mas = set(str(i))
    if len(mas) == len(str(i)):
        flag = True
        for j in mas:
            if int(j) % 2 == 0:
                flag = False
                break
        if flag:
            numbers.append(i)
print(len(numbers), numbers[0])