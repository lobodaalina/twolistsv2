import random


def func():
    n = int(input("Enter the number of elements in lists:"))
    list1 = [random.randint(0, 10) for i in range(n)]
    list2 = [random.randint(0, 10) for j in range(n)]
    print(list1)
    print(list2)
    list3 = []
    for i in list1:
        if i in list3:
            continue
        for j in list2:
            if i == j:
                list3.append(i)
                break
    print(list3)

func()
