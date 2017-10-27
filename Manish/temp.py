import json
import subprocess

#gitlog= "git log > git_log.txt"
#subprocess.call(gitlog,shell=True)




with open('git_log.txt','r') as fd:
    print(fd)
    data =fd.readlines()
    size=len(data)-1
    #print("size",size)
    t_list=[]

print("\n\n\n")
for i, line in enumerate(data):
    if("commit" in line and size != i):
        for j in range(i,i+5):
                if(data[j] != "\n"):
                 print("j", j)
                 print("i", i)
                 print(data[j])
                 t_list.append(data[j])

        print(t_list)
        t_list.clear()
        print("Empty",t_list)
        print("\n\n\n")

