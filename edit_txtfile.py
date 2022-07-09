import array as arr
import os

file1 = open("/home/adham/Desktop/Final_Night/croppedN1/test/", "r+")

list = arr.array('i', [])
list = file1.readlines()
length = len(list)
print(length)
listlist = arr.array('i', [])
sub = arr.array('i', [])
adham = arr.array('i', [])
final = []
string = ""

file1.seek(0)

print(list)
i = 0
while length > 0:
    listlist = list[i].split()
    # print(listlist)
    # print(listlist[0])
    if (listlist[0] == "2"):  #ID you want to change
        # print ("TRUE")
        listlist[0] = "1"     #New ID 

    # print (listlist)

    sub = listlist[1:]
    # print(sub)

    adham = [listlist[0], sub[0], sub[1], sub[2], sub[3]]
    # print (adham)

    string = adham[0] + " " + adham[1] + " " + adham[2] + " " + adham[3] + " " + adham[4] + "\n"
    # print (string)

    final.append(string)

    i += 1
    length -= 1

print(final)

file1.writelines(final)

file1.close()
