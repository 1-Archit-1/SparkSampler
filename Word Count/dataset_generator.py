""" Script to create text files for word count"""

import random

file1 = open("largest.txt","a") 
words_list_small = [ "apple", "banana", "grape", "orange",  "lychee", "persimmon", "cucumber", "peach",  "coconut", "lemon", "lime", "pomegranate", "apricot","fig", "date"]
index = 0
#Increase the range to make a bigger file
for x in range(590000000):
    index = random.randint(0,len(words_list_small)-1)
    file1.write(words_list_small[index])
    if x%4==0:
        file1.write('\n')