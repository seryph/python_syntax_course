
# File Handling

# a file named "geek", will be opened with the reading mode.
file = open('file.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)




file = open('file.txt','w')
file.write("This is the write command")
file.close()