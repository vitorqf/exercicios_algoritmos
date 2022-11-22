from time import perf_counter
from randomize import randomize
from split import split
from bubblesort import bubbleSort
from prime import prime

SIZE = int(input('ARRAY SIZE ==> '))
DIVISIONS = int(input('DIVIDED BY ==> '))

print('')

random = randomize(SIZE)

split = split(random, DIVISIONS)

extract_time = perf_counter()

for sub in split:
    print(f'{sub}')

split = [bubbleSort(prime(sub_array)) for sub_array in split]

print(f"[-] {'AVG EXTRACTING:':<20} {round((perf_counter() - extract_time), 4):>26} sec [-]")

print(split)