import re
import os

# Função para realizar limpeza do terminal com base no sistema operacional, caso kernel Windows, utiliza 'cls', caso linux e afins, utiliza 'clear'.
def clear():

    if os.name == 'nt':
        _ = os.system('cls') 

    else:
        _ = os.system('clear')

# Cor amarelo em ANSI
YELLOW = '\033[0;33m'

# Cor de escape
CLEAR = '\033[m'

# Busca o arquivo pelo nome e extensão
print('Insert your file name, including file extension. ex: db.txt')
filename = input('> ')

print('\nSearch below...')
search = input('> ')

with open(filename, 'r') as file:
    # É feito a leitura do arquivo passado
    for line in file:

        # Caso haja algum match entre o trecho do texto e a busca (regex, case-sensitive), é limpado o terminal e trocado o match pela mesma palavra, porém, com coloração diferente.
        if re.search(search, line):
            clear()

            print(re.sub(search, f"{YELLOW}{search}{CLEAR}", line))

            try:
                _ = input('Press ENTER to continue, or CTRL + C to exit.')

            except KeyboardInterrupt:
                print('\n[-] Exiting...')
                exit()

# Em caso de ver todos os matchs da mesma string, é encontrado o fim do arquivo e também em caso de não existir match.
print("\n[-] You've reached the end of file!")