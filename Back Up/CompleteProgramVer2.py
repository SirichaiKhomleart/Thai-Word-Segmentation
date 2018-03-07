print("Compatible with python 3 only.")
##print("This is Thai Segmentation quiz, but it look very like the final thesis for the forth-year students.")

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

root = tk.Tk()
root.withdraw()
print("Please input 'JTCC-0.1.jar' file")
jtcc_file_path = filedialog.askopenfilename() #get file path for JTCC-0.1.jar
##print("JTCC path is "+jtcc_file_path)
print("Please input plain text file")
plaintext_file_path = filedialog.askopenfilename() #get file path for plaintext.txt
##print("File path is "+plaintext_file_path)

plaintext_lines =  len(open(plaintext_file_path,'rb').read().splitlines())
##print("Number of lines in file is "+str(plaintext_lines))

##print("Command is ")
##print('java', '-jar',jtcc_file_path,'file',plaintext_file_path)



def get_output(cmd, until):
    linenumber=1
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    ret = []
    while True:
        ##print("current line:"+str(linenumber)+", until: "+str(until))
        line = p.stdout.readline()
        line = line.decode('utf8')
        ret.append(line)
        if str(linenumber)==str(until):
            break
        linenumber = linenumber+1
    p.kill()
    return ret

##print (''.join(get_output(['java','-jar',jtcc_file_path,'file',plaintext_file_path], until=plaintext_lines)))
clusterarray = [plaintext_lines]
clusterarray = get_output(['java','-jar',jtcc_file_path,'file',plaintext_file_path], until=plaintext_lines)


for i in range (len(clusterarray)):
    temp = clusterarray[i].split('|')
    clusterarray[i]=temp
    ##print ("current spliting at line: "+str(i))

print("Generate Cluster Done")
####This is for checking cluster array
##for i in range (len(clusterarray)):
##    for j in range (len(clusterarray[i])):
##        print("i: "+str(i)+" j: "+str(j)+" text: "+clusterarray[i][j])

for listtemp in clusterarray:
    ##print("list")
    ##print(listtemp)
    if '\n' in listtemp:
        listtemp.remove('\n')


def searching(word):
    if word in dictionary:
        print(word, "This word is in a dictionary.")
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
print("Dictionary list is loaded, matching start!")

f_input = clusterarray

candidate = []
line = 0
for sentence in f_input:
    candidate.append([])
    create_candidate(sentence,0,len(sentence)-1,line)
    line += 1

candidate_array=candidate

import math

##find the probability using bigram
print("Calculate probability")

##these are variables for monogram
index_array=[]
index_array_count=[]
index=[]

for line in candidate_array:
    for group in line:
        for word in group:
            if word in index_array:
                index_array_count[index_array.index(word)] += 1
            else:
                index_array.append(word)
                index_array_count.append(1)

for i in range (len(index_array)):
    index.append([index_array[i],index_array_count[i]])

##these are variable for bigram
index2_array=[]
index2_array_count=[]
index2=[]

for line in candidate_array:
    for group in line:
        for i in range (len(group)-1):
            combineWord = str(group[i])+" "+str(group[i+1])
            if combineWord in index2_array:
                index2_array_count[index2_array.index(combineWord)] += 1
            else:
                index2_array.append(combineWord)
                index2_array_count.append(1)

for i in range (len(index2_array)):
    index2.append([index2_array[i],index2_array_count[i]])

##these are variable for trigram
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


##Probability
def prob(word):
    flag = False
    for i in range (len(index)):
        if index[i][0]==word:
            flag = True
            return (index[i][1])/(len(index))
    if flag==False:
        return 0

def probGiven(word2,word1): ##Probability word2 after word 1 ## "ตัวอย่าง" word1=ตัว word2=อย่าง
    # P1 = prob(word1)
    CombineWord = str(word1)+" "+str(word2)
    flag2=False
    for i in range (len(index2)):
        if index2[i][0]==CombineWord:
            flag2=True
            return (index2[i][1])/(len(index2))
    if flag2==False:
        return 0
    
def smallMonogram(word1):
    P1=prob(word1)
    return P1

def monogram(group):
    sum = 1
    for i in range (len(group)-1):
        word1 = group[i]
        sum *= smallMonogram(word1)
    return sum

def smallBigram(word2,word1):
    P1=prob(word1)
    P21=probGiven(word2,word1)
    if P21==0:
        return 0
    else:
        return P1/P21

def bigram(group):
    sum = 1
    for i in range (len(group)-1):
        word1 = group[i]
        word2 = group[i+1]
        sum *= smallBigram(word2,word1)
    return sum

def probGiven2(word3,word2,word1):
    # P21 = probGiven(word2,word1)
    flag3 = False
    CombineWord = str(word1)+" "+str(word2)+" "+str(word3)
    for i in range (len(index3)):
        if index3[i][0] == CombineWord:
            flag2 = True
            return (index3[i][1]) / (len(index3))
    if flag3 == False:
        return 0

def smallTrigram(word3,word2,word1):
    P21 = probGiven(word2,word1)
    P321 = probGiven2(word3,word2,word1)
    if P21==0:
        return 0
    else:
        return P321/P21

def trigram(group):
    sum = 1
    for i in range (len(group)-2):
        word1 = group[i]
        word2 = group[i+1]
        word3 = group[i+2]
        sum *= smallTrigram(word3,word2,word1)
    return sum


##
##print('test')
##print(bigram(a0))
##print(bigram(a1))
##print(bigram(a2))
##print(bigram(a3))
##print(bigram(a4))
##print()
##
##print(index3)
##
##for line in candidate_array:
##    for group in line:
##        print(bigram(group))
##    print("-----------------")
##
##print("-----------------")
##print("-----------------")
##
##
##for line in candidate_array:
##    for group in line:
##        print("len: "+str(len(group))+" Prob:"+str(trigram(group))+" Word: ")
##        print(group)
##    print("-----------------")
##
##
##print("-----------------")
##print("-----------------")
print("Calculate probability using bigram")
answer=[]
for line in candidate_array:
    minwordIndex = math.inf
    for i in range (len(line)):
        if len(line[i])<minwordIndex:
            minwordIndex=len(line[i])
    selectCandidate=[]
    for j in range (len(line)):
        if len(line[j])==minwordIndex:
            selectCandidate.append(line[j])
    ##print(selectCandidate)
    if len(selectCandidate)==1:
        answer.append(selectCandidate[0])
    else:
        maxprob=0
        maxprobIndex=0
        ##print("candidate more than one")
        ##print(selectCandidate)
        for i in range (len(selectCandidate)):
            currprob = bigram(selectCandidate[i])
            if currprob>maxprob:
                maxprob=currprob
                maxprobIndex=i
            ##print("currprob " + str(currprob))
        answer.append(selectCandidate[maxprobIndex])

print("Segmentation Done!")
print("-------answer-------")
for line in answer:
    print ("|".join(line))
##print(answer)
print("-----------------------------------")
print("Calculate probability using trigram")
answer=[]
for line in candidate_array:
    minwordIndex = math.inf
    for i in range (len(line)):
        if len(line[i])<minwordIndex:
            minwordIndex=len(line[i])
    selectCandidate=[]
    for j in range (len(line)):
        if len(line[j])==minwordIndex:
            selectCandidate.append(line[j])
    ##print(selectCandidate)
    if len(selectCandidate)==1:
        answer.append(selectCandidate[0])
    else:
        maxprob=0
        maxprobIndex=0
        ##print("candidate more than one")
        ##print(selectCandidate)
        for i in range (len(selectCandidate)):
            currprob = trigram(selectCandidate[i])
            if currprob>maxprob:
                maxprob=currprob
                maxprobIndex=i
            ##print("currprob " + str(currprob))
        answer.append(selectCandidate[maxprobIndex])

print("Segmentation Done!")
print("-------answer-------")
for line in answer:
    print ("|".join(line))
##print(answer)
print("-----------------------------------")
print("Calculate probability using n-gram start from trigram")
answer=[]
for line in candidate_array:
    minwordIndex = math.inf
    for i in range (len(line)):
        if len(line[i])<minwordIndex:
            minwordIndex=len(line[i])
    selectCandidate=[]
    for j in range (len(line)):
        if len(line[j])==minwordIndex:
            selectCandidate.append(line[j])
    ##print(selectCandidate)
    if len(selectCandidate)==1:
        answer.append(selectCandidate[0])
    else:
        maxprob=0
        maxprobIndex=0
        ##print("candidate more than one")
        ##print(selectCandidate)
        maxprobArray=[]
        for i in range (len(selectCandidate)):
            currprob = trigram(selectCandidate[i])
            if currprob>maxprob:
                maxprob=currprob
        for i in range (len(selectCandidate)):
            if (trigram(selectCandidate[i])==maxprob):
                maxprobArray.append(selectCandidate[i])
        if (len(maxprobArray)==1):
            answer.append(selectCandidate[0])
        elif (len(maxprobArray)<1):
            print("error occur with maxprobArray")


        else:
            maxprobBI=0
            maxprobIndexBI=0
            ##print("candidate bigram inside trigram more than one")
            ##print(selectCandidate)
            maxMonogramProb=[]
            for i in range (len(maxprobArray)):
                currprobBI = bigram(maxprobArray[i])
                if currprobBI>maxprobBI:
                    maxprobBI=currprobBI
            for i in range (len(maxprobArray)):
                if (bigram(maxprobArray[i])==maxprobBI):
                    maxMonogramProb.append(maxprobArray[i])
            if (len(maxMonogramProb)==1):
                answer.append(maxMonogramProb[0])
            elif (len(maxMonogramProb)<1):
                print("error occur with maxMonogramProb")
            else:
                maxprobMONO=0
                maxprobIndexMONO=0
                ##print("candidate monogram inside bigram more than one")
                ##print(selectCandidate)
                for i in range (len(maxMonogramProb)):
                    currprobMONO = monogram(maxMonogramProb[i])
                    if currprobMONO>maxprobMONO:
                        maxprobMONO=currprobMONO
                        maxprobIndexMONO=i
                        ##print("currprob " + str(currprob))
                answer.append(maxMonogramProb[maxprobIndexMONO])
        

print("Segmentation Done!")
print("-------answer-------")
for line in answer:
    print ("|".join(line))
##print(answer)

