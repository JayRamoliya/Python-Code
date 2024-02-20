# append the end of the file
# overwrite any existing content


# f=open('File_Handling.txt','a')
# f.write("this is end\n")

# open and read the file after the appending
# l=open('File_Handling.txt','r')
# print(l.read())
# f.close()

# ==================

# is method will overwrite the entire file
f=open('demo.txt','w')
f.write("nice work in my project")
f.close()

# open and read the file after the appding
f=open('demo.txt','r')
print(f.read())