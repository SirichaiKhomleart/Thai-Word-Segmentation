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

print("-----------------")
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
