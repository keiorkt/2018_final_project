
def display_student_data(student_list):
  print("---------------------------------------------------------------------------------------------------------")
  print("<Student Data>")
  for i in range(len(student_list)):
    i += 1
    attend_count = student_list[i]["attendance"].count(True)
    absent_count = student_list[i]["attendance"].count(False)
    print("ID: " + student_list[i]["student_id"] + ", " +
          "Name: " + student_list[i]["name"] + ", " +
          "Attendance: " + str(attend_count) + ", " +
          "Absence: " + str(absent_count) + ", " +
          "Test Score: " + str(student_list[i]["test"][0]) + "/" + str(student_list[i]["test"][1]) + ", " +
          "Assignment: " +
          str(student_list[i]["assignment"][0]) + "/" +
          str(student_list[i]["assignment"][1]) + "/" +
          str(student_list[i]["assignment"][2]))
  print("---------------------------------------------------------------------------------------------------------\n")