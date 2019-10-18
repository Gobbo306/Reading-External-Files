#------------------------------------------------
#Dylan Friesen
#Reading external files
#Thursday October 17, 2019
#------------------------------------------------

#---------------Functions------------------------

def read_file():     #imports the file for reading
    file = open('Randall.txt', 'r')
    all_lines = file.read() #reads all the lines in the document
    print(all_lines) #prints all the lines that it read
    file.close() #closes the document after it is done
    
def list_file(): #it is importing the file for reading
    file = open('Randall.txt', 'r')
    Randall_list = file.readlines() #defining the lines in the document as Randall_list
    print(Randall_list) #printing what was read, as python reads it( a list), instead of text document    
    
def read_linebyline(): #imports file for reading
    file = open('Randall.txt', 'r')
    line = file.readline() #sets line as the first line
    print(line)
    line2 = file.readline() #sets line 2 as the second line
    print(line2)
    line3 = file.readline() #sets line 3 as the third line
    print(line3)
    
def main(): #main code for all the functions
    read_file()
    list_file()
    read_linebyline()
    
#---------------Main Code--------------------
    
main()
