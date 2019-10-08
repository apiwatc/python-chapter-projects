#! /usr/bin/python

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    # add '*' to lists that were copied from Wiki
    lines[i] = '* ' + lines[i].strip()
text = '\n'.join(lines)
pyperclip.copy(text)
