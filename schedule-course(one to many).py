import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CourseManagementSystem"]
mycol = mydb["schedule-course"]

#mydict = { "_id": "001","courseID":"01", "instructorID":"2021", "course": [{"courseID":"01", "name":"JAVA"}, {"courseID": "02", "name":"C programming"}] }

mydict = { "_id": "002","courseID":"01", "instructorID":"2021", "course": [{"courseID":"04", "name":"DBMS"}, {"courseID": "05", "name":"Algorithm"}] }

x = mycol.insert_one(mydict)