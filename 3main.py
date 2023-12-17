

foiz = int(input("foiz kirit:"))
list = [10,20,30,40,60]
list_second = []
#for x in list:
    #print(f"{(x*foiz)/100}")

def find_percent(percent, massive,list_second):
    for x in massive:
        num = (x*percent)/100
        list_second.append(num)
    return list_second

print(find_percent(foiz,list,list_second))


