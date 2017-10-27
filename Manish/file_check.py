import  os
import os.path
print (os.path.isfile("data.json"))
print (os.path.exists("data.json"))

try:
    os.path.exists("data.json")

except FileNotFoundError:
        print("file not there")
else:
    print("file is there ")
    os.remove("data.json")