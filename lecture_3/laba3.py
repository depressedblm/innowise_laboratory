"""
Анализатор оценок студентов
"""

from typing import List, Dict, Optional


class StudentGradeAnalyzer:
    
    def __init__(self):
        self.students: List[Dict] = []  # список студентов

    def display_menu(self) -> None:
        print("\n--- Анализатор оценок студентов ---")
        print("1. Добавить нового студента")
        print("2. Добавить оценки для студента")
        print("3. Показать отчет")
        print("4. Найти лучшего студента")
        print("5. Выход")

    def add_new_student(self) -> None:
        name = input("Введите имя студента: ").strip()
        
        # Проверка существования студента
        if any(student['name'] == name for student in self.students):
            print(f"Студент '{name}' уже существует!")
            return
        
        new_student = {"name": name, "grades": []}
        self.students.append(new_student)
        print(f"Студент '{name}' добавлен!")

    def add_grades_for_student(self) -> None:
        name = input("Введите имя студента: ").strip()
        
        student = self._find_student_by_name(name)
        if not student:
            print(f"Студент '{name}' не найден!")
            return
        
        print(f"Добавление оценок для {name}:")
        print("Введите 'done' для завершения")
        
        while True:
            grade_input = input("Введите оценку: ").strip().lower()
            
            if grade_input == 'done':
                break
                
            try:
                grade = int(grade_input)
                if 0 <= grade <= 100:
                    student['grades'].append(grade)
                    print(f"Оценка {grade} добавлена")
                else:
                    print("Оценка должна быть от 0 до 100!")
            except ValueError:
                print("Введите число или 'done'!")

    def show_report(self) -> None:
        if not self.students:
            print("Список студентов пуст!")
            return
        
        print("\n--- Отчет по студентам ---")
        averages = []  # список средних баллов
        
        for student in self.students:
            name = student['name']
            grades = student['grades']
            
            try:
                average = sum(grades) / len(grades)
                print(f"{name}: средний балл = {average:.2f}")
                averages.append(average)
            except ZeroDivisionError:
                print(f"{name}: средний балл = N/A")
        
        # Вывод статистики
        if averages:
            print("---")
            print(f"Максимальный средний: {max(averages):.2f}")
            print(f"Минимальный средний: {min(averages):.2f}")
            print(f"Общий средний: {sum(averages)/len(averages):.2f}")

    def find_top_performer(self) -> None:
        if not self.students:
            print("Список студентов пуст!")
            return
        
        # Студенты с оценками
        students_with_grades = [s for s in self.students if s['grades']]
        
        if not students_with_grades:
            print("Нет студентов с оценками!")
            return
        
        # Использование max с lambda как требуется
        top_student = max(
            students_with_grades,
            key=lambda s: sum(s['grades']) / len(s['grades'])  # lambda для среднего балла
        )
        
        top_average = sum(top_student['grades']) / len(top_student['grades'])
        print(f"Лучший студент: {top_student['name']} с баллом {top_average:.2f}")

    def _find_student_by_name(self, name: str) -> Optional[Dict]:
        # Поиск студента по имени
        for student in self.students:
            if student['name'].lower() == name.lower():
                return student
        return None

    def run(self) -> None:
        print("Анализатор оценок студентов запущен!")
        
        while True:
            try:
                self.display_menu()
                choice = input("Выберите опцию (1-5): ").strip()
                
                if not choice.isdigit():
                    print("Введите число от 1 до 5!")
                    continue
                
                choice = int(choice)
                
                if choice == 1:
                    self.add_new_student()
                elif choice == 2:
                    self.add_grades_for_student()
                elif choice == 3:
                    self.show_report()
                elif choice == 4:
                    self.find_top_performer()
                elif choice == 5:
                    print("Выход из программы!")
                    break
                else:
                    print("Выберите число от 1 до 5!")
                    
            except ValueError:
                print("Некорректный ввод!")
            except KeyboardInterrupt:
                print("\nПрограмма прервана")
                break


def main():
    analyzer = StudentGradeAnalyzer()
    analyzer.run()


if __name__ == "__main__":
    main()