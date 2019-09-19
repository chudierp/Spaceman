from spaceman import is_word_guessed
from spaceman import get_guessed_word
from spaceman import is_guess_in_word
import unittest

class SpacemanTests(unittest.TestCase):
    def test_is_word_guessed(self): 
        fake_word = "Chu"
        letters_guessed = ["a", "b", "c"]
        
        self.assertEqual(is_word_guessed(fake_word, letters_guessed), False)
        
    def test_get_guessed_word(self):
        assert get_guessed_word('fish', ['i', 's', 'h'] ) == "_ i s h "

    def test_is_guess_in_word(self):
        assert is_guess_in_word('i',['f', 'i', 's', 'h']) is True    
    
   
  
if __name__== '__main__':
    unittest.main()
