from random import randint

def search(array):
    LAST = len(array) - 1
    greatest = 0

    for i in range(len(array)):
        if (len(array[i]) > 1):
            if array[i][LAST] >= greatest:
                greatest = array[i][LAST]

        else:
            if array[i][0] >= greatest:
                greatest = array[i][0]

    return greatest

def bubbleSort(array):
    length = len(array)

    for j in range(length - 1):
        for i in range(length - 1 - j):
            if(array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]

    return array

def split(array, DIVISIONS):
    split_array = [array[i::DIVISIONS] for i in range(DIVISIONS)]
    return split_array

def randomize(SIZE):
    random_array = [randint(1, 1000) for _ in range(SIZE)]
    return random_array

SIZE = int(input('ARRAY SIZE\n==> '))
DIVISIONS = int(input('DIVIDED BY\n==> '))

random_array = randomize(SIZE)
array = split(random_array, DIVISIONS)
array = [bubbleSort(sub_array) for sub_array in array]

for sub_array in array:
    print(f'{sub_array}')

greatest = search(array)

print(greatest)


