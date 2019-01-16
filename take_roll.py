
def take_attendance(student_list):
  for i in range(len(student_list)):
    print("Is " + student_list[i+1]["name"] + " here? (yes/no)")
    attendance_4 = input().lower()
    if attendance_4 == "yes":
      student_list[i+1]["attendance"].append(True)
    else:
      student_list[i+1]["attendance"].append(False)
