import os
import shutil


def MoveFiles(sourceFolder, destinationFolder):
        if not os.path.exists(sourceFolder):
            print("The source directory " + sourceFolder + " does not exists")
        else:
            print("Source : " + sourceFolder)
            print("Destination :" + destinationFolder)

            allFiles = os.listdir(sourceFolder)

            for file in allFiles:
                filePath = os.path.join(sourceFolder, file)

                #Igonore if empty
                if os.path.isdir(filePath):
                    print("File already present")
                    continue
                print("File : " + filePath)

                if os.path.exists(destinationFolder):

                    #Moving file   
                    try:
                        if (file.startswith('HU')):
                            print("huhuhuhuuhu")
                            hu_destination = "/home/subin/Documents/hu"
                            shutil.move(filePath, hu_destination)
                        else:
                            shutil.move(filePath, destinationFolder)
                        
                    except: 
                        print("File Already present")

                if not os.path.exists(destinationFolder):
                    os.makedirs(destinationFolder)


                
                    
                    
                    
def main():
    sourceFolder = "/home/subin/Documents/source"
    destinationFolder = "/home/subin/Documents/destination"
    MoveFiles(sourceFolder, destinationFolder)


main()


