import subprocess
from tkinter import filedialog

##print("Please input 'JTCC-0.1.jar' file")
##jtcc_file_path = filedialog.askopenfilename() #get file path for JTCC-0.1.jar
##print("JTCC path is "+jtcc_file_path)
##print("Please input plain text file")
##plaintext_file_path = filedialog.askopenfilename() #get file path for plaintext.txt
##print("File path is "+plaintext_file_path)

subprocess.call(["echo","python"])
result = subprocess.check_output(['echo','service','mpd','restart'])
print(result)
