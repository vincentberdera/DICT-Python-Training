try:
    acc = list()
    fr = open("account.txt", "r")
    for line in fr:
        line = line.strip("\n")
        line = line.strip(" ")
        acc = line.split(",")

        pin = int(acc[1])
        balance = int(acc[2])
        print(line)


    fr.close()

    balance = balance + 5000

    print(balance)

    fw = open("account.txt", "w")
    content = acc[0]+","+acc[1]+","+str(balance)
    fw.write(content)
    fw.close()

except FileNotFoundError:
    print("File not found")