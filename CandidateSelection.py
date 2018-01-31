a0=['ปลา','มี','ตา','กลม','แต่','เสื้อ','ตาก','ลม']
a1=['ปลา','มี','ตา','กลม','แต่','เสื้อ','ตา','กลม']
a2=['ปลา','มี','ตาก','ลม','แต่','เสื้อ','ตาก','ลม']
a3=['ปลา','มี','ตาก','ลม','แต่','เสื้อ','ตา','กลม']
a4=['ปลา','มี','ตา','กลม','แต่','เสื้อ','ตา','ก','ลม']
b0=['วัน','นี้','ฝน','ตก','รถ','ติด']
b1=['วัน','นี้','ฝน','ต','ก','รถ','ติด']
b2=['วัน','นี้','ฝน','ตก','รถ','ติ','ด']
b3=['วัน','นี้','ฝน','ต','กร','ถ','ติด']
b4=['วัน','นี้','ฝน','ต','กร','ถ','ติ','ด']

candidate_line0=[a0,a1,a2,a3,a4]
candidate_line1=[b0,b1,b2,b3,b4]
candidate_array=[candidate_line0,candidate_line1]
# candidate_array=[[['ทดสอบ', 'การ', 'แบ่ง', 'คำ', 'ฮ'], ['ทดสอบ', 'การ', 'แบ่', 'ง', 'คำ', 'ฮ'], ['ทดสอบ', 'กา', 'ร', 'แบ่ง', 'คำ', 'ฮ'], ['ทดสอบ', 'กา', 'ร', 'แบ่', 'ง', 'คำ', 'ฮ'], ['ทดสอ', 'บ', 'การ', 'แบ่ง', 'คำ', 'ฮ'], ['ทดสอ', 'บ', 'การ', 'แบ่', 'ง', 'คำ', 'ฮ'], ['ทดสอ', 'บ', 'กา', 'ร', 'แบ่ง', 'คำ', 'ฮ'], ['ทดสอ', 'บ', 'กา', 'ร', 'แบ่', 'ง', 'คำ', 'ฮ']]]

import math

##find the probability using bigram

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



print('test')
print(bigram(a0))
print(bigram(a1))
print(bigram(a2))
print(bigram(a3))
print(bigram(a4))
print()

print(index3)

for line in candidate_array:
    for group in line:
        print(bigram(group))
    print("-----------------")

print("-----------------")
print("-----------------")


for line in candidate_array:
    for group in line:
        print("len: "+str(len(group))+" Prob:"+str(trigram(group))+" Word: ")
        print(group)
    print("-----------------")


print("-----------------")
print("-----------------")

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
    print(selectCandidate)
    if len(selectCandidate)==1:
        answer.append(selectCandidate[0])
    else:
        maxprob=0
        maxprobIndex=0
        for i in range (len(selectCandidate)):
            currprob = trigram(selectCandidate[i])
            if currprob>maxprob:
                maxprob=currprob
                maxprobIndex=i
            print("currprob " + str(currprob))
        answer.append(selectCandidate[i])

print("--------------")
print(answer)



