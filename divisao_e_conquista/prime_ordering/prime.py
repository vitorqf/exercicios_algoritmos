def prime(array):

    prime_array = []

    for i in range(len(array)):
        count = 0
        for j in range(1, array[i] + 1):
            if (array[i] % j == 0):
                count += 1
            
        if (count == 2):
            prime_array.append(array[i])

    return prime_array