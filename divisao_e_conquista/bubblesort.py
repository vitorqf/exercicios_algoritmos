def bubbleSort(array):
    length = len(array)
    aux = 0

    # Vai de 0 até a ultima posição do array passado
    for j in range(length - 1):

        # Vai de 0 até a ultima posição verificada - 1
        for i in range(length - 1 - j):

            # Se o valor na posição 1, for menor que o valor da posição 1 + 1
            if(array[i] > array[i + 1]):

                # faça o swap para que a posição 1 + 1 seja maior que a 1
                aux = array[i]
                array[i] = array[i + 1]
                array[i + 1] = aux

    return array
