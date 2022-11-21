from time import perf_counter
from bubblesort import bubbleSort
from split import split
from randomize import randomize
from merge import merge

# Começa a contar a performance geral
runtime = perf_counter()


# Define o tamanho do array inicial e em quantos arrays ele deve ser dividido
SIZE = int(input("INSERT ARRAY TOTAL SIZE\n=> "))
DIVISIONS = int(input("INSERT TOTAL ARRAYS\n=> "))

# Inicio do relatório de performance
print(f"\n{' RESULTS ':=^59}")

# Gera um array aleatório
raw_array = randomize(SIZE)

# splitted_arrays = split(raw_array, divisões))
splitted_arrays = split(raw_array, DIVISIONS)

# cada array dentro de splitted_arrays é substituída pelo sua versão bubblesorted
sorting = perf_counter()

splitted_arrays = [bubbleSort(splitted_arrays[i]) for i in range(len(splitted_arrays))]

elapsed = round(perf_counter() - sorting, 4)

print(f"[-] {'SORTING:':<20} {elapsed:>26} sec [-]")
# fim do sorting

# # inicio do merging
# merging = perf_counter()

# merged = []

# elapsed = round(perf_counter() - merging, 4)

# print(f"[-] {'MERGING:':<20} {elapsed:>26} sec [-]")

# # Finaliza a contagem de performance geral
elapsed = round(perf_counter() - runtime, 4)

print(f"[-] {'RUNTIME:':<20} {elapsed:>26} sec [-]")
print(f"{'':=^59}")

