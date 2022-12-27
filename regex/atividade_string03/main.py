"""

1 - Remover caracteres não numericos
2 - Extrair os 11 primeiros dígitos
3 - Somar o restante

Saída:
11122233344


"""

import re

def get_cpf_and_code_from_breach(data_breach: str) -> str:

    clear_data_breach_lines = [re.findall('[\d+\.+]', line) for line in data_breach]

    cpf = ''.join(clear_data_breach_lines[0][0:11])

    remaining_first_line = clear_data_breach_lines[0][11::]

    return clear_data_breach_lines

contents = []

while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

print(get_cpf_and_code_from_breach(contents))


