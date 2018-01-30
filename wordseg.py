import json
from py4j.java_gateway import JavaGateway
##import jpy as jp

def searching(word):
    if word in dictionary:
        print(word)
        print("This word is in a dictionary.")
    return;

def create_candidate(sentence_list):
    counter = 0
    for st in sentence_list:
        if counter != len(sentence_list)-1:
            searching(st+sentence_list[counter+1])
        else:
            searching(st)
        counter+=1
    return;

dictionary = json.load(open('thaiwordlist.json', encoding="utf8"))
dictionary2 = ["ทด","แทน","สอบ","ท"]
print("Dictionary list is loaded")

f_input = [["ท","ด","ส","อ","บ","กา","ร","แบ่","ง","คำ","ฮ"],
           ["เสา","ร์","นี้","ไป","ไห","น","ไก่","กา","ตา","ก","ล","ม","จับ","ตา","ดู","ด","อ","ก","เบี้ย"]]
candidate = []
sentence = 0
for sentence in f_input:
    candidate.append(create_candidate(sentence))

