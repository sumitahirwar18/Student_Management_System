import csv
student_database= {}


while True:
    print("\n===================================")
    print("--- STUDENT MANAGEMENT SYSTEM ---")
    print("=====================================") 
    print("1. Add Student")
    print("2. View all Students")
    print("3. Save Data to CSV")
    print("4. Exit")
    print("=================================")
   

    choice=input("Enter your choice(1-4):")

    if choice=="1":
       print("\n--- Add New Student ---")
       student_id=input("Enter Student ID(e.g. STU101):")
       
       if student_id in student_database:
        print(f"\n [ERROR]: Student with ID {student_id} already exists!")
       else:
        Name=input("Enter student name ")
        Age=int(input("Enter Student age "))
        Grade=input("Enter Student Grade (A/B/C/D/F) ").upper()
        Attendance=float(input("Enter attendance percentage(0-100) "))


        student_database[student_id]={
           
           "Name":Name,
           "Age":Age,
           "Grade":Grade,
           "Attendance":Attendance
        }

        print(f"\n[Success]: Student name added successfully!")

    elif choice=="2":
        print("\n--- Student Records ---")   

        if not student_database:
           print("\n[System] : No records found. The database is empty")
        else:
           for sid,details in student_database.items():
              print(f"ID:{sid}|Name:{details['Name']}|Age:{details['Age']}|"
                    f"Grade:{details['Grade']}|Attendance:{details['Attendance']}")

    elif choice=="3":
       print("\n --- Saving Data ---")
       if not student_database:
          print("\n[System]: No data available to save")
       else:
          with open('students.csv',mode='w',newline='') as file:
             writer= csv.writer(file)

             writer.writerow(['StudentID','Name','Age','Grade',"Attendance"])

             for sid,details in student_database.items():
                writer.writerow([sid,details['Name'],details['Age'],details['Grade'],details['Attendance']])
       print("\n[Success]: Data successfully saved to'students.csv'! ")

    elif choice=="4":
       print("\n [System]: Exiting program Thank you")
       break
    
    else:
       print("\n [System]: Invalid Choice,please select 1,2,or3 ")

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       