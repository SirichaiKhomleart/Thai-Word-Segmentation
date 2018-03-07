import json
#for file input dialog
import tkinter as tk 
from tkinter import filedialog
#for interact with terminal
import os
import signal
import subprocess
import sys
import re

def searching(word):
    if word in dictionary:
##        print(word, "This word is in a dictionary.")
        return True
    else:
        return False

def create_candidate(sentenceList,pointer,lenghtList,line):
    if pointer == lenghtList:       #base case
        return sentenceList
    else:                               #recursive loop
        current_word = sentenceList[pointer]+sentenceList[pointer+1]
##        print(current_word)
        if any([l.startswith(current_word) for l in dictionary]):            
            sepList2 = list(sentenceList)
            current_word2 = current_word
            while(any([l.startswith(current_word2) for l in dictionary])):
##                print("Type: "+str(type(sepList2))+current_word2)
                if(pointer != len(sepList2)-2):
                    sepList2[pointer] = sepList2[pointer]+sepList2[pointer+1]
                    del sepList2[pointer+1]
                    current_word2 = sepList2[pointer]+sepList2[pointer+1]
                    if searching(current_word2):
##                        print("Run candidate"+str(pointer)+" "+str(len(sepList2)-1))
                        sepList2 = create_candidate(sepList2,pointer,len(sepList2)-1,line)
                        if(sepList2!=None):
##                            print(sepList2,pointer)
                            candidate[line].append(sepList2)
                        return
                else:
                    break
        if searching(current_word):
            sepList = list(sentenceList)
            sepList3 = list(sentenceList)
            sepList[pointer] = sepList[pointer]+sepList[pointer+1]
            del sepList[pointer+1]
            sepList = create_candidate(sepList,pointer,lenghtList-1,line) 
            sepList3 = create_candidate(sepList3,pointer+1,lenghtList,line)
            if(sepList!=None):
##                print(sepList,pointer)
                candidate[line].append(sepList)
            if(sepList3!=None):
##                print(sepList3,pointer)
                candidate[line].append(sepList3)            
            return
        else:
            sepList4 = list(sentenceList)
            sepList4 = create_candidate(sepList4,pointer+1,lenghtList,line)
            if(sepList4==None):
                return;
##            print(sepList4,pointer)
            candidate[line].append(sepList4)
            
##dictionary = json.load(open('thaiwordlist.json', encoding="utf8"))
with open("thaiwordlist.txt", encoding="utf8") as f:
    dictionary = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
dictionary = [x.strip() for x in dictionary] 
dictionary2 = ["ทด","แทน","ท","ด","ส","อ","บ","ดอกเบี้ย","ทดสอบ","แบ่งคำ"]
print("Dictionary list is loaded")

f_input = [["ท","ด","ส","อ","บ","กา","ร","แบ่","ง","คำ"],
           ["เสา","ร์","นี้","ไป","ไห","น","ไก่","กา","ตา","ก","ล","ม","จับ","ตา","ดู","ด","อ","ก","เบี้ย"]]
f_input2 = [["ค","บ","ค","น","พา","ล","พา","ไป","หา","ผิ","ด","ค","บ","บัณ","ฑิต","บัณ","ฑิต","พา","ไป","หา","ผ","ล"]]

candidate = []
line = 0
for sentence in f_input2:
    candidate.append([])
    create_candidate(sentence,0,len(sentence)-1,line)
    line += 1

