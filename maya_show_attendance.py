# student_listの内容
# no : 番号
# student_id: 学籍番号（適当）
# name: 名前(適当)
# attendance: 今まで出欠、配列 [1回目の授業、2回目の授業...]
# 1: {student_id: "id_1", name: "sample_1", attendance: [True,False]}

student_list = {1: {"student_id" : "id_1", "name": "sample_1","attendance" : [True, False, True]},
                2: {"student_id" : "id_2", "name": "sample_2", "attendance" : [False,True, True]},
                3: {"student_id" : "id_3", "name": "sample_3", "attendance" : [True, True, True]}}

# Task：一人一人の生徒の出席数、欠席数を表示するプログラミングを記述せよ

# 補足：True = 出席、False = 欠席
# 遅刻はあとで実装するので今は考えなくて良い

# True= Total number classes attended by particular Student

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

# student id: 1, name: "sample_1", attend: 2, absent: 1
