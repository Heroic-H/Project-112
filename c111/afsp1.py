import os
from_dir="C:/Users/batul/Downloads"
listOfFiles=os.listdir(from_dir)
#print(listOfFiles)
for fileName in listOfFiles:
    name,extension=os.path.splitext(fileName)
    #print(name)
    #print(extension)
    print(listOfFiles.len)