import json
import os
list =[10,20,30]

def Fun_delete_file_Json_file():
    try:
        os.path.exists("j_data.json")

    except FileNotFoundError:
        print("file not there")
    else:
        print("file is there ")
        os.remove("j_data.json")


def fun_json(num):
    print (num)
    data={}
    data=[]
    data.append(
        {
            "name":"Mohan",
            "age" :num
        }
    )
    with open("j_data.json","a") as fd:
        json.dump(data,fd,indent=2)
        fd.close()

Fun_delete_file_Json_file()

for i in list:
    #print(i)
    fun_json(i)