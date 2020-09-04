from Handler import StudentHandler
# handler = StudentHandler()
# handler.createDb()

q = ('1. 列出成績'+'\n'
    '2. 新增學生'+'\n'
    '3. 新增學生成績'+'\n'
    '4. 更新學生成績'+'\n'
    '5. 刪除學生成績'+'\n'
    '6. 離開'+'\n'
    '請選擇功能代號：')

handler = StudentHandler()
handler.createDb()

# handler.cursor.execute('SELECT * FROM Grade WHERE student = (?)',(101,))
# handler.cursor.execute('SELECT * FROM Student')
# rows = handler.cursor.fetchall()
# print(rows)

case = int(input(q))

while case != 6:
    if case == 1:
        handler.print_trans()
        case = int(input(q))
    elif case == 2:
        stu_code = int(input('請輸入學生學號：'))
        stu_name = int(input('請輸入學生名稱：'))
        
        handler.add_stu(stu_code, stu_name)

        case = int(input(q))
    elif case == 3:
        stu_code = int(input('請輸入學生學號：'))
        stu_sem = int(input('請輸入學期：'))
        stu_chi = int(input('請輸入國文成績：'))
        stu_eng = int(input('請輸入英文成績：'))
        stu_mth = int(input('請輸入數學成績：'))
        
        handler.add_grade(stu_sem, stu_chi, stu_eng, stu_mth, stu_code)

        case = int(input(q))
    elif case == 4:
        stu_code = int(input('請輸入學生學號：'))
        stu_sem = int(input('請輸入學期：'))
        stu_chi = int(input('請輸入國文成績：'))
        stu_eng = int(input('請輸入英文成績：'))
        stu_mth = int(input('請輸入數學成績：'))

        handler.update_grade(stu_sem, stu_chi, stu_eng, stu_mth, stu_code)

        case = int(input(q))
    elif case == 5:
        stu_code = int(input('請輸入學生學號：'))
        stu_name = int(input('請輸入學期：'))

        handler.delete_grade(stu_code, stu_name)

        case = int(input(q))
    else:
        print('輸入格式有誤')
        case = int(input(q))

    

   

        
