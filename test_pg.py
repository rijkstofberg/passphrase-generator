#!/bin/python

import unittest

from pg import PassphraseGenerator


class TestMatrixMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_number_generator(self):
        pg = PassphraseGenerator() 
        rstart = 1
        rstop = 6
        number = pg.generate_random_number(rstart, rstop)
        self.assertIn(number, range(rstart, rstop+1),
                'Number %s not in expected range.' % number)

    def test_read_words(self):
        pg = PassphraseGenerator()
        self.assertTrue(pg.words != None, 'Word list is uninitialised!')
        self.assertTrue(pg.words != {}, 'Word list is empty!')

    def test_read_words_bad_file_urn(self):
        pg = PassphraseGenerator('empty_file.txt')
        self.assertTrue(pg.words == {}, 'Word list is empty!')

    def test_generate_random_word_key(self):
        pg = PassphraseGenerator()
        key = pg.generate_random_word_key(length=5, rstart=1, rstop=6)
        self.assertEqual(len(key), 5, 'The key must be 5 chars long!')

    def test_generate_passphrase(self):
        pg = PassphraseGenerator()

        phrase = pg.generate_passphrase(
                phrase_length=2, key_length=5, rstart=1, rstop=6)
        self.assertEqual(len(phrase.split(' ')), 2, 'Phrase incorrect length!')

        phrase = pg.generate_passphrase(
                phrase_length=5, key_length=5, rstart=1, rstop=6)
        self.assertEqual(len(phrase.split(' ')), 5, 'Phrase incorrect length!')

if __name__ == '__main__':
    unittest.main()
