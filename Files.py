my_files=["file1.txt","file2.txt","file3.txt"]
with open('file4.txt','w') as outfile:
    for i in my_files:
        with open(i) as infile:
            outfile.write(infile.read())
            outfile.write("\n")
            
