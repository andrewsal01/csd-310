from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.z5vqi.mongodb.net/cluster0?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
one = {
    "student_id": "1007",
    "first_name": "Thomas",
    "last_name": "Train",
    "enrollments": [
        {
            "term": "Term 1",
            "gpa": 1.0,
            "start_date": "January 1, 2021",
            "end_date": "March 10, 2021",
            "courses": [
                {
                    "course_id": "Course 1",
                    "description": "Coding",
                   "instructor": "Fred",
                    "grade": "C"
                },
                {
                    "course_id": "Course 2",
                    "description": "Database",
                    "instructor": "Velma",
                    "grade": "A"
                }
            ]
        }
    ]

}
two = {
    "student_id": "1008",
    "first_name": "Steve",
    "last_name": "Irwin",
    "enrollments": [
        {
            "term": "Term 2",
            "gpa": 2.00,
            "start_date": "February 2, 2022",
            "end_date": "May 2, 2022",
            "courses": [
                {
                    "course_id": "Course 2",
                    "description": "Fry Cook",
                    "instructor": "SpongeBob",
                    "grade": "C"
                },
                {
                    "course_id": "Course 22",
                    "description": "Driving",
                    "instructor": "Puff",
                    "grade": "B"
                }
            ]
        }
    ]
}

three = {
    "student_id": "1009",
    "first_name": "Tom",
    "last_name": "Brady",
    "enrollments": [
        {
            "term": "Term 3",
            "gpa": 3.0,
            "start_date": "March 3, 2023",
            "end_date": "June 13, 2023",
            "courses": [
                {
                    "course_id": "Course 3",
                    "description": "TeamWork",
                    "instructor": "Belichick",
                    "grade": "A+"
                },
                {
                    "course_id": "Course 4",
                    "description": "Defense",
                    "instructor": "Covington",
                    "grade": "B"
                }
            ]
        }
    ]
}
students = db.students
print("\n  -- INSERT STATEMENTS --")
one_student_id = students.insert_one(one).inserted_id
print("  Inserted student record One Won into the students collection with document_id " + str(one_student_id))

two_student_id = students.insert_one(two).inserted_id
print( " Inserted student record Two Too into the students collection with document_id " + str(two_student_id))

three_student_id = students.insert_one(three).inserted_id
print("  Inserted student record Three Thirty into the students collection with document_id "+ str(three_student_id))