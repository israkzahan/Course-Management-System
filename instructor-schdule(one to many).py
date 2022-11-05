import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CourseManagementSystem"]
mycol = mydb["instructor-schedule"]

mydict = { "_id":"2021","name": "TJ", "department": "cse", "email":"tj@ewubd.edu","schedule": [{"scheduleID": "001","courseID":"01", "instructorID":"2021"}, {"scheduleID": "002","courseID":"02", "instructorID":"2023"}] }
mydict = { "_id":"2022","name": "DMAR", "department": "cse", "email":"dmar@ewubd.edu","schedule": [{"scheduleID": "003","courseID":"03", "instructorID":"2022"}, {"scheduleID": "004","courseID":"04", "instructorID":"2024"}] }

x = mycol.insert_one(mydict)