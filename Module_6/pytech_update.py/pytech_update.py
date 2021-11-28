from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.z5vqi.mongodb.net/cluster0?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})
print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: "+ doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Train Jr."}})
thomas = students.find_one({"student_id": "1007"})
print("\n --Displaying Student Document 1007 --")
print(" Student ID: " + thomas["student_id"] + "\n First Name: " + thomas["first_name"] + "\n Last name: " + thomas["last_name"] + "\n")
input("\n\n End of Program, press any key to continue...")