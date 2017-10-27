import json
import os
import subprocess

gitlog= "git log > git_log.txt"
subprocess.call(gitlog,shell=True)

def Fun_delete_file_Json_file():
    try:
        os.path.exists("data.json")

    except FileNotFoundError:
        print("file not there")
    else:
        print("file is there ")
        os.remove("data.json")

def Fun_files_print_log():

    with open("data.json", 'r')as fd:
        print("in call")
        JS_Data=json.load(fd,)
        for line in JS_Data:
            print("Commit", line["Commit"])
            string = "git show --pretty="" --name-only " + line["Commit"]
            subprocess.call(string, shell=True)
            print("\n\n\n")


# main function starts here

Fun_delete_file_Json_file()
with open('git_log.txt','r') as fd:
    data =fd.readlines()
    size=len(data)-1
    j=0
    j_list=[]

J_data = []
for i, line in enumerate(data):
    if "Author:" in line and size != j:
        for j in range(i-1,i+5):
            if data[j] != "\n":
                j_list.append(data[j])
                if(size == j):
                    break

        J_data.append(
        {
            'Commit': j_list[0].split(" ")[1].rstrip("\n"),
            'Auther': j_list[1].split(":")[1].rstrip("\n"),
            'Date'  : j_list[2].split(":")[1].rstrip("\n"),
            'Dev_Comment': j_list[3].lstrip(" ")
        }
        )

        with open("data.json", 'w')as fd:
            json.dump(J_data, fd, indent=4)

        j_list.clear()

Fun_files_print_log()