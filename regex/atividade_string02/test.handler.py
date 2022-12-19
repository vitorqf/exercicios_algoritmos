import unittest
from handler import string_handle

class TestHandler(unittest.TestCase):
    def test_string_handle(self):
        self.assertEqual(string_handle("Hallo, dies ist eine\n"
"ziemlich lange Zeile, die in Html\n"
"aber nicht umgebrochen wird.\n"
"<br>\n"
"Zwei <br> <br> produzieren zwei Newlines.\n"
"Es gibt auch noch das tag <hr> was einen Trenner darstellt\n"
"Zwei <hr> <hr> produzieren zwei Horizontal Rulers.\n"
"Achtung mehrere Leerzeichen irritieren\n"
"Html genauso wenig wie\n"
"mehrere Leerzeilen.\n"), 
                                        
                                        """Hallo, dies ist eine ziemlich lange Zeile, die in Html aber nicht umgebrochen
                                        wird.
                                        Zwei

                                        produzieren zwei Newlines. Es gibt auch noch das tag
                                        --------------------------------------------------------------------------------
                                        was einen Trenner darstellt. Zwei
                                        --------------------------------------------------------------------------------
                                        --------------------------------------------------------------------------------
                                        produzieren zwei Horizontal Rulers. Achtung mehrere Leerzeichen irritieren Html
                                        genauso wenig wie mehrere Leerzeilen.""")