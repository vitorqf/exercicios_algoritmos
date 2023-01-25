import re

test_str = \
"""
<html>
<head><title>Exercícios</title></head>
<body>
<h1>Exercícios</h1>
<table>
<thead>
<th>#</th>
<th>Questão</th>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Primeiro exercício de regex</td>
</tr>
</tbody>
</table>
</html>

Encontrei os endereços de e-mail da seguinte frase
'purple alice@google.com, blah monkey bob@abc.com blah dishwasher, aluis+io@ifrn.edu.br'
"""

PATTERNS = {
    'h1': r'<h1>(.*?)</h1>',
    'emails': r'[\w\.-]+@[\w\.-]+'
}

def get_h1_from_text(text: str) -> list:
    h1_occur = re.findall(PATTERNS['h1'], text)
    return h1_occur

def get_emails_from_text(text: str) -> list:
    email_ocurr = re.findall(PATTERNS['emails'], text)
    return email_ocurr

if __name__ == '__main__':
    h1_occur = get_h1_from_text(test_str)
    email_ocurr = get_emails_from_text(test_str)
    print(f'Textos dentro de tag <h1>:\n{h1_occur}')
    print(f'\nE-mails identificados:\n{email_ocurr}')