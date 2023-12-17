
list = [1,2,3,4,6,7,8,9,10]
list_second = []
for x in range(1,11):
    if x not in list:
        list_second.append(x)
        print(x)


