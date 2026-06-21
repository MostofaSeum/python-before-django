#video link: https://youtu.be/078tYSD7K8E?si=dbDPksMeGIndv8bC

info = {
    "name": "Seum",
    "age": 23,
    "city": "Dhaka"
}
# print(info["name"])

#Null Dictionary
null_dict = {}
null_dict["name"] = "Seum"
# print(null_dict)

#Nested Dictionary
student ={
    "name":"seum",
    "score":{
        "bangla":80,
        "english":90,
        "math":95
    }
}

student["total"]=100
print(student)

# print(student)
# print(student["score"])
print(student.keys())
print(student.values())
print(student.items())
