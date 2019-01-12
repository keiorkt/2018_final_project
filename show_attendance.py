# maya

student_list = {1: {"student_id" : "id_1", "name": "sample_1","attendance" : [True, False, True]},
                2: {"student_id" : "id_2", "name": "sample_2", "attendance" : [False,True, True]},
                3: {"student_id" : "id_3", "name": "sample_3", "attendance" : [True, True, True]}}

def display_total_attendance(student_list):
  for i in range(len(student_list)):
    i += 1
    attend_count = student_list[i]["attendance"].count(True)
    absent_count = student_list[i]["attendance"].count(False)
    print("ID: " + student_list[i]["student_id"] + ", "
          "Name: " + student_list[i]["name"] + ", "
          "Attendance: " + str(attend_count) + ", "
          "Absence: " + str(absent_count)
          )

display_total_attendance(student_list)
