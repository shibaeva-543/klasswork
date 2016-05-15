import random
__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-

def analyser(numbers, alph):
    summ = 0
    name = input()
    while name != 'stop':
        f = open(name, 'r')
        symbols = f.read()
        for i in range(len(symbols)):
            if symbols[i] in numbers:
                numbers[symbols[i]] += 1
                summ += 1
        name = input()
    return summ


class Monoalphabet:
    alphabet = ""  # FIXME

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}  # FIXME

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        pass  # FIXME


#key = Monoalphabet.alphabet[:]
#random.shuffle(key)
#cipher = Monoalphabet(key)
#line = input()
#while line:
#    print(cipher.encode(line))
#    line = input()


alph = "àáâãäå¸æçèéêëìíîïğñòóôõö÷øùúûüışÿÀÁÂÃÄÅ¨ÆÇÈÉÊËÌÍÎÏĞÑÒÓÔÕÖ×ØÙÚÛÜİŞß"
numbers = dict()
for i in range(len(alph)):
    numbers[alph[i]] = 0
summ = analyser(numbers, alph)
alph = alph[0:33]
for i in range(len(alph)):
    numbers[alph[i]] += numbers[alph[i].upper()]
    numbers[alph[i]] /= summ
print(numbers, summ)