
# A_PLUS = 95
# A = 90
# B = 80
# C = 70
# D = 60

FINAL_RATIO = 0.6
MID_TERM_RATIO = 0.4
TEST_RATIO = 0.7
ASSIGNMENT_RATIO = 0.2
ATTENDANCE_RATIO = 0.1

def determine_grade(score):
    if score >= 95:
        return 'A+'
    elif score >= 90 and score < 95:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    else:
        return 'F'

def calculate_grade(student_data):
  mid_term_score = student_data["test"][0] * MID_TERM_RATIO
  final_score = student_data["test"][1] * FINAL_RATIO
  test_score = mid_term_score + final_score

  class_count = len(student_data["attendance"])
  attendance = student_data["attendance"].count(True)
  attendance_rate = attendance / class_count

  assignment_score = sum(student_data["assignment"]) / len(student_data["assignment"])

  final_score = test_score * TEST_RATIO + attendance_rate * 100 * ATTENDANCE_RATIO + assignment_score * ASSIGNMENT_RATIO
  grade = determine_grade(final_score)
  return grade

def calculate_grades(student_list):
  student_index = list(student_list.keys())
  print("--------------------------------------")
  print("<Student Grade>")
  for i in student_index:
    grade = calculate_grade(student_list[i])
    print("ID: " + student_list[i]["student_id"] + ", " +
           "Name: " + student_list[i]["name"] + ", " +
           "Grade : " + grade)
  print("--------------------------------------\n")
