class Student:
    """Представляет студента и его учебные результаты."""

    def __init__(self, name: str, age: int, average_grade: float):
        self.set_name(name)
        self.set_age(age)
        self.set_average_grade(average_grade)

    def set_name(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя не должно быть пустым.")
        self._name = name.strip()

    def get_name(self) -> str:
        return self._name

    def set_age(self, age: int) -> None:
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст должен быть положительным целым числом.")
        self._age = age

    def get_age(self) -> int:
        return self._age

    def set_average_grade(self, average_grade: float) -> None:
        grade = float(average_grade)
        if not 0 <= grade <= 10:
            raise ValueError("Средний балл должен быть в диапазоне от 0 до 10.")
        self._average_grade = grade

    def get_average_grade(self) -> float:
        return self._average_grade

    def get_grade(self) -> str:
        if self._average_grade > 8:
            return "Отлично"
        if self._average_grade >= 6:
            return "Хорошо"
        if self._average_grade >= 4:
            return "Удовлетворительно"
        return "Неудовлетворительно"

    @property
    def passed(self) -> bool:
        return self._average_grade >= 4

    def display_info(self) -> None:
        print(f"Имя: {self._name}")
        print(f"Возраст: {self._age}")
        print(f"Средний балл: {self._average_grade:.2f}")
        print(f"Оценка: {self.get_grade()}")
        print(f"Зачёт: {'Да' if self.passed else 'Нет'}")
        print("-" * 30)


if __name__ == "__main__":
    student1 = Student("Иван", 20, 9.2)
    student2 = Student("Мария", 21, 7.5)
    student3 = Student("Алексей", 19, 3.8)

    students = [student1, student2, student3]

    for student in students:
        student.display_info()

    # Демонстрация изменения свойств через методы
    student2.set_average_grade(8.6)
    student2.set_age(22)
    print("После изменения данных:")
    student2.display_info()
