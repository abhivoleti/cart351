# rainbowFile=open("rainbow.txt", "r")
# #read first 10 chars
# out = rainbowFile.read
# #print(out)
# #read all
# outAll= rainbowFile
# print(outAll)

# allLines = rainbowFile.readlines()
# #print(allLines)
# print(allLines[1])

# sampleFile = open("files/sample_text_rev.txt","w")
# for i in range(3): 
#     a_name = input("Enter the name of the animal: ") 
#     sampleFile.write(a_name) 
#     sampleFile.write("\n") 
# sampleFile.close() 
# print("Data is written into the file.") 
# colorList = [] 
# for i in range(3): 
#     a_name = input("Enter the name of a color: ") 
#     colorList.append(a_name + '\n') 
# sampleFile.writelines(colorList) 
# sampleFile.close() 
# print("Data is written into the file.") 
sampleFile_a = open("files/sample_text.txt","a")
nameList = [] 
for i in range(3): 
    a_name = input("Enter the name of someone in your class: ") 
    nameList.append(a_name + '\n') 
sampleFile_a.writelines(nameList) 
sampleFile_a.close() 
print("Data is written into the file.")