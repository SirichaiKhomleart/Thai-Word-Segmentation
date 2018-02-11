import json
import time

def searching(word):
    if word in dictionary:
##        print(word, "This word is in a dictionary.")
        return True
    else:
        return False

def create_candidate(sentenceList,pointer,lenghtList,line,token):
    global counter
    if pointer > lenghtList:       #base case
        return sentenceList
    else:                               #recursive loop
        current_word = sentenceList[pointer]
##        print(current_word)
        if searching(current_word):
            token = 0
            sepList1 = list(sentenceList)
            sepList1 = create_candidate(sepList1,pointer+1,lenghtList,line,token)
            if(sepList1 != None):
                counter+=1
##                print("counter",counter,sepList1)
                candidate[line].append(sepList1)
            if (any([l.startswith(current_word) for l in dictionary])) and (not pointer+1 > lenghtList):
                if (token == 0):
                    token = 1
                elif (token == 1):
                    token = 2
                sepList2 = list(sentenceList)
                sepList2[pointer] = sepList2[pointer]+sepList2[pointer+1]
                del sepList2[pointer+1]
                sepList2 = create_candidate(sepList2,pointer,lenghtList-1,line,token)
##                if (sepList2 == [] and token == 1):
##                    token = 0
##                    sepList2 = list(sentenceList)
##                    sepList2 = create_candidate(sepList2,pointer+1,lenghtList,line,token)
##                elif (sepList2 == [] and token == 2):
##                    return []
            return
        elif (not searching(current_word)) and (not pointer+1 > lenghtList):
            if (any([l.startswith(current_word) for l in dictionary])):
                if (token == 0):
                    token = 1
                elif (token == 1):
                    token = 2
                sepList3 = list(sentenceList)
                sepList3[pointer] = sepList3[pointer]+sepList3[pointer+1]
                del sepList3[pointer+1]
                sepList3 = create_candidate(sepList3,pointer,lenghtList-1,line,token)
                if (sepList3 == [] and token == 1):
                    token = 0
                    sepList3 = list(sentenceList)
                    sepList3 = create_candidate(sepList3,pointer+1,lenghtList,line,token)
                elif (sepList3 == [] and token == 2):
                    return []
            else:
                return []
        
def merge_back(pointer,namelist):
    namelist[pointer] = namelist[pointer]+namelist[pointer+1]
    del namelist[pointer+1]
    return namelist

def merge_front(pointer,namelist):
    namelist[pointer] = namelist[pointer-1]+namelist[pointer]
    del namelist[pointer-1]
    return namelist

## Main Program
stime = time.time()
with open("thaiwordlist.txt", encoding="utf8") as f:
    dictionary = f.readlines()
dictionary = [x.strip() for x in dictionary] 
dictionary2 = ["ทด","แทน","ท","ด","ส","อ","บ","ดอกเบี้ย","ทดสอบ","แบ่งคำ"]
print("Dictionary list is loaded")

###Tester part
counter = 0
string = "คบคนพาลพาลพาไปหาผิดคบบัณฑิตบัณฑิตพาไปหาผลเด็กตากลมนั่งตากลมตากแดด"
string1 = "พศินเมื่อไหร่"
string2 = [list(string)]
for a in string2:
    if ' ' in a:
        a.remove(' ')

# Cluster creation
front_vowel = ["เ","แ","โ","ใ","ไ"]
back_vowel = ["ะ","า","ิ","ี","ึ","ื","ุ","ู","ั","ำ","ๅ","์","ํ","่","้","๊","๋","็"]
for i in range(len(string2)):
    j = 0
    while string2[i][j] != None:
        checker = string2[i][j]
        if checker in front_vowel:
            string2[i] = merge_back(j,string2[i])
        elif checker in back_vowel:
            string2[i] = merge_front(j,string2[i])
            j = j-1
            while (checker == "ั" or checker == "ื") and string2[i][j][-1] in back_vowel:
                string2[i] = merge_back(j,string2[i])
            if checker == "็":
                string2[i] = merge_back(j,string2[i])
            elif (checker == "ื" or checker == "ี") and ("เ" in string2[i][j]) and (string2[i][j][-1] != "ย" and string2[i][j][-1] != "อ"):
                y = j+1
                while (string2[i][y] != "ย"):
                    string2[i] = merge_back(j,string2[i])
                    y = y+1
                string2[i] = merge_back(j,string2[i])
        j = j+1
        if j == len(string2[i]):
            break
print("Cluster: ",string2)

#Candidate Creation
candidate = []
line = 0
for sentence in string2:
    candidate.append([])
    create_candidate(sentence,0,len(sentence)-1,line,0)
    line += 1

#Printing output
for i in range(len(candidate)):
    for j in range(len(candidate[i])):
        print("Line "+str(i+1),"Candidate "+str(j+1),candidate[i][j])
print("Execution time : ",(time.time()-stime)," seconds")
