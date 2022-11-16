import time

#open file and check how to convert it
file = open('text.txt', 'r')
data = file.read()
line = 0
wordcount = 0
keep = input('Do you want to keep to keep the original format (y)? Or have the program make a new line after each space (n)? (y/n)')

#format the file or not
if keep == 'y':
    print('original data kept')
if keep == 'n':
    with open('text.txt', 'r') as file:
        data = data.replace('\n', '\b')
        data = data.replace('.', '.\n')

    with open('text.txt', 'w') as file:
        file.write(' ')
        file.write(data)
        file.close()

keyword = input("What word are you searching for?")

#mail loop
while True:
    try:
        with open('text.txt',"r") as file:
            content = file.readlines()
            #look through each line and seach for the keyword
            if content[line].__contains__(keyword):
                wordcount, line += 1
                print(f"The word you are looking for is on line: {line}")
                print (f"This is the line: {content[line]}")
                time.sleep(1)
            else:    
                line += 1
    #end options
    except:
        if wordcount == 0:
            print("The word you were looking for is not in the file")
            file.close()
            exit()
        else:
            print(f"There were a total of the {wordcount} of the words you were looking for in the document")
            file.close()
            exit()