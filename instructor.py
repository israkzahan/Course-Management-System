import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CourseManagementSystem"]
mycol = mydb["instructor"]

mydict = { "_id":"2021","name": "TJ", "department": "cse", "email":"tj@ewubd.edu","course": [{"courseID":"01", "name":"JAVA"}, {"courseID": "02", "name":"C programming"}] }
mydict = { "_id":"2022","name": "DMAR", "department": "cse", "email":"dmar@ewubd.edu","course": [{"courseID":"01", "name":"JAVA"}, {"courseID": "04", "name":"C++"}, {"courseID": "05", "name":"Data Science"} ] }

x = mycol.insert_one(mydict)