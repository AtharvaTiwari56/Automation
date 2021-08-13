import os 
import shutil

pathboy = input('Give me your folder path:')
listoffiles = os.listdir(pathboy)

for file in listoffiles:
    name, extension = os.path.splitext(file) 
    extension = extension[1:]

    if extension==" ":
        continue

    if os.path.exists(pathboy+ '/' + extension):
        shutil.move(pathboy + '/' + file, pathboy+'/'+ extension+'/'+file)
    else:
        os.mkdir(pathboy+'/'+extension)
        shutil.move(pathboy + '/' + file, pathboy+'/'+ extension+'/'+file)

