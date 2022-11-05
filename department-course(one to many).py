import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CourseManagementSystem"]
mycol = mydb["department_course"]

mydict = { "_id":"111", "department": "CSE", "location":"MainBuilding","course": [{"courseID":"01", "name":"JAVA","dept":"cse"}, {"courseID": "02", "name":"Algorithm","dept": "cse"}] }

mydict = { "_id":"222", "department": "EEE", "location":"AB1","course": [{"courseID":"06", "name":"Electronic","dept":"cse"}, {"courseID": "02", "name":"Electronics","dept": "EEE"}] }

x = mycol.insert_one(mydict)