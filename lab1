import os

# Шлях до папки з файлами 
folder_path = "C:\Studying\pythan\Materials"

# Імена файлів
file_names = ["math.txt", "statistics.txt", "physics.txt", "student_names.txt"]

# Перевірка наявності файлів
data = {}
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(file_path):
        print(f"Файл '{file_name}' не знайдено.")
    else:
        print(f"Файл '{file_name}' знайдено.")
        with open(file_path, "r", encoding="utf-8") as file:
            data[file_name] = file.readlines()

# Зчитування даних
try:
    # Імена студентів
    student_names = [name.strip() for name in data["student_names.txt"]]
    
    # Оцінки за предметами
    subjects = {
        "math": [int(score.strip()) for score in data["math.txt"]],
        "statistics": [int(score.strip()) for score in data["statistics.txt"]],
        "physics": [int(score.strip()) for score in data["physics.txt"]],
    }

    # Формування словника оцінок студентів
    students_data = {}
    for i, name in enumerate(student_names):
        students_data[name] = {
            subject: subjects[subject][i] for subject in subjects
        }

    # Розрахунок середніх оцінок
    student_averages = {
        name: sum(scores.values()) / len(scores) for name, scores in students_data.items()
    }

    # Завдання 1: Загальна кількість студентів та статистика по кожному предмету
    print(f"\nЗагальна кількість студентів: {len(student_names)}")
    for subject, scores in subjects.items():
        avg_score = sum(scores) / len(scores)
        min_score = min(scores)
        max_score = max(scores)
        print(f"{subject.capitalize()}: середня оцінка {avg_score:.2f}, мін оцінка: {min_score}, макс оцінка: {max_score}")

    # Завдання 2: Ім'я студента з найвищим балом по кожному предмету
    print("\nСтуденти з найвищими оцінками по кожному предмету:")
    for subject, scores in subjects.items():
        max_score = max(scores)
        max_student = student_names[scores.index(max_score)]
        print(f"{subject.capitalize()}: студент: {max_student}, оцінка: {max_score}")

    # Завдання 3: Студенти з середньою оцінкою нижче 50
    low_average_students = [name for name, avg in student_averages.items() if avg < 50]
    print(f"\nКількість студентів з оцінкою нижче 50: {len(low_average_students)}")
    for student in low_average_students:
        print(student)

    # Завдання 4: Три студенти з найвищими середніми оцінками
    top_students = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\nТри студенти з найвищими середніми оцінками:")
    for student, avg_score in top_students:
        print(f"{student} - середня оцінка: {avg_score:.2f}")

    # Виведення загальної статистики
    print("\nСтатистика для кожного студента:")
    for name, avg_score in student_averages.items():
        print(f"Студент: {name}, середня оцінка: {avg_score:.2f}")

except KeyError as e:
    print(f"Помилка: Дані для '{e}' не були знайдені у файлах.")
except Exception as e:
    print(f"Сталася помилка: {e}")
