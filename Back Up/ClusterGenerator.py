print("Compatible with python 3 only.")
##print("This is Thai Segmentation quiz, but it look very like the final thesis for the forth-year students.")


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
print("JTCC path is "+jtcc_file_path)
print("Please input plain text file")
plaintext_file_path = filedialog.askopenfilename() #get file path for plaintext.txt
print("File path is "+plaintext_file_path)

plaintext_lines =  len(open(plaintext_file_path,'rb').read().splitlines())
print("Number of lines in file is "+str(plaintext_lines))

print("Command is ")
print('java', '-jar',jtcc_file_path,'file',plaintext_file_path)


def get_output(cmd, until):
    linenumber=1
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    ret = []
    while True:
        ##print("current line:"+str(linenumber)+", until: "+str(until))
        line = p.stdout.readline()
        line = line.replace(b'|',b'')
##        line = line.replace(b'\xe0\xb8?',b'\xe0\xb8\x81')
        print(line)
##        line = line.decode('utf8')
##        ret.append(line)
        file = open("textfile.txt","wb")
        file.write(line)
        if str(linenumber)==str(until):
            break
        linenumber = linenumber+1
    p.kill()
    return ret

##print (''.join(get_output(['java','-jar',jtcc_file_path,'file',plaintext_file_path], until=plaintext_lines)))
clusterarray = [plaintext_lines]
clusterarray = get_output(['java','-jar',jtcc_file_path,'file',plaintext_file_path], until=plaintext_lines)


##for i in range (len(clusterarray)):
##    temp = clusterarray[i].split('|')
##    clusterarray[i]=temp
    ##print ("current spliting at line: "+str(i))

print("Generate Cluster Done")
####This is for checking cluster array
##for i in range (len(clusterarray)):
##    for j in range (len(clusterarray[i])):
##        print("i: "+str(i)+" j: "+str(j)+" text: "+clusterarray[i][j])
