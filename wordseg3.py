import json

def searching(word):
    if word in dictionary:
##        print(word, "This word is in a dictionary.")
        return True
    else:
        return False

def create_candidate(sentenceList,pointer,lenghtList,line):
    global counter
    if pointer > lenghtList:       #base case
        return sentenceList
    else:                               #recursive loop
        current_word = sentenceList[pointer]
##        print(current_word)
        if searching(current_word):
            sepList1 = list(sentenceList)
            sepList1 = create_candidate(sepList1,pointer+1,lenghtList,line)
            if(sepList1 != None):
                counter+=1
##                print("counter",counter,sepList1)
                candidate[line].append(sepList1)
            if (any([l.startswith(current_word) for l in dictionary])) and (not pointer+1 > lenghtList):
                sepList2 = list(sentenceList)
                sepList2[pointer] = sepList2[pointer]+sepList2[pointer+1]
                del sepList2[pointer+1]
                sepList2 = create_candidate(sepList2,pointer,lenghtList-1,line)
            return
        elif (not searching(current_word)) and (not pointer+1 > lenghtList):
            if (any([l.startswith(current_word) for l in dictionary])):
                sepList3 = list(sentenceList)
                sepList3[pointer] = sepList3[pointer]+sepList3[pointer+1]
                del sepList3[pointer+1]
                sepList3 = create_candidate(sepList3,pointer,lenghtList-1,line)
            else:
                return              
        
def merge_back(pointer,namelist):
    namelist[pointer] = namelist[pointer]+namelist[pointer+1]
    del namelist[pointer+1]
    return namelist

def merge_front(pointer,namelist):
    namelist[pointer] = namelist[pointer-1]+namelist[pointer]
    del namelist[pointer-1]
    return namelist

## Main Program
with open("thaiwordlist.txt", encoding="utf8") as f:
    dictionary = f.readlines()
dictionary = [x.strip() for x in dictionary] 
dictionary2 = ["ทด","แทน","ท","ด","ส","อ","บ","ดอกเบี้ย","ทดสอบ","แบ่งคำ"]
print("Dictionary list is loaded")

###Tester part
counter = 0
string = "คบคนพาลพาลพาไปหาผิดคบบัณฑิตบัณฑิตพาไปหาผล"
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
            elif (checker == "ื" or checker == "ี") and ("เ" in string2[i][j]):
                y = j
                while string2[i][y] != "ย":
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
    create_candidate(sentence,0,len(sentence)-1,line)
    line += 1

#Printing output
for i in range(len(candidate)):
    for j in range(len(candidate[i])):
        print("Line "+str(i+1),"Candidate "+str(j+1),candidate[i][j])
