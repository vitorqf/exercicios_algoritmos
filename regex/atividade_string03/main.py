"""

1 - Remover caracteres não numericos
2 - Extrair os 11 primeiros dígitos
3 - Somar o restante

Saída:
11122233344


"""

import re

def handler(string):
    breach_output = {}

    get_digits_from_cpf = re.findall('[\\d]', string)

    join_get_digits_from_cpf = ''.join(get_digits_from_cpf[0:10])

    breach_output['cpf'] = join_get_digits_from_cpf

    return breach_output

contents = []

while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

contents = ''.join(contents)

print(handler(contents))


