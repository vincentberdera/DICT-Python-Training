try:
    # fw = open("record.txt","w") # writing content or overwriting the content
   fw = open("record.txt","a") # Appending the content

   content = str(input("Enter a word: "))
   fw.write(content+"\n")
   fw.close()

   fr = open("record.txt","r")
   print("===Content====")
   for line in fr:
       line = line.strip("\n")
       line = line.strip(" ")
       print(line)

   fr.close()

except FileNotFoundError:
    print("File not found")
