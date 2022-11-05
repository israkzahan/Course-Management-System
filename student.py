import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CourseManagementSystem"]
mycol = mydb["student"]

#mydict = { "_id":"2018-2-60-057","name": "Bob", "department": "cse", "phone":"01753443558","course": [{"courseID":"01", "name":"JAVA"}, {"courseID": "02", "name":"C programming"}] }
mydict = { "_id":"2018-2-60-056","name": "Alice", "department": "cse", "phone":"01908764521","course": [{"courseID":"01", "name":"JAVA"}, {"courseID": "02", "name":"C programming"}, {"courseID": "03", "name":"Algorithm"} ] }




x = mycol.insert_one(mydict)


