import os
print(os.path.join('usr','bin','spam'))
# File Name
print('------------------------------------')
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for fileName in myFiles:
    print(os.path.join('C:\\Users\\nuttanon', fileName))

print('------------------------------------')
# The Current Working Directory
print(os.getcwd())
# Change dir
os.chdir('C:\\Windows\\System32')
print(os.getcwd())
#Creating New Folders with os.makedirs()
# os.makedirs('C:\\test\\sub-test')

# The base name follows the last slash
# in a path and is the same as the filename. The dir
# name is everything before the last slash.
path = 'C:\\Windows\\System32\\calc.exe'
print('Is baseName',os.path.basename(path))
print('Is dirName',os.path.dirname(path))
#If you need a path’s dir name and base name together
print('Together is Tulple',os.path.split(path))
#folder-separating slash
print('Split to List',path.split(os.path.sep))
#Folder Contents
print('ListDir',os.listdir('C:\\Windows\\System32'))
#Calling os.path.exists(path) will return True if the file or folder referred
    #to in the argument exists and will return False if it does not exist.
#Calling os.path.isfile(path) will return True if the path argument exists
    #and is a file and will return False otherwise.
#Calling os.path.isdir(path) will return True if the path argument exists
    #and is a folder and will return False otherwise.
print('------------------------------------')
#Open File
helloFile = open('C:\\Users\\Thorkait\\hello.txt')
#For ReadOnly but default is read only
helloFile2 = open('C:\\Users\\Thorkait\\hello.txt', 'r')
#Reading the Contents of Files
#Read content of file
helloContent = helloFile.read();
print('Read all content',helloContent)
#Read content line by line
helloContent = helloFile.readline();
print('Read line by line',helloContent)
print('------------------------------------')
#Writing to Files
baconFile = open('bacon.txt','w')
baconFile.write('Hello world!\n')
baconFile.close()
#Line2
baconFile = open('bacon.txt','w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
#Read text
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
print('-----------------------------')
# Saving Variables with the shelve Module
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
#Get all data
shelfFile = shelve.open('mydata')
print('Type is',type(shelfFile))
print('Get data',shelfFile['cats'])
shelfFile.close()
#Get by key
shelfFile = shelve.open('mydata')
print('Key is',list(shelfFile.keys()))
print('List is',list(shelfFile.values()))
shelfFile.close()