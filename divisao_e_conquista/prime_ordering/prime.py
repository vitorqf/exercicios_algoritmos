def prime(array):
    # Para cada posição na array passada
    for i in range(len(array)):
        # Inicia o contador de divisão em 0
        count = 0

        # Vai de 1 até o valor dentro da posição do array + 1, isto é, de 1 até 4, por exemplo
        for j in range(1, array[i] + 1):

            # Se de 1 a 4, 4 for divisivel por um dos números, então, o contador aumenta 1
            if (array[i] % j == 0):
                count += 1
            
        # Se a quantidade de divisões for exatamente duas, retorna o valor
        if (count == 2):
            return array[i]
