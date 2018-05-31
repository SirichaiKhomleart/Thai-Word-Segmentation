print("Compatible with python 3 only.")


#import important features
import json
import tkinter as tk
from tkinter import filedialog
import os
import signal
import subprocess
import sys
import re
import time
import math



#Initial setup
#Loading text file
if(os.path.isfile("thaiword.txt")):
    input_file_path = "thaiword.txt"
else:
    print("Please input plain text file")
    input_file_path = filedialog.askopenfilename()
print("--> Reading plain text file...")
with open(input_file_path,encoding = "utf8") as f:
    mylist = f.read().splitlines()
inputfile = [list(x) for x in mylist]
print(mylist)
if ('\ufeff' in inputfile[0]):
    inputfile[0].remove('\ufeff')

#Loading Dictionary
if(os.path.isfile("thaiwordlist.txt")):
    thaidict_file_path = "thaiwordlist.txt"
else:
    print("Please input Thai dictionary file")
    thaidict_file_path = filedialog.askopenfilename()
print("--> Loading dictionary...")
with open(thaidict_file_path, encoding="utf8") as f:
    dictionary = f.readlines()
dictionary = [x.strip() for x in dictionary]



#define function for create clusters and form candidates
def searching(word):
    if word in dictionary:
        #print("----> '" + word + "' --> This word found in dictionary.")
        return True
    else:
        return False

def create_candidate(sentenceList, pointer, lenghtList, line, token):
    global counter
    if (pointer > lenghtList) or ((pointer >= lenghtList) and (sentenceList[pointer] in sym)):  # base case
        return sentenceList
    else:  # recursive loop
        current_word = sentenceList[pointer]
        if searching(current_word):
            token = 0
            sepList1 = list(sentenceList)
            sepList1 = create_candidate(sepList1, pointer + 1, lenghtList, line, token)
            if (sepList1 != None) and (sepList1 != []):
                counter += 1
                candidate[line].append(sepList1)
            if (any([l.startswith(current_word) for l in dictionary])) and (not pointer + 1 > lenghtList):
                if (token == 0):
                    token = 1
                elif (token == 1):
                    token = 2
                sepList2 = list(sentenceList)
                sepList2[pointer] = sepList2[pointer] + sepList2[pointer + 1]
                del sepList2[pointer + 1]
                sepList2 = create_candidate(sepList2, pointer, lenghtList - 1, line, token)
            return
        elif (not searching(current_word)) and (not pointer + 1 > lenghtList):
            if (any([l.startswith(current_word) for l in dictionary])):
                if (token == 0):
                    token = 1
                elif (token == 1):
                    token = 2
                sepList3 = list(sentenceList)
                sepList3[pointer] = sepList3[pointer] + sepList3[pointer + 1]
                del sepList3[pointer + 1]
                sepList3 = create_candidate(sepList3, pointer, lenghtList - 1, line, token)
                a = 1
                if (sepList3 == [] and token == 1):
                    while sepList3 == []:
                        token = 0
                        sepList3 = list(sentenceList)
                        sepList3 = create_candidate(sepList3, pointer + a, lenghtList, line, token)
                        a += 1
                elif (sepList3 == [] and token == 2):
                    return []
            elif (current_word == " ") or (current_word in sym):
                token = 0
                sepList1 = list(sentenceList)
                sepList1 = create_candidate(sepList1, pointer + 1, lenghtList, line, token)
                if (sepList1 != None) and (sepList1 != []):
                    counter += 1
                    candidate[line].append(sepList1)
            else:
                return []

def merge_back(pointer, namelist):
    namelist[pointer] = namelist[pointer] + namelist[pointer + 1]
    del namelist[pointer + 1]
    return namelist

def merge_front(pointer, namelist):
    namelist[pointer] = namelist[pointer - 1] + namelist[pointer]
    del namelist[pointer - 1]
    return namelist



#define function for calculate probability
def prob(word):
    flag = False
    for i in range(len(index)):
        if index[i][0] == word:
            flag = True
            return (index[i][1]) / (len(index))
    if flag == False:
        return 0

def probGiven(word2, word1):  ##Probability word2 after word 1 ## "ตัวอย่าง" word1=ตัว word2=อย่าง
    CombineWord = str(word1) + " " + str(word2)
    flag2 = False
    for i in range(len(index2)):
        if index2[i][0] == CombineWord:
            flag2 = True
            return (index2[i][1]) / (len(index2))
    if flag2 == False:
        return 0

def smallMonogram(word1):
    P1 = prob(word1)
    return P1

def monogram(group):
    sum = 1
    for i in range(len(group) - 1):
        word1 = group[i]
        sum *= smallMonogram(word1)
    return sum

def smallBigram(word2, word1):
    P1 = prob(word1)
    P21 = probGiven(word2, word1)
    if P21 == 0:
        return 0
    else:
        return P1 / P21

def bigram(group):
    sum = 1
    for i in range(len(group) - 1):
        word1 = group[i]
        word2 = group[i + 1]
        sum *= smallBigram(word2, word1)
    return sum

def probGiven2(word3, word2, word1):
    flag3 = False
    CombineWord = str(word1) + " " + str(word2) + " " + str(word3)
    for i in range(len(index3)):
        if index3[i][0] == CombineWord:
            flag2 = True
            return (index3[i][1]) / (len(index3))
    if flag3 == False:
        return 0

def smallTrigram(word3, word2, word1):
    P21 = probGiven(word2, word1)
    P321 = probGiven2(word3, word2, word1)
    if P21 == 0:
        return 0
    else:
        return P321 / P21

def trigram(group):
    sum = 1
    for i in range(len(group) - 2):
        word1 = group[i]
        word2 = group[i + 1]
        word3 = group[i + 2]
        sum *= smallTrigram(word3, word2, word1)
    return sum



#Set timer for measure execution time
starttime = time.time()
print("Thai Word Segmentation Start!")



#Main Program
#Step 1: Word Clustering
print("--> Begin Word Clustering")
counter = 0
front_vowel = ["เ","แ","โ","ใ","ไ"]
back_vowel = ["ะ","า","ิ","ี","ึ","ื","ุ","ู","ั","ำ","ๅ","์","ํ","่","้","๊","๋","็"]
sym = ["1","2","3","4","5","6","7","8","9","0","ฯ",",","!","@","#","$","%","^","&","*","+","-","/","\'","_","ๆ","ฯ",".",":",";","(",")","[","]","{","}","|","๑","๒","๓","๔","๕","฿","๖","๗","๘","๙","๐","?","๚","<",">"]
blank_line=[] ##handle blank line in input file
inputfile_noblank=[]
for i in range(len(inputfile)):  ##handle blank line in input file
    if (len(inputfile[i])==0):
        blank_line.append(i)
    else:
        inputfile_noblank.append(inputfile[i])
inputfile=inputfile_noblank
for i in range(len(inputfile)):
    j = 0
    while inputfile[i][j] != None:
        checker = inputfile[i][j]
        if checker in front_vowel:
            inputfile[i] = merge_back(j,inputfile[i])
        elif checker in back_vowel:
            inputfile[i] = merge_front(j,inputfile[i])
            j = j-1
            while (checker == "ั" or checker == "ื") and inputfile[i][j][-1] in back_vowel:
                inputfile[i] = merge_back(j,inputfile[i])
            if (checker == "ื" or checker == "ี") and ("เ" in inputfile[i][j]) and (inputfile[i][j][-1] != "ย" and inputfile[i][j][-1] != "อ"):
                y = j
                while (inputfile[i][j][-1] != "ย" and inputfile[i][j][-1] != "อ"):
                    inputfile[i] = merge_back(j,inputfile[i])
                    y = y+1
        j = j+1
        if j == len(inputfile[i]):
            break
#print("----> Generated Cluster: ",inputfile)

#Step 2: Candidate Formation
print("--> Begin Candidate Formation")
candidate = []
line = 0
for sentence in inputfile:
    candidate.append([])
    create_candidate(sentence,0,len(sentence)-1,line,0)
    line += 1
#for i in range(len(candidate)):
    #for j in range(len(candidate[i])):
         #print("----> Line "+str(i+1)," Candidate "+str(j+1),candidate[i][j])

#Step 3: Probability Calculation
print("--> Begin Probability Calculation")
candidate_array=candidate

#Counting probability for monogram
index_array = []
index_array_count = []
index = []
for line in candidate_array:
    for group in line:
        for word in group:
            if word in index_array:
                index_array_count[index_array.index(word)] += 1
            else:
                index_array.append(word)
                index_array_count.append(1)
for i in range(len(index_array)):
    index.append([index_array[i], index_array_count[i]])

#Counting probability for bigram
index2_array = []
index2_array_count = []
index2 = []
for line in candidate_array:
    for group in line:
        for i in range(len(group) - 1):
            combineWord = str(group[i]) + " " + str(group[i + 1])
            if combineWord in index2_array:
                index2_array_count[index2_array.index(combineWord)] += 1
            else:
                index2_array.append(combineWord)
                index2_array_count.append(1)
for i in range(len(index2_array)):
    index2.append([index2_array[i], index2_array_count[i]])

#Counting probability for trigram
index3_array = []
index3_array_count = []
index3 = []
for line in candidate_array:
    for group in line:
        for i in range(len(group) - 2):
            combineWord = str(group[i]) + " " + str(group[i + 1]) + " " + str(group[i + 2])
            if combineWord in index3_array:
                index3_array_count[index3_array.index(combineWord)] += 1
            else:
                index3_array.append(combineWord)
                index3_array_count.append(1)
for i in range(len(index3_array)):
    index3.append([index3_array[i], index3_array_count[i]])

#Calculate probability (Using Minimum Word Count > Trigram > Bigram > Monogram)
answer = []
error=False
for line in candidate_array:
        minwordIndex = math.inf
        for i in range(len(line)):
            if len(line[i]) < minwordIndex:
                minwordIndex = len(line[i])
        selectCandidate = []
        for j in range(len(line)):
            if len(line[j]) == minwordIndex:
                selectCandidate.append(line[j])
        ##print(selectCandidate)
        if len(selectCandidate) == 1:
            answer.append(selectCandidate[0])
        else:
            maxprob = 0
            maxprobIndex = 0
            ##print("candidate more than one")
            ##print(selectCandidate)
            maxprobArray = []
            for i in range(len(selectCandidate)):
                currprob = trigram(selectCandidate[i])
                if currprob > maxprob:
                    maxprob = currprob
            for i in range(len(selectCandidate)):
                if (trigram(selectCandidate[i]) == maxprob):
                    maxprobArray.append(selectCandidate[i])
            if (len(maxprobArray) == 1):
                answer.append(selectCandidate[0])
            elif (len(maxprobArray) < 1):
                #print("----> Error occur with maxprobArray")
                error=True
                answer.append(["<<This line contains unacceptable characters/language>>"])


            else:
                maxprobBI = 0
                maxprobIndexBI = 0
                ##print("candidate bigram inside trigram more than one")
                ##print(selectCandidate)
                maxMonogramProb = []
                for i in range(len(maxprobArray)):
                    currprobBI = bigram(maxprobArray[i])
                    if currprobBI > maxprobBI:
                        maxprobBI = currprobBI
                for i in range(len(maxprobArray)):
                    if (bigram(maxprobArray[i]) == maxprobBI):
                        maxMonogramProb.append(maxprobArray[i])
                if (len(maxMonogramProb) == 1):
                    answer.append(maxMonogramProb[0])
                elif (len(maxMonogramProb) < 1):
                    #print("----> Error occur with maxMonogramProb")
                    error=True
                    answer.append(["<<This line contains unacceptable characters/language>>"])
                else:
                    maxprobMONO = 0
                    maxprobIndexMONO = 0
                    ##print("candidate monogram inside bigram more than one")
                    ##print(selectCandidate)
                    for i in range(len(maxMonogramProb)):
                        currprobMONO = monogram(maxMonogramProb[i])
                        if currprobMONO > maxprobMONO:
                            maxprobMONO = currprobMONO
                            maxprobIndexMONO = i
                            ##print("currprob " + str(currprob))
                    answer.append(maxMonogramProb[maxprobIndexMONO])
answer_withBlankLine=[]
temp=len(answer)+len(blank_line)
counter=0
try:
    for i in range(temp):
        if i in blank_line:
            answer_withBlankLine.append([])
            counter+=1
        else:
            answer_withBlankLine.append(answer[i-counter])
    answer=answer_withBlankLine
except:
    error=True
if (error==True):
    print("\n<<< Error occured! >>>\n<<< There are some unacceptable characters inside input text file >>>")
    print("<<< Other languages but Thai are not supported yet >>>\n<<< as well as special characters >>>\n")

print("Segmentation Done!\n")
print("-------answer-------")
for line in answer:
    print ("|".join(line))
print("--------------------\n")

#Calculate execution time
endtime = time.time()
print("Execution Time: "+str(endtime-starttime)+" seconds.")



# README!!!
# This is the university project that aims to the study of information retrieval.
# ------------------------------
# Sirindhorn International Institute of Technology
# Thammasat University
#
# CSS432 - Information Retrieval          Section 1
# Semester 2          Year 2017
#
# Members
# 1     5822781910    Mr.Sirichai    Khomleart
# 2     5822782421    Mr.Pasin       Jiratthiticheep
# 3     5822782546    Mr.Nuttapol  Saiboonruen
