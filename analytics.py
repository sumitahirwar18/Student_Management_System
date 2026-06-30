import csv

total_students= 0
total_attendance= 0.0
grade_counts={}
at_risk_students=[]

try:
    with open('students.csv',mode='r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            total_students+=1

            attendance=float(row['Attendance'])
            total_attendance +=1


            grade=row['Grade']
            if grade in grade_counts:
                grade_counts[grade] +=1
            else:
                grade_counts[grade]=1

                if attendance<75.0:
                    at_risk_students.append((row['Name'],attendance))
    average_attendance= total_attendance/total_students if total_students > 0 else 0               


    print("\n ================================================")
    print("\n --- AUTOMATED STUDENT ANALYTICS REPORT ---")
    print("\n ================================================")
    print(f"Total Student Base Analyzed: {total_students}")
    print(f"Overall Average Attendance Ratio: {average_attendance:.2f}%")
    print("Grade Distribution Metric :")
    for g,count in grade_counts.items():
        print(f" - Grade{g}:{count} student(s)")
    print("----------------------------------------")
    print("Risk Assessment and Interventions:")    
    if at_risk_students:
        print(f"[ALERT]: Found {len(at_risk_students)} At-Risk Student(s) (Attendance<75%): ")
        for name,att in at_risk_students:
            print(f"*{name}(Attendance:{att}%)")
    else:
        print("[Status]: Excellent! No St8udentsare currently flagged at-risk")
        print("===============================================")

except FileNotFoundError:
    print("\n[Data Error]: 'students.csv' not found! run 'app.py' and save data first")            