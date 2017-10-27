import json
import os
import  feedparser

def Fun_delete_file_Json_file():
    try:
        os.path.exists("data.json")

    except FileNotFoundError:
        print("file not there")
    else:
        print("file is there ")
        os.remove("data.json")

def Fun_data_print():
    with open("data.json", 'r')as fd:
        data =json.load(fd)
        print(data)



def Fun_json(my_list):
    #print("mylist", my_list)
    data = {}
    data = []
    data.append(
        {
            'Commit':my_list[0].split(" ")[1].rstrip("\n"),
             'Auther':my_list[1].split(":")[1].rstrip("\n"),
             'Date': my_list[2].split(":")[1].rstrip("\n"),
             'Dev_Comment': my_list[3].lstrip(" ")
        }
    )
    with open("data.json", 'a')as fd:
        # print(fd)
        json.dump(data, fd,indent=4)



Fun_delete_file_Json_file()
with open('git_log.txt','r') as fd:
    print(fd)
    data =fd.readlines()
    size=len(data)-1
    #print("size", size)
    j=0
    j_list=[]

for i, line in enumerate(data):
    if "Author:" in line and size != j:
        #print(line)
        for j in range(i-1,i+5):
            if data[j] != "\n":
                #print("J-->%d data%s" %(j, data[j]))
                j_list.append(data[j])
                if(size == j):
                    break
        Fun_json(j_list)
        j_list.clear()
        print("\n\n")
#Fun_data_print()
