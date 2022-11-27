from random import randint
from time import perf_counter


def randomize(SIZE):
    # Começa a contar a performance da função randomize
    starting = perf_counter()
    
    # Cria um array de SIZE posições com números aleatórios de 1 a 10
    array = [randint(1, 1000) for _ in range(SIZE)]

    # Finaliza a contagem de performance da função randomize
    elapsed = round(perf_counter() - starting, 4)

    print(f"[-] {'RANDOMIZING:':<20} {elapsed:>26} sec [-]")

    return array