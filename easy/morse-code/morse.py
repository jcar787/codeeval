#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
db = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
      '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
      '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S',
      '-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y',
      '--..':'Z','.----':'1','..---':'2','...--':'3','....-':'4',
      '.....':'5','-....':'6','--...':'7','---..':'8','----.':'9',
      '-----':'0'}
for test in test_cases:
    sentence = test.strip().split(' ')
    result = ''

    for word in sentence:
        if word:
            result += db[word]
        else:
            result += ' '

    print result
test_cases.close()
