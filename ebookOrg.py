# Done: Open the book directory
# Done: Get a unique list of file names
# Done: Move each unique filename to a folder with all ext.

import glob, os, shutil

os.chdir(r'C:\Users\Owner\Downloads\Python Materials\Python - humble bundle')

allfiles = glob.glob('./*.*')
noprefix =[x[2:] for x in allfiles]
noExt = []
for i in noprefix:
    name = os.path.splitext(i)[0]
    noExt.append(name)
uniFiles = list(dict.fromkeys(noExt))

os.chdir(r'C:\Users\Owner\Downloads\Python Materials\Python - humble bundle\test')

for file in uniFiles:
    try:
        os.mkdir(file)
        print('Folder ', file, 'Created')
    except FileExistsError:
        print(file, ' Folder Exists')

for file in uniFiles:
    filepath = glob.glob(f'../{file}.*')
    for xpath in filepath:
        filename = xpath[2:]
        destination = 'C:\\Users\\Owner\\Downloads\\Python Materials\\Python - humble bundle\\test\\{0}'.format(file)
        shutil.copy(xpath,destination)