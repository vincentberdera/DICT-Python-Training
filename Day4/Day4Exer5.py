# try:
#     fr = open("data.txt", "r")
#
#     content = fr.readline()
#     print("===========Content============")
#     print(content)
#     fr.close()
# except FileNotFoundError:
#     print("File not found")

# li = []
# try:
#     fr = open("data.txt", "r")
#     print("======Content======")
#     for line in fr:
#         line = line.strip("\n")
#         line = line.strip(" ")
#
#         li = line.strip(",")
#         print(f"{li[0]}")
#
# except FileNotFoundError:
#     print("File not found")


# li = []
# try:
#     fr = open("data.txt", "r")
#     print("======Content======")
#     print("NAME\tEMAIL\t\tCONTACT")
#     for line in fr:
#         line = line.strip("\n")
#         line = line.strip(" ")
#
#         li = line.split(",")
#         print(f"{li[0]}\t{li[1]}\t{li[2]}")
#
# except FileNotFoundError:
#     print("File not found")

mylist = list()
yourlist = list()
try:
    fr = open("data.txt","r")
    print("======Content=======")

    for line in fr:
        line = line.strip("\n")
        mylist= line.split("#")

        yourlist.append(mylist)
        print(f"{mylist[0]}\t{mylist[1]}\t{mylist[2]}")

    print(f"{yourlist[0][1]}")

except FileNotFoundError:
    print("File not found")

