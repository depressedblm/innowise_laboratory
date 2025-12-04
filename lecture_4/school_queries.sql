
-- 1. Создание таблиц
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    CHECK (grade >= 1 AND grade <= 100)
);

-- 2. Вставка данных (студенты)
INSERT INTO students (full_name, birth_year) VALUES 
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- 3. Вставка данных (оценки)
INSERT INTO grades (student_id, subject, grade) VALUES
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
(9, 'Art', 92);

-- 4. Создание индексов для оптимизации
CREATE INDEX IF NOT EXISTS idx_student_id ON grades(student_id);
CREATE INDEX IF NOT EXISTS idx_birth_year ON students(birth_year);
CREATE INDEX IF NOT EXISTS idx_subject ON grades(subject);

-- 5. Найти все оценки для конкретного студента (Alice Johnson)
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';

-- 6. Посчитать средний балл каждого студента
SELECT s.full_name, ROUND(AVG(g.grade), 2) as avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg_grade DESC;

-- 7. Вывести всех студентов, родившихся после 2004 года
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year;

-- 8. Вывести все предметы и их средние оценки
SELECT subject, ROUND(AVG(grade), 2) as avg_grade
FROM grades
GROUP BY subject
ORDER BY avg_grade DESC;

-- 9. Найти топ-3 студентов с наивысшим средним баллом
SELECT s.full_name, ROUND(AVG(g.grade), 2) as avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 3;

-- 10. Показать всех студентов, у которых есть хотя бы одна оценка ниже 80
SELECT DISTINCT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name, g.grade;