import random


random.seed(3)

my_array = [random.randint(0,99) for i in range(20)]

print(my_array)


def selection_sort(array):
    x = array.copy()
    n = len(x)

    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
    return x


random.shuffle(my_array)

print(my_array)

print(selection_sort(my_array))

