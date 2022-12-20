"""
Sua tarefa é escrever um pequeno navegador html. Ele deve exibir apenas o conteúdo do arquivo de entrada e conhecer apenas os comandos html (tags) que é uma quebra de linha e que é uma régua horizontal. Em seguida, você deve tratar todos os tabuladores, espaços e novas linhas como um espaço e exibir o texto resultante com no máximo 80 caracteres por linha.

Entrada
A entrada consiste em um texto que você deve exibir. Este texto consiste em palavras e tags HTML separadas por um ou mais espaços, tabulações ou novas linhas. Uma palavra é uma sequência de letras, números e pontuação. Por exemplo, "abc,123" é uma palavra, mas "abc, 123" são duas palavras, ou seja, "abc" e "123". Uma palavra é sempre menor que 81 caracteres e não contém nenhum '<' ou '>'. Todas as tags HTML são <br> ou <hr>.

Resultado
Você deve exibir o texto resultante usando estas regras:

Se você ler uma palavra na entrada e a linha resultante não tiver mais de 80 caracteres, imprima-a, caso contrário, imprima-a em uma nova linha.

Se você ler um <br> na entrada, comece uma nova linha.

Se você ler um <hr> na entrada, inicie uma nova linha, a menos que já esteja no início de uma linha, exiba 80 caracteres de '-' e inicie uma nova linha (novamente).

A última linha é finalizada por um caractere de nova linha.


Entrada: 
Hallo, dies ist eine
ziemlich lange Zeile, die in Html
aber nicht umgebrochen wird.
<br>
Zwei <br> <br> produzieren zwei Newlines.
Es gibt auch noch das tag <hr> was einen Trenner darstellt.
Zwei <hr> <hr> produzieren zwei Horizontal Rulers.
Achtung mehrere Leerzeichen irritieren
Html genauso wenig wie
mehrere Leerzeilen.


Saída: 
Hallo, dies ist eine ziemlich lange Zeile, die in Html aber nicht umgebrochen
wird.
Zwei

produzieren zwei Newlines. Es gibt auch noch das tag
--------------------------------------------------------------------------------
was einen Trenner darstellt. Zwei
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
produzieren zwei Horizontal Rulers. Achtung mehrere Leerzeichen irritieren Html
genauso wenig wie mehrere Leerzeilen.

"""

from handler import string_handle

# print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")

# contents = []

# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     contents.append(line)

# contents = '\n'.join(contents)

test_str = ("Hallo, dies ist eine\n"
	"ziemlich lange Zeile, die in Html\n"
	"aber nicht umgebrochen wird.\n"
	"<br>\n"
	"Zwei <br> <br> produzieren zwei Newlines.\n"
	"Es gibt auch noch das tag <hr> was einen Trenner darstellt.\n"
	"Zwei <hr> <hr> produzieren zwei Horizontal Rulers.\n"
	"Achtung mehrere Leerzeichen irritieren\n"
	"Html genauso wenig wie\n"
	"mehrere Leerzeilen.\n")

print('\n\n\nResult:\n\n')
print(string_handle(test_str))