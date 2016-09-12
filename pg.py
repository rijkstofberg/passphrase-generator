#!/bin/python

import random

class PassphraseGenerator:

    def __init__(self, file_urn='word_list.txt'):
        self.words = self.read_words(file_urn)


    def read_words(self, urn):
        words = {}
        with open(urn) as data:
            for line in data:
                (key, val) = line.split(':')
                words[key] = val.strip()
        return words


    def generate_random_number(self, rstart=1, rstop=6):
        return random.randint(rstart, rstop)


    def generate_random_word_key(self, length=5, rstart=1, rstop=6):
        key = []
        for i in range(0, length):
            key.append(self.generate_random_number(rstart, rstop))
        return ''.join(str(k) for k in key)


    def get_word_by_number(self, target_number):
        return self.words.get(target_number, '')


    def generate_passphrase(self, phrase_len=5, key_len=5, rstart=1, rstop=6):
        phrase = []
        for i in range(0, phrase_len):
            word = ''
            while word == '':
                rand_number = self.generate_random_word_key(
                    key_len, rstart, rstop)
                word = self.get_word_by_number(rand_number)
                print 'Missed key %s' %rand_number
            phrase.append(word)

        return ' '.join(phrase).strip(' ')


if __name__ == '__main__':
    pg = PassphraseGenerator()
    phrase = pg.generate_passphrase(
        phrase_len=5, key_len=5, rstart=1, rstop=6)
    print phrase
