import os
import shutil
from_dir="C:/Users/batul/Downloads"
to_dir="C:/Users/batul/Downloads/Homework_Thing"
listOfFiles=os.listdir(from_dir)
#print(listOfFiles)
for fileName in listOfFiles:
    name,extension=os.path.splitext(fileName)
    #print(name)
    #print(extension)
    if extension=="":
        continue
    if extension in[".txt", ".doc", ".docx", ".pdf"]:
        path1=from_dir+"/"+fileName
        path2=to_dir+"/"+"Document files"
        path3=to_dir+"/"+"Document files"+"/"+fileName
        if os.path.exists(path2):
            print("moving "+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving "+fileName+"...")
            shutil.move(path1,path3)