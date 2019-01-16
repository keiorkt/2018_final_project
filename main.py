import login
import take_roll
import show_students
import calculate_grade

teacher_accounts = {'a':'a'}
student_list = {1: {"student_id" : "id_1", "name": "sample_1", "attendance" : [True, False, True], "test": [75,80], "assignment": [80, 70, 75]},
                2: {"student_id" : "id_2", "name": "sample_2", "attendance" : [False,True, True], "test": [80,90], "assignment": [80, 70, 50]},
                3: {"student_id" : "id_3", "name": "sample_3", "attendance" : [True, True, True], "test": [100,100], "assignment": [100, 90, 95]}}


is_logged_in = login.ask_user_name(teacher_accounts)

while is_logged_in:
  command = int(input("what do you want to do? \n 1.Take roll \n 2.Show student data \n 3.Calculate grade \n 4.Exit \n\nEnter the number : "))
  if command == 1:
    take_roll.take_attendance(student_list)
  elif command == 2:
    show_students.display_student_data(student_list)
  elif command == 3:
    calculate_grade.calculate_grades(student_list)
  elif command == 4:
    print("Thank you")
    break
