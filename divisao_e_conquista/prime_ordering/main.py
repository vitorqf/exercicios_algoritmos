from time import perf_counter
from randomize import randomize
from split import split
from bubblesort import bubbleSort
from prime import prime

starting = perf_counter()

SIZE = int(input('ARRAY SIZE ==> '))
DIVISIONS = int(input('DIVIDED BY ==> '))

print('')

print(f"{' RESULTS ':=^59}")

# Retorna um array de tamanho SIZE com números aleatórios de 1 a 1000
random = randomize(SIZE)

# Retorna um array de arrays com tamanhos de SIZE/DIVISIONS
split = split(random, DIVISIONS)

extract_time = perf_counter()

prime_numbers = []

# Para cada array dentro do array separado
for subarray in split:
    
    # Se o número for primo e não for repetido, o registre no array de primos
    if (prime(subarray) not in prime_numbers and prime(subarray) != None):
        prime_numbers.append(prime(subarray))

print(f"[-] {'EXTRACTING:':<20} {round((perf_counter() - extract_time), 4):>26} sec [-]")

sorting_time = perf_counter()

prime_numbers = bubbleSort(prime_numbers)

print(f"[-] {'SORTING:':<20} {round((perf_counter() - sorting_time), 4):>26} sec [-]")

print(f'[-] PRIMES: {prime_numbers}')

print(f'\nDone in {round((perf_counter() - starting), 4)} sec')