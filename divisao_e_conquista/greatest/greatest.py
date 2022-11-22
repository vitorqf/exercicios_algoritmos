from random import randint
from time import perf_counter

def search(array):
    greatest = 0

    for i in range(len(array)):

        if (len(array[i]) > 1):
            LAST = len(array[i]) - 1

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
    random_array = [randint(1, 1000000) for _ in range(SIZE)]
    return random_array

starting = perf_counter()

try: 
    SIZE = int(input('[*] ARRAY SIZE ==> '))
    
except:
    SIZE = int(input('[!] INVALID VALUE. PLEASE, INSERT AGAIN ==> '))
    

try:
    DIVISIONS = int(input('[*] DIVIDED BY ==> '))

    while DIVISIONS > SIZE:
        DIVISIONS = int(input("[!] DIVISION CANT BE GREATER THAN ARRAY SIZE. INSERT AGAIN ==> "))

except:
    DIVISIONS = int(input('[!] INVALID VALUE. PLEASE, INSERT AGAIN ==> '))



random_array = randomize(SIZE)

array = split(random_array, DIVISIONS)
array = [bubbleSort(sub_array) for sub_array in array]

greatest = search(array)

print(f'\n[-] GREATEST: {greatest}')

print(f'[-] ELAPSED TIME: {(perf_counter() - starting):.4f} s')


