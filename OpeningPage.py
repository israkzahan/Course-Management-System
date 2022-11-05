import pymongo
print("Welcome to Course Management System")
print("Who you are?")
print("1) Students")
print("2) Instructors")
print("3) Admin")
a=int(input("Enter Your Role: "))
if a==1:

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["CourseManagementSystem"]
    mycol = mydb["student"]

    mydoc = mycol.find()
    for a in mydoc:
        print(a)
elif a==2:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["CourseManagementSystem"]
    mycol = mydb["instructor"]

    mydoc = mycol.find()
    for a in mydoc:
        print(a)

elif a==3:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["CourseManagementSystem"]
    mycol = mydb["course"]

    mydoc = mycol.find()
    for a in mydoc:
        print(a)

    id=str(input("Enter course id:"))
    name=str(input("Enter course name: "))
    department=str(input("Enter course department: "))
    credit=float(input("Enter course credit: "))
    mycol.insert_one({"_id":id,  "name": name,  "department":department, "credit":credit})
        
        
    print("Course added succesfully")

    a=int(input("Enter 1 for run again:"))

else:
    print("Nothing to show you. Please exit the system")