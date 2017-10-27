import json
import subprocess
import os

gitlog= "git log > git_log.txt"
subprocess.call(gitlog,shell=True)


def Fun_JS_Data_files(JS_Data):
    print(JS_Data)
    for line in JS_Data:
        print("Commit",line["Commit"])
        print("Auther",line["Auther"])
        string = "git show --pretty="" --name-only "+line["Commit"]
        subprocess.call(string,shell=True)
        #print("string",string)
        #print(git show --pretty="" --name-only bd61ad98)

def Fun_json_print():
    with open("data.json","r") as pd:
         data = json.load(pd)
         return data
        #print(data)
    #for line in data:
    #  print(line["commit"])

def Fun_json(my_list):
    print("mylist",my_list)
    data = {}
    data = []
    data.append(
        {
            #'Commit':my_list[0].split(" ")[1].rstrip("\n"),
            #'Auther':my_list[1].split(":")[1].rstrip("\n"),
            #'Date': my_list[2].split(":")[1].rstrip("\n"),
            #'Dev_Comment': my_list[3].lstrip(" ")
        }
    )
    with open("data.json", 'w')as fd:
        #print(fd)
        json.dump(data,fd)


with open('git_log.txt','r') as fd:
    print(fd)
    data =fd.readlines()
    size=len(data)-1
    t_list=[]

for i, line in enumerate(data):
    #print(line)
    if("commit" in line and size != i):
        for j in range(i,i+5):
            if(data[j] != "\n"):
                print(data[j])
                #t_list.append(data[j])
        print("\n\n ")
        #Fun_json(t_list)
        #print(t_list)
        t_list.clear()

JS_Data=Fun_json_print()
#print("js",JS_Data)

#Fun_JS_Data_files(JS_Data)