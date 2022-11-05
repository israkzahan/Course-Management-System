import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CourseManagementSystem"]
doccol = mydb["student"]
mycol = mydb["instructor"]
appcol = mydb["course"]
a=1
while a==1:
    print("Welcome to Course Mnagement System")
    print("____________________________________________")
    
    print("1. add student")
    print("2. update student")
    print("3. delete student")
    print("4. add instructor")
    print("5. update instructor")
    print("6. delete instructor")
    print("7. add course")
    print("8. update course ")
    print("9. delete course ")
    print("10. exit this system")
    a=int(input("Entre Your Option: "))
    if a==1:
        id=str(input("Enter your id:"))
        name=str(input("Enter your name: "))
        department=str(input("Enter your department: "))
        phone=str(input("Enter your phone: "))
        doccol.insert_one({ "_id":id, "name":name, "department":department, "phone":phone})

        print("Student added succesfully")

        #myquery = { "address": "Valley 345" }
        #newvalues = { "$set": { "address": "Canyon 123" } }

    elif a==2:
        mydoc=doccol.find()
        for x in mydoc:
            print("id: "+str(x['_id']))
            print("name: "+x['name'])
            print("department: "+x['department'])
            print("phone:"+x['phone'])

        id=str(input("Enter new student id for update: "))
        name=str(input("Enter new student name for update: "))
        department=str(input("Enter new student department for update: "))
        phone=str(input("Enter new student phone number for update: "))

        doccol.update_one({"_id":id},{"$set":{"name":name, "department":department,"phone":phone}}) 
  

        print("Student information updated succesfully")    

    elif a==3:
        mydoc=doccol.find()
        for x in mydoc:
            print("id: "+str(x['_id']))
            print("name: "+x['name'])
            print("department: "+x['department'])
            print("phone:"+x['phone'])
        a=input("Enter student Id for delete: ")
        doccol.delete_one({'_id':a})  

        print("Student deleted succesfully")    


    elif a==4:
        id=str(input("Enter instructor id:"))
        name=str(input("Enter instructor name: "))
        department=str(input("Enter instructor department: "))
        email=str(input("Enter instructor email: "))
        mycol.insert_one({"_id":id,  "name": name,  "department":department, "email":email})

        print("Instructor added succesfully")

    elif a==5:
        mydoc=mycol.find()
        for x in mydoc:
            print("id: "+str(x['_id']))
            print("name: "+x['name'])
            print("department: "+x['department'])
            print("email:"+x['email'])

        id=str(input("Enter instructor which want to be deleted: "))
        name=str(input("Enter new instructor name for update: "))
        department=str(input("Enter new instructor department for update: "))
        email=str(input("Enter new instructor email number for update: "))

        mycol.update_one({"_id":id},{"$set":{"name":name, "department":department,"email":email}}) 
  

        print("instructor information updated succesfully")   

    elif a==6:
        mydoc=mycol.find()
        for x in mydoc:
            print("id: "+str(x['_id']))
            print("name: "+x['name'])
            print("department: "+x['department'])
            print("email:"+x['email'])
        a=input("Enter instructor Id for delete: ")
        mycol.delete_one({'_id':a})  

        print("Instructor deleted succesfully") 

    elif a==7:
        id=str(input("Enter course id:"))
        name=str(input("Enter course name: "))
        department=str(input("Enter course department: "))
        
        appcol.insert_one({"_id":id,  "name": name,  "department":department})

        print("Course added succesfully")

    elif a==8:
        mydoc=appcol.find()
        for x in mydoc:
            print("id: "+str(x['_id']))
            print("name: "+x['name'])
            print("department: "+x['department'])
            #print("credit:"+x['credit'])

        id=str(input("Enter course ID which want to be updated: "))
        name=str(input("Enter new course name for update: "))
        department=str(input("Enter new course department for update: "))
        

        appcol.update_one({"_id":id},{"$set":{"name":name, "department":department}}) 
  

        print("Course information updated succesfully")    

    elif a==9:
        mydoc=appcol.find()
        for x in mydoc:
            print("id: "+str(x['_id']))
            print("name: "+x['name'])
            print("department: "+x['department'])
            #print("credit:"+x['credit'])

        a=input("Enter course Id for delete: ")
        appcol.delete_one({'_id':a})  

        print("Course deleted succesfully")    


    a=int(input("Enter 1 for run again:"))