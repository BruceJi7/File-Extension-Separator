import os, shutil


# Type Working Directory here
os.chdir("C:\\Users\\User\\Pictures\\Mum's Bag, Backup\\20190415 Photos of Bags")

# Load contents of directory
dirContents = os.listdir('.\\')

# Define function to list all extension types.
def extensionsPresent(sourceList):
    print('Listing all present file types...')
    extensionsList = []
    for item in sourceList:
        if item[-4:] not in extensionsList:
            extensionsList.append(item[-4:])
    print('File types present: {}'.format(extensionsList))    
    return extensionsList    
        

# Main function - creates folder for an extension and moves files into it.
def pickyList(sourceList, extension):
    oneFolderCreation(extension)
    destinationPath = ('.\\{} Files\\'.format(extension[1:]))
    movedFileCount = 0
    for item in sourceList:
        
        if item[-4:] == extension:
            shutil.move(item, destinationPath)
            movedFileCount += 1
    print('Moved {} files to {}'.format(movedFileCount, destinationPath))
    movedFileCount = 0
# Define a function to create a new folder for each extension type.
def folderCreation(extensionsList):
    for item in extensionsList:
        foldername = ('{} Files'.format(item[1:]))
        os.makedirs(foldername)
        print('{} folder created'.format(foldername))
        
def oneFolderCreation(extension):
        foldername = ('{} Files'.format(extension[1:]))
        os.makedirs(foldername)
        print('{} folder created'.format(foldername))
    

    
extensionsInFolder = extensionsPresent(dirContents) # Make as a variable, else it will run this function each time

#folderCreation(extensionsInFolder)

for item in extensionsInFolder:
    pickyList(dirContents, item)
    