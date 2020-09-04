import sqlite3  # Handler.py 只能 import 這排，不能 import 其他東西

DB_NAME = 'db.sqlite'  # 定義全域變數

# 學生有 學號(id) 姓名(name)
SQL1 = ('CREATE TABLE IF NOT EXISTS "Student" ('
       '"code" INTEGER PRIMARY KEY,'
       '"name" TEXT)')

# 成績有 學期(semester) 國文(chinese) 英文(english) 數學(mathematics)
# 學生(student) 且 UNIQUE(semester, student)
SQL2 = ('CREATE TABLE IF NOT EXISTS "Grade" ('
       '"id" INTEGER PRIMARY KEY AUTOINCREMENT,'
       '"semester" INTEGER,'
       '"chinese" INTEGER,'
       '"english" INTEGER,'
       '"mathematics" INTEGER,'
       '"student" INTEGER,'
       'FOREIGN KEY(student) REFERENCES Student(id),'
       'UNIQUE(semester, student))')

class Grade(object):

    def __init__(self, semester, chinese, english, mathematics, student):
        self.semester = semester
        self.chinese = chinese
        self.english = english
        self.mathematics = mathematics
        self.student = student


class Student(object):

    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.grades = []


class StudentHandler(object):

    def __init__(self):
        self.students = []
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        
    def createDb(self):
        self.cursor.execute(SQL1)
        self.cursor.execute(SQL2)
        self.cursor.execute('SELECT * FROM Student')
        student_list = self.cursor.fetchall()
        for x in student_list:
            currStu = Student(x[0], x[1])
            self.cursor.execute(
                'SELECT * FROM Grade WHERE student = (?)', (x[0],))
            for y in self.cursor.fetchall():
                currStu.grades.append(Grade(y[1], y[2], y[3], y[4], y[5]))
            self.students.append(currStu)
        self.conn.commit()
        

    def get_stu(self, code):
        for x in self.students:
            if x.code == code: return x

    def add_stu(self, code, name):
        currStu = Student(code, name)
        self.students.append(currStu)
        self.cursor.execute('INSERT INTO Student (code, name) VAlUES (?, ?)', (currStu.code, currStu. name))
        self.conn.commit()

    def add_grade(self, semester, chinese, english, mathematics, code):
        currGrade = Grade(semester, chinese, english, mathematics, code)
        currStu = self.get_stu(code)
        currStu.grades.append(currGrade)
        self.cursor.execute('INSERT INTO Grade (semester, chinese, english, mathematics, student)\
                    VALUES(?,?,?,?,?)', (
                        currGrade.semester,
                        currGrade.chinese,
                        currGrade.english,
                        currGrade.mathematics,
                        currGrade.student))
        self.conn.commit()

    def update_grade(self, semester, chinese, english, mathematics, code):
        currGrade = Grade(semester, chinese, english, mathematics, code)
        currStu = self.get_stu(code)
        for x in currStu.grades:
            if x.semester == currGrade.semester:
                curr_index = currStu.grades.index(x)
                currStu.grades[curr_index] = currGrade
                SQL = ''' UPDATE Grade
                          SET   chinese = ?,
                                english = ?,
                                mathematics = ?
                          WHERE semester = ?'''
                self.cursor.execute(SQL, (currGrade.chinese, currGrade.english, currGrade.mathematics, currGrade.semester))
                self.conn.commit()


    def delete_grade(self, code, sem):
        currStu = self.get_stu(code)
        for x in currStu.grades:
            if x.semester == sem:
                currStu.grades.remove(x)
                SQL = ''' DELETE FROM Grade
                          WHERE semester = ?'''
                self.cursor.execute(SQL, sem)
                self.conn.commit()
        

    def print_trans(self):
        for x in self.students:
            for y in x.grades:
                print('學號：{} 姓名：{}{} 學期：{} 國文：{} 英文：{} 數學：{}'.format(\
                        x.code, x.name, '\n', y.semester, y.chinese, y.english, y.mathematics))
    
    
        
