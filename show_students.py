# maya

student_list = {1: {"student_id" : "id_1", "name": "sample_1", "attendance" : [True, False, True], "test": [75,80], "assignment": [80, 70, 75]},
                2: {"student_id" : "id_2", "name": "sample_2", "attendance" : [False,True, True], "test": [80,90], "assignment": [80, 70, 50]},
                3: {"student_id" : "id_3", "name": "sample_3", "attendance" : [True, True, True], "test": [100,100], "assignment": [100, 100, 95]}}

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