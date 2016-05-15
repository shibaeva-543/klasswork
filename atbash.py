__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {self.alphabet[i]:self.alphabet[-i-1] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[-i-1].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])
        


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
cipher = Atbash()
line = fin.readline()
while line:
    print(cipher.encode(line), file = fout)
    line = fin.readline()
fout.close()