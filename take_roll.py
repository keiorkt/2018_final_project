# usei

student_list = {1: {"student_id" : "id_1", "name": "sample_1", "attendance" : [True, False, True]},
                2: {"student_id" : "id_2", "name": "sample_2", "attendance" : [False,True, True]},
                3: {"student_id" : "id_3", "name": "sample_3", "attendance" : [True, True, True]}}

def take_attendance(student_list):
  for i in range(len(student_list)):
    print("Is " + student_list[i+1]["name"] + " here? (yes/no)")
    attendance_4 = input().lower()
    if attendance_4 == "yes":
      student_list[i+1]["attendance"].append(True)
    elif attendance_4 == "no":
      student_list[i+1]["attendance"].append(False)
  print(student_list)

take_attendance(student_list)
