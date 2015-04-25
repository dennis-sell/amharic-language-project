import codecs
# -*- coding: utf-8 -*-

#file1: english, file2: amharic
def process(file1, file2):
    english = open(file1 + ".txt")
    amharic = codecs.open(file2 + ".txt", "r", "utf-8")
    english_out = open(file1 + "_cleaned.txt", "w")
    amharic_out = open(file2 + "_cleaned.txt", "w")

    english_chapter_ends = []
    counter = 0
    for line in english:
        if len(line.strip()) == 0:
            continue
        if ']' in line:
            i = line.index(']')
        else: #hit a chapter end
            english_chapter_ends.append(counter)
            i = -1
        english_out.write(line[i+1:])
        counter+=1

    amharic_counter = 0
    for line in amharic:
        if u'\u1364' in line:
            i = line.index(u'\u1364')
        else: #hit the end of chapter
            end = english_chapter_ends.pop(0)
            if amharic_counter <= end-1:
                amharic_out.write('\n')
                amharic_counter +=1
            i = -1
        amharic_out.write(line[i+1:].encode('utf-8'))
        amharic_counter +=1

process("eng_genesis", "genesis")