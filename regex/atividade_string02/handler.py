import re

def string_handle(base_string):
    print('BASE STRING\n', base_string)

    # Identifica as quebras de linha e as troca por um espaço
    remove_newline = re.sub('\\n', ' ', base_string)

    print('\n1 STEP\n', remove_newline)

    # Identifica a tag <hr> quando está isolada ou acompanhada de espaços em um dos lados e a troca por 80 hifens
    replace_hr_tag = re.sub('[\\s]?<hr>[\\s]?', '\\r--------------------------------------------------------------------------------', remove_newline)

    print('\n2 STEP\n', replace_hr_tag)
    
    # Identificada a tag <br> quando está isolada ou acompanhada de espaço em um dos lados e a troca por 1 quebra de linha
    replace_br_tag = re.sub('[\\s]?<br>[\\s]?', '\\n', replace_hr_tag)

    print('\n3 STEP\n', replace_br_tag)

    # Identifica os primeiros quaisquer 80 caracteres de uma linha e os substitui pelo próprio grupo de captura + um carriage return para não haver quebra de linha excedente
    print_width_80 = re.sub("(.{80})", "'\\1\\r", replace_br_tag)