import psycopg2


def create_db():  # создает таблицы
   with psycopg2.connect(dbname='hmwrkpostgre', user='postgres', password = '1234') as con:
       with con.cursor() as cur:
           cur.execute('''
           CREATE TABLE student (
           id serial PRIMARY KEY,
           name character varying(100),
           gpa numeric(10,2),
           birth timestamp with time zone
           );

           CREATE TABLE course (
           id serial PRIMARY KEY,
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
               INSERT INTO student VALUES (default, %s, %s, %s)
               ''', (students['name'], students['gpa'], students['birth'])
               )
            cur.execute('''
               SELECT ID FROM STUDENT WHERE NAME = %s
               ''', (students['name'],)
               )
            data = cur.fetchall()
            cur.execute('''
                INSERT INTO student_course VALUES (default, %s, %s)
                ''', (data[0], course_id)
                        )


def add_student(student):  # просто создает студента
    with psycopg2.connect(dbname='hmwrkpostgre', user='postgres', password='1234') as con:
        with con.cursor() as cur:
            cur.execute('''
               INSERT INTO student VALUES (default, %s, %s, %s)
               ''', (student['name'], student['gpa'], student['birth'])
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
    student_dict = {'name': 'Митя Митин', 'gpa': '7', 'birth': '2000-04-04 20:00:00-07'}
    #add_student(student_dict)
    #get_student('8')
    #add_students('1', student_dict)
    get_students('1')


if __name__ == "__main__":
    main()
