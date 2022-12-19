import re

"""

1 - print_width = 80
2 - <br> = \n
3 - <hr> = \n--------------------------------------------------------------------------------\n
4 - lastline = \n
5 - abc,123 = palavra
6 - abc, 123 = duas palavras

"""

def string_handle(base_string):
    remove_newline = re.sub('\n', ' ', base_string)

    replace_br_tag = re.sub('([\\s]?<br>[\\s]?)', '\\n', remove_newline)

    replace_hr_tag = re.sub('\\s?<hr>\\s?', '\n--------------------------------------------------------------------------------\n', replace_br_tag)

    print_width_80 = re.sub('(?![^\n]{1,80}$)([^\n]{1,80})\\s', '\\1\\r', replace_hr_tag)

    final_string = print_width_80

    return final_string