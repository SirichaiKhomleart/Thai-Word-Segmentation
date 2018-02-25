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



Precaution
------------------------------
1
This program compatible with only python 3, computer that run this program have to have pythin 3 installed.
After execute this program, program may ask the directory of input text file and Thai dictionary file.

2
In order to make this program run properly, user need to specify the operating system of his/her computer.
During the execution, program may ask you to input ypur operating system name.
If you use Windows, please input "W".  But if you use macOS or other Linux systems, please input "M".
In case you input is not follow the instruction, the program will assume that you use Linux system.

3
This program is not support word/phase from other languages but Thai language.
If other languages appear in your text input file, the program may ignore them and not print them as output answer.

4
This program not support numerical contents, and it will output as seperate digits for every number.
For example, 123456 may be segmentation as 1|2|3|4|5|6.

5
Input text file have to remove all of special character that not consider as a language, as well as blank line.
Please remove the blank lines and special characters from input file before you save it.
Program may face error if the input text file content those characters (and blank lines).
