import sqlite3
import os

def create_database():
    # Удаляем старую базу данных, если существует
    if os.path.exists('school.db'):
        os.remove('school.db')
        print("Старая база данных удалена")
    
    # Подключаемся к базе данных (файл создастся автоматически)
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    
    print("База данных 'school.db' создана")
    
    # 1. Создаем таблицу students
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
    )
    ''')
    
    # 2. Создаем таблицу grades
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        grade INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id),
        CHECK (grade >= 1 AND grade <= 100)
    )
    ''')
    
    print("Таблицы 'students' и 'grades' созданы")
    
    # 3. Вставляем данные студентов
    students = [
        ('Alice Johnson', 2005),
        ('Brian Smith', 2004),
        ('Carla Reyes', 2006),
        ('Daniel Kim', 2005),
        ('Eva Thompson', 2003),
        ('Felix Nguyen', 2007),
        ('Grace Patel', 2005),
        ('Henry Lopez', 2004),
        ('Isabella Martinez', 2006)
    ]
    
    cursor.executemany('INSERT INTO students (full_name, birth_year) VALUES (?, ?)', students)
    print(f"Добавлено {len(students)} студентов")
    
    # 4. Вставляем данные оценок
    grades = [
        (1, 'Math', 88),
        (1, 'English', 92),
        (1, 'Science', 85),
        (2, 'Math', 75),
        (2, 'History', 83),
        (2, 'English', 79),
        (3, 'Science', 95),
        (3, 'Math', 91),
        (3, 'Art', 89),
        (4, 'Math', 84),
        (4, 'Science', 88),
        (4, 'Physical Education', 93),
        (5, 'English', 90),
        (5, 'History', 85),
        (5, 'Math', 88),
        (6, 'Science', 72),
        (6, 'Math', 78),
        (6, 'English', 81),
        (7, 'Art', 94),
        (7, 'Science', 87),
        (7, 'Math', 90),
        (8, 'History', 77),
        (8, 'Math', 83),
        (8, 'Science', 80),
        (9, 'English', 96),
        (9, 'Math', 89),
        (9, 'Art', 92)
    ]
    
    cursor.executemany('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', grades)
    print(f"Добавлено {len(grades)} оценок")
    
    # 5. Создаем индексы для оптимизации
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_student_id ON grades(student_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_birth_year ON students(birth_year)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_subject ON grades(subject)')
    print("Индексы созданы для оптимизации запросов")
    
    # 6. Выполняем и показываем результаты запросов из задания
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ ЗАПРОСОВ:")
    print("="*50)
    
    # Запрос 3: Все оценки Alice Johnson
    print("\n3. Все оценки Alice Johnson:")
    cursor.execute('''
    SELECT s.full_name, g.subject, g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE s.full_name = 'Alice Johnson'
    ''')
    for row in cursor.fetchall():
        print(f"  {row[0]} - {row[1]}: {row[2]}")
    
    # Запрос 4: Средний балл каждого студента
    print("\n4. Средний балл каждого студента:")
    cursor.execute('''
    SELECT s.full_name, ROUND(AVG(g.grade), 2) as avg_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY avg_grade DESC
    ''')
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]}")
    
    # Запрос 5: Студенты, родившиеся после 2004 года
    print("\n5. Студенты, родившиеся после 2004 года:")
    cursor.execute('''
    SELECT full_name, birth_year
    FROM students
    WHERE birth_year > 2004
    ORDER BY birth_year
    ''')
    for row in cursor.fetchall():
        print(f"  {row[0]} (родился в {row[1]} году)")
    
    # Запрос 6: Средние оценки по предметам
    print("\n6. Средние оценки по предметам:")
    cursor.execute('''
    SELECT subject, ROUND(AVG(grade), 2) as avg_grade
    FROM grades
    GROUP BY subject
    ORDER BY avg_grade DESC
    ''')
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]}")
    
    # Запрос 7: Топ-3 студентов с наивысшим средним баллом
    print("\n7. Топ-3 студентов с наивысшим средним баллом:")
    cursor.execute('''
    SELECT s.full_name, ROUND(AVG(g.grade), 2) as avg_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 3
    ''')
    for i, row in enumerate(cursor.fetchall(), 1):
        print(f"  {i}. {row[0]}: {row[1]}")
    
    # Запрос 8: Студенты с оценками ниже 80
    print("\n8. Студенты с оценками ниже 80:")
    cursor.execute('''
    SELECT DISTINCT s.full_name, g.subject, g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE g.grade < 80
    ORDER BY s.full_name, g.grade
    ''')
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} - {row[2]}")
    
    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()
    
    print("\n" + "="*50)
    print(f"База данных успешно создана в файле: {os.path.abspath('school.db')}")
    print(f"Размер файла: {os.path.getsize('school.db')} байт")

if __name__ == "__main__":
    create_database()