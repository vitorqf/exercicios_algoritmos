class Funcoes:
    def somatorio(n):
        if (n == 0):
            return 0

        elif (n < 0):
            return n + Funcoes.somatorio(n + 1)

        else:
            return n + Funcoes.somatorio(n - 1)

    def inputReader(x, y, sum):
        choice = int(input("\nDigite 1 para somar novamente\n==> "))
        sum += x + y
        
        match choice:
            case 1:
                x = int(input("\nInsira X: "))
                y = int(input("Insira Y: "))
                return Funcoes.inputReader(x, y, sum)
            
            case _:
                return sum
    
    def procura(x, v, n):
        if (v[n] == x):
            return n

        else:
            return Funcoes.procura(x, v, n - 1)

    def fibonacci():
        pass

print(f"\n{' Questao 01 ':=^40}\n")

n = 10

print(f"Resultado: {Funcoes.somatorio(n)}")

print(f"\n{' Questao 02 ':=^40}\n")

first_x = int(input("Insira X: "))
first_y = int(input("Insira Y: "))
sum = 0

print(f"\nSoma total: {Funcoes.inputReader(first_x, first_y, sum)}")

x = 4
v = [0, 1, 2, 3, 4, 10]
n = 2

print(f"\n{' Questao 03 ':=^40}\n\nPosicao em que X esta presente: v[{Funcoes.procura(x, v, n)}]")

print(f"\n{' Questao 04 ':=^40}\n")
print("a) ")