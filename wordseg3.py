import json
import time

def searching(word):
    if word in dictionary:
        print(word, "This word is in a dictionary.")
        return True
    else:
        return False

def create_candidate(sentenceList,pointer,lenghtList,line,token):
    global counter
    if pointer > lenghtList:       #base case
        return sentenceList
    else:                               #recursive loop
        current_word = sentenceList[pointer]
        print(current_word)
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
            elif(current_word == " "):
                token = 0
                sepList1 = list(sentenceList)
                sepList1 = create_candidate(sepList1,pointer+1,lenghtList,line,token)
                if(sepList1 != None):
                    counter+=1
                    candidate[line].append(sepList1)
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
print("Dictionary list is loaded")

###Tester part
counter = 0
testString = "คบคนพาลพาลพาไปหาผิดคบบัณฑิตบัณฑิตพาไปหาผลเด็กตากลมนั่งตากลมตากแดด"
testString = "พศินเมื่อไหร่"

# Read file for input
with open("thaiword.txt",encoding = "utf8") as f:
    mylist = f.read().splitlines()
inputfile = [list(x) for x in mylist]
inputfile[0].remove('\ufeff')

# Cluster creation
front_vowel = ["เ","แ","โ","ใ","ไ"]
back_vowel = ["ะ","า","ิ","ี","ึ","ื","ุ","ู","ั","ำ","ๅ","์","ํ","่","้","๊","๋","็"]
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
            if checker == "็":
                inputfile[i] = merge_back(j,inputfile[i])
            elif (checker == "ื" or checker == "ี") and ("เ" in inputfile[i][j]) and (inputfile[i][j][-1] != "ย" and inputfile[i][j][-1] != "อ"):
                y = j
                while (inputfile[i][j][-1] != "ย" and inputfile[i][j][-1] != "อ"):
                    inputfile[i] = merge_back(j,inputfile[i])
                    y = y+1

        j = j+1
        if j == len(inputfile[i]):
            break
print("Cluster: ",inputfile)

#Candidate Creation
candidate = []
line = 0
for sentence in inputfile:
    candidate.append([])
    create_candidate(sentence,0,len(sentence)-1,line,0)
    line += 1

#Printing output
for i in range(len(candidate)):
    for j in range(len(candidate[i])):
        print("Line "+str(i+1),"Candidate "+str(j+1),candidate[i][j])
print("Execution time : ",(time.time()-stime)," seconds")
