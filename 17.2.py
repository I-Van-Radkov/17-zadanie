nech = '13579'
password = []
max_pass = 0
for i in range(10000, 100000):
    if (str(i)[-1] in nech) and (str(i)[-2] in nech):
        if str(i)[1] == '2':
            password.append(i)
            if str(i)[-1] == '5':
                max_pass = i
print(len(password), max_pass)