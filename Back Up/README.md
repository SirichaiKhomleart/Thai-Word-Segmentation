# Thai Word Segmentation



This is the university project that aims to the study of information retrieval.
------------------------------
Sirindhorn International Institute of Technology
Thammasat University

CSS432 - Information Retrieval          Section 1
Semester 2          Year 2017

Members
1     5822781910    Mr.Sirichai    Khomleart
2     5822782421    Mr.Pasin       Jiratthiticheep
3     5822782546    Mr.Nuttapol  Saiboonruen



Information
------------------------------
This Thai-Word-Segmentation program is the segmentation program based on Thai dictionary.
This program will clustering every word and generate possible answers by comparing the word with dictionary.
In case there are many possible outputs, this program will use approach of minimun word count and n-gram probability (start from trigram, then bigram, and monogram) in order to find the correct answer.

In conclusion, this program has perform three step.
1 Word Clustering
2 Candidate Formation
3 Probability Calculation



Precaution
------------------------------
1
This program compatible with only python 3, computer that run this program have to have pythin 3 installed.
After execute this program, program may ask the directory of input text file and Thai dictionary file.

2
This program is not support word/phase from other languages but Thai language.
If other languages appear in your text input file, the program may ignore them and not print them as output answer.

3
This program not support numerical contents, and it will output as seperate digits for every number.
For example, 123456 may be segmentation as 1|2|3|4|5|6.

4
Input text file have to remove all of special character that not consider as a language.
Please remove special characters from input file before you save it.
Program may face error if the input text file content those characters.
