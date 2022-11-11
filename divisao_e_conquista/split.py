from time import perf_counter


def split(array, divisions):
    starting = perf_counter()

    elapsed = round((perf_counter() - starting), 4)

    print(f"[-] {'SPLITTING:':<20} {elapsed:>26} sec [-]")

    return [array[i::divisions] for i in range(divisions)]