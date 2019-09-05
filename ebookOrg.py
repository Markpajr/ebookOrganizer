# Done: Open the book directory
# Done: Get a unique list of file names
# Done: Move each unique filename to a folder with all ext.

import glob, os, shutil

# Sets working directory to where my ebook files are
os.chdir(r'C:\Users\Owner\Downloads\Python Materials\Python - humble bundle')

# Uses glob to get a list of every file in the directory
allfiles = glob.glob('./*.*')
# Removes .// from the glob strings in the list
noprefix =[x[2:] for x in allfiles]
noExt = []
# Removes the extensions frome every file
for i in noprefix:
    name = os.path.splitext(i)[0]
    noExt.append(name)
# Removes all duplicates from the list by converting to a dict    
uniFiles = list(dict.fromkeys(noExt))

# Changes working directory to where I want the ebooks located
os.chdir(r'C:\Users\Owner\Downloads\Python Materials\Python - humble bundle\test')

# Creates folders for each ebook based on it's unique name
for file in uniFiles:
    try:
        os.mkdir(file)
        print('Folder ', file, 'Created')
    except FileExistsError:
        print(file, ' Folder Exists')
# Uses glob to make a list containing every file type for each unique ebook
# Copies every extension for each ebook to their respective folders
for file in uniFiles:
    filepath = glob.glob(f'../{file}.*')
    for xpath in filepath:
        filename = xpath[2:]
        destination = 'C:\\Users\\Owner\\Downloads\\Python Materials\\Python - humble bundle\\test\\{0}'.format(file)
        shutil.copy(xpath,destination)