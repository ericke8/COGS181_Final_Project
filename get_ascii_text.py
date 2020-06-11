from art import *
import os

text_file = os.path.abspath('./data/tiny-shakespeare.txt')
output_file = os.path.abspath('./data/ascii-text.txt')


reading = open(text_file, 'r')
out = open(output_file, 'w')

while True:
    line = reading.readline()
    words = line.strip().split()
    for word in words:
        if word:
            art = text2art(word)
            out.write(art)

    if not line:
        break
out.close()
reading.close()