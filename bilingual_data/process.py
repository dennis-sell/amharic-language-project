import codecs
# -*- coding: utf-8 -*-

english = open("eng_genesis.txt")
amharic = codecs.open("genesis.txt", "r", "utf-8")

english_out = open("eng_genesis_cleaned.txt", "w")
amharic_out = open("genesis_cleaned.txt", "w")
for line in english:
    if ']' in line:
        i = line.index(']')
    else: 
        i = -1
    # print line[i+1:]
    english_out.write(line[i+1:])

for line in amharic:
    if u'\u1364' in line:
        i = line.index(u'\u1364')
    else: 
        i = -1
    # print line[i+1:]
    amharic_out.write(line[i+1:].encode('utf-8'))