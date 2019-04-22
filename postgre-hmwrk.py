import psycopg2


def create_db():  # создает таблицы
   with psycopg2.connect(dbname='hmwrkpostgre', user='postgres', password = '1234') as con:
       with con.cursor() as cur:
           cur.execute('''
           CREATE TABLE student (
           id integer PRIMARY KEY,
           name character varying(100),
           gpa numeric(10,2),
           birth timestamp with time zone
           );

           CREATE TABLE course (
           id integer PRIMARY KEY,
           name character varying(100) 
           );
           
            CREATE TABLE student_course(
            id serial PRIMARY KEY,
            student_id INTEGER REFERENCES student(id),
            course_id INTEGER REFERENCES course(id)
            )
           ''')


def get_students(course_id): # возвращает студентов определенного курса
    with psycopg2.connect(dbname='hmwrkpostgre', user='postgres', password='1234') as con:
        with con.cursor() as cur:
            cur.execute('''
                          SELECT STUDENT_ID FROM STUDENT_COURSE WHERE COURSE_ID = %s
                           ''', (course_id))
            data = cur.fetchall()
            get_student(data[0])


def add_students(course_id, students): # создает студентов из записывает их на курс
    with psycopg2.connect(dbname='hmwrkpostgre', user='postgres', password='1234') as con:
        with con.cursor() as cur:
            cur.execute('''
               INSERT INTO student VALUES (%s, %s, %s, %s)
               ''', (students['id'], students['name'], students['gpa'], students['birth'])
               )
            cur.execute('''
               INSERT INTO student_course(id, student_id, course_id) VALUES (default,%s, %s)
               ''', (students['id'], course_id)
               )


def add_student(student):  # просто создает студента
    with psycopg2.connect(dbname='hmwrkpostgre', user='postgres', password='1234') as con:
        with con.cursor() as cur:
            cur.execute('''
               INSERT INTO student VALUES (%s, %s, %s, %s)
               ''', (student['id'], student['name'], student['gpa'], student['birth'])
               )


def get_student(student_id):
    with psycopg2.connect(dbname='hmwrkpostgre', user='postgres', password='1234') as con:
        with con.cursor() as cur:
            cur.execute('''
              SELECT NAME FROM STUDENT WHERE ID = %s
               ''', (student_id))
            data = cur.fetchall()
            print(data[0])


def main():
    #create_db()
    student_dict = {'id': '2', 'name': 'Володя Володин', 'gpa': '7', 'birth': '2000-04-04 20:00:00-07'}
    #add_student(student_dict)
    #get_student('2')
    #add_students('4', student_dict)
    #get_students('4')


if __name__ == "__main__":
    main()
