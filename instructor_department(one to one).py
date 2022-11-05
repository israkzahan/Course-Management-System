import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CourseManagementSystem"]
mycol = mydb["instructor_department"]

#mydict = {"_id":"chairperson","name": "TJ", "department": "cse", "email":"tj@ewubd.edu","department":[{"instructor_id": "chairperson","department": "CSE", "location":"MainBuilding"}] }

#mydict = {"_id":"111","name": "DMAH", "department": "eee", "email":"dmah@ewubd.edu","department":[{"instructor_id": "111","department": "EEE", "location":"AB1"}] }
mydict = {"_id":"222","name": "MD.Salah Uddin", "department": "CSE", "email":"uddin@ewubd.edu","department":[{"instructor_id": "222","department": "CSE", "location":"Main Building"}] }

x = mycol.insert_one(mydict)
print(x);