from collections import Counter

attendance = {
    "Rahul": ["P", "P", "A", "P", "P"],
    "Priya": ["P", "P", "P", "P", "A"],
    "Aman": ["P", "A", "P", "P", "P"],
    "Sneha": ["A", "P", "A", "P", "P"],
    "Karan": ["P", "P", "P", "P", "P"]
}

def analyze_attendance(attendance):
    attendance_summary={}
    for student,records in attendance.items():
        count=Counter(records)
        total_classes=len(records)
        present_count=count.get("P",0)
        absent_count=count.get("A",0)
        attendance_percentage=(present_count/total_classes)*100

        above_75=dict(filter(lambda x:x[1]>75,{"Above 75%":attendance_percentage}.items()))
        attendance_summary[student]={
            "Total Classes":total_classes,
            "Present":present_count,
            "Absent":absent_count,
            "Attendance Percentage":attendance_percentage,
            "Above 75%":above_75
        }
    return attendance_summary

def filter_students(data,**conditions):
    minimum_percentage=conditions.get("minimum_percentage",0)
    above_75=conditions.get("above_75",False)
    maximum_percentage=conditions.get("maximum_percentage",100)
    return {
        name:details for name,details in data.items() if details["Attendance Percentage"]>=minimum_percentage and details["Attendance Percentage"]<=maximum_percentage and (not above_75 or details["Attendance Percentage"]>75)
    }
#report
for student,details in analyze_attendance(attendance).items():
    print(f"Student: {student}")
    for key,value in details.items():
        print(f"{key}: {value}")
    else:
        print("Attendance analysis completed for the student.\n")
    
