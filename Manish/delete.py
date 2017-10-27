import json
#jsondata = {"name":"mohansa","age":30}
#jsondata1 = {"name":"sakethram","age":12}


data = { }
data = []

data.append(
    {
        "name":"manju",
        "age":30,
        "sex":"M"
    })
data.append(
    {
        "name":"lekshana",
        "age":3,
        "sex":"F"
    })

with open("delete.json","a") as fd:
    json.dump(data, fd,indent=2)
    #json.dump(jsondata1, fd, indent=2)

#    print(data)