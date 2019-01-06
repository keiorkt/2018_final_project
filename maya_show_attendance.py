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
