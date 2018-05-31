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



Data Test Set
------------------------------

-------INPUT-------

ในงานนี้มีคนดังกล่าวว่าต่อไปจะไม่โกงอีกแล้ว

ในงานนี้มีคนดังกล่าวปรากฏตัวอยู่ด้วย

ป้าบ้าบิ่นให้การกับตำรวจเรื่องหวย 30 ล้าน

ครูสอนให้การทำงานเป็นกลุ่มเป็นไปอย่างราบรื่น

ใครเป็นคนให้การบ้าน

ที่นี่มีร้านข้าวซอยลำดวนอยู่ท้ายซอย

ร้านข้าวซอยนิมมานอยู่ในซอย 7

กาลิเลโอ กาลิเลอีเป็นนักคณิตศาสตร์ชาวอิตาลี

ขุนนางเดินตามหามเหสีตั้งแต่เช้า

ฝนแล้งปีนี้ทำให้การประปามีรายได้เพิ่มขึ้น

นักลงทุนดูดอกเบี้ยที่จะได้จากธนาคารแล้วคิดว่าลงทุนในตลาดหลักทรัพย์คุ้มค่ากว่า

ยามเย็นเดินดูดอกไม้ในสวนทำให้เพลิดเพลินจิตใจ

ยามยากก็ต้องกินข้าวไปดูดอกไก่ไป

ทุกสิ้นปีจะมีการประดับดอกไม้ไฟฟ้าตามมุมถนน

งานดอกไม้ไฟมีให้ดูทั้งปี

รู้หรือไม่ว่าแซ่ที่มีคนใช้มากที่สุดในประเทศไทยคือแซ่อะไร

ตระกูลใหญ่มักจะมีคนใช้มาก

ชาวนาขายที่นาไปสร้างคอนโด

นายอำเภอไปเจอพ่อที่นาหลังบ้าน


-------OUTPUT-------

ใน|งาน|นี้|มี|คนดัง|กล่าวว่า|ต่อไป|จะ|ไม่|โกง|อีกแล้ว

ใน|งาน|นี้|มี|คน|ดังกล่าว|ปรากฏตัว|อยู่|ด้วย

ป้า|บ้าบิ่น|ให้การ|กับ|ตำรวจ|เรื่อง|หวย| |3|0| |ล้าน

ครู|สอน|ให้|การทำงาน|เป็น|กลุ่ม|เป็นไป|อย่างราบรื่น

ใคร|เป็น|คน|ให้|การบ้าน

ที่นี่|มี|ร้าน|ข้าว|ซอย|ลำ|ด|วน|อยู่|ท้าย|ซอย

ร้าน|ข้าว|ซอย|นิ|ม|มาน|อยู่|ใน|ซอย| |7

กาลิเลโอ| |กา|ลิ|เล|อี|เป็น|นัก|คณิตศาสตร์|ชาว|อิตาลี

ขุนนาง|เดินตาม|หา|มเหสี|ตั้ง|แต่เช้า

ฝนแล้ง|ปี|นี้|ทำให้|การประปา|มี|รายได้|เพิ่มขึ้น

นักลงทุน|ดู|ดอกเบี้ย|ที่จะ|ได้|จาก|ธนาคาร|แล้ว|คิด|ว่า|ลงทุน|ใน|ตลาดหลักทรัพย์|คุ้มค่า|กว่า

ยาม|เย็น|เดิน|ดู|ดอกไม้|ใน|สวน|ทำให้|เพลิดเพลิน|จิตใจ

ยามยาก|ก็|ต้อง|กินข้าว|ไป|ดูด|อกไก่|ไป

ทุก|สิ้นปี|จะ|มี|การ|ประดับ|ดอกไม้|ไฟฟ้า|ตาม|มุมถนน

งาน|ดอกไม้ไฟ|มี|ให้|ดู|ทั้งปี

รู้|หรือ|ไม่ว่า|แซ่|ที่|มี|คนใช้|มาก|ที่สุด|ใน|ประเทศไทย|คือ|แซ่|อะไร

ตระกูล|ใหญ่|มักจะ|มี|คนใช้|มาก

ชาวนา|ขาย|ที่นา|ไป|สร้าง|คอนโด

นายอำเภอ|ไป|เจอ|พ่อ|ที่นา|หลังบ้าน


