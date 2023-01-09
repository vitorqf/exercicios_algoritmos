import re

def get_info_from_breach(data_breach: str) -> str:

    # Pega todos digitos e o primeiro ponto para cada linha da string
    clear_data_breach_lines = [re.findall('[\d+\.{1}]', line) for line in data_breach]

    # Da primeira linha, irá pegar os 11 primeiros digitos para completar o cpf
    cpf = ''.join(clear_data_breach_lines[0][0:11])

    # Irá extrair os digitos restantes da primeira linha e a segunda linha por completa
    remaining_first_line = ''.join(clear_data_breach_lines[0][11::])
    remaining_second_line = ''.join(clear_data_breach_lines[1])

    # Irá converter ambas em float e somar para gerar o código do corrupto
    remaining_digits_sum = float(remaining_first_line) + float(remaining_second_line)

    breacher = f"cpf {cpf}\n{remaining_digits_sum}"

    return breacher
    
contents = []

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")

while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

print(get_info_from_breach(contents))


