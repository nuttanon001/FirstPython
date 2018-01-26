#Copying Files and Folders
import shutil, os
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')
#Copy and new file name
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
#Copytree
shutil.copytree('C:\\bacon','C:\\bacon_backup')
#Moving and Renaming Files and Folders
shutil.move('C:\\bacon.txt', 'C:\\eggs')
#Method()
#Calling os.unlink(path) will delete the file at path.
#---------------------
#Calling os.rmdir(path) will delete the folder at path. This folder must be
#empty of any files or folders.
#---------------------
#Calling shutil.rmtree(path) will remove the folder at path, and all files
#and folders it contains will also be deleted.
print('-------------------------')
#Walking a Directory Tree
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

print('------------------------')
#Reading ZIP Files
import zipfile
os.chdir('C:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
print('List file in zip',exampleZip.namelist())

spamInfo = exampleZip.getinfo('spam.txt')
#FileSize
print('File size',spamInfo.file_size)
#CompressSize
print('Compress size',spamInfo.compress_size)
#
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()
print('------------------------')
#Extracting from ZIP Files
os.chdir('C:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
#Extracting all file
exampleZip.extractall()
exampleZip.close()
print('------------------------')
#Extracting single file
exampleZip.extract('spam.txt')
#Extracting single file to dir
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
exampleZip.close()
print('------------------------')

#Creating and Adding to ZIP Files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()