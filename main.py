import sqlite3 as sql

with sql.connect("students.db") as con:
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
                   name STR, lastname STR,
                   hobby STR,
                   homework_grades INTEGER DEFAULT 0
                   )''')
    
    cursor.execute('''INSERT INTO students(name, lastname, hobby, homework_grades)
                   VALUES
                   ("one", "oneson", "math", 1),
                   ("two", "secondson", "math", 20),
                   ("three", "threesome", "math", 3),
                   ("four", "furryson", "math", 40),
                   ("five", "the fifth", "math", 5),
                   ("six", "the sexiest", "math", 60),
                   ("seven", "seventhson", "math", 7),
                   ("eight", "eightson", "math", 80),
                   ("nine", "reznor", "math", 9),
                   ("ten", "tennison", "math", 100)
                   ''')
    
    cursor.execute('''SELECT * FROM students WHERE LENGTH(lastname) > 10''')
    for i in cursor.fetchall():
        print("Достали: " + str(i))

    cursor.execute('''UPDATE students SET name="genius" WHERE homework_grades > 10''')

    cursor.execute('''SELECT * FROM students WHERE name == "genius"''')
    for i in cursor.fetchall():
        print("Geniuses: " + str(i))

    cursor.execute('''DELETE FROM students WHERE (rowid % 2 == 0)''')
    
