import unittest

from handler import string_handle

class TestHandler(unittest.TestCase):
    def test_string_handle(self):

        # Se for inserido uma string suja mas com letras l, o ou O, ela deve remover todos caracteres não números e retornar um inteiro menor que 32 bits
        self.assertEqual(string_handle('loO6,   67;  DADSAD, 13. 4'), 100667134)

        # Se for inserido uma string vazia ou só dado um enter, deve ser retornado um ValueError e impresso 'error'
        with self.assertRaises(ValueError):
            string_handle('\n')

        # Se for inserido uma string que ao ser processada não gere nada, deve ser retornado um ValueError e impresso 'error'
        with self.assertRaises(ValueError):
            string_handle('hi')

        # Se for inserido uma string que ao ser processada gere um número maior que 32 bits, deve ser retornado um ValueError e impresso 'error'
        with self.assertRaises(ValueError):
            string_handle('2200000000')


if __name__ == '__name__':
    unittest.main()