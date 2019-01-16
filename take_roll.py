# usei

student_list = {1: {"student_id" : "id_1", "name": "sample_1", "attendance" : [True, False, True], "test": [75,80], "assignment": [80, 70, 75]},
                2: {"student_id" : "id_2", "name": "sample_2", "attendance" : [False,True, True], "test": [80,90], "assignment": [80, 70, 50]},
                3: {"student_id" : "id_3", "name": "sample_3", "attendance" : [True, True, True], "test": [90,95], "assignment": [100, 90, 95]}}


def take_attendance(student_list):
  for i in range(len(student_list)):
    print("Is " + student_list[i+1]["name"] + " here? (yes/no)")
    attendance_4 = input().lower()
    if attendance_4 == "yes":
      student_list[i+1]["attendance"].append(True)
    else:
      student_list[i+1]["attendance"].append(False)
