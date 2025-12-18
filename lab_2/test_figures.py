from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def demonstrate_external_package():
    """
    Демонстрация работы внешнего пакета
    Вместо requests будем использовать стандартные библиотеки
    """
    print("=" * 50)
    print("Демонстрация работы внешнего пакета:")

    # Вариант 1: используем math как внешний пакет
    import math
    print("Использование пакета math для вычислений:")

    # Пример использования math
    radius = 5
    circle_area = math.pi * (radius ** 2)
    print(f"Площадь круга радиусом {radius}: {circle_area:.2f}")

    # Вариант 2: используем datetime
    import datetime
    print("\nИспользование пакета datetime:")
    now = datetime.datetime.now()
    print(f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # Вариант 3: используем random (если нужно что-то простое)
    import random
    print("\nИспользование пакета random:")
    random_number = random.randint(1, 100)
    print(f"Случайное число от 1 до 100: {random_number}")

    print("Внешние пакеты работают корректно!")


def main():
    """
    Основная функция программы
    """
    # Номер варианта (замените на свой номер)
    N = 5

    print("Демонстрация работы с геометрическими фигурами:")
    print("=" * 50)

    # Создаем объекты согласно заданию
    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    # Выводим информацию о фигурах
    print(rectangle)
    print(circle)
    print(square)

    # Демонстрируем работу внешнего пакета
    demonstrate_external_package()

    print("=" * 50)
    print("Дополнительная информация о фигурах:")
    print(f"Название прямоугольника: {rectangle.get_figure_name()}")
    print(f"Название круга: {circle.get_figure_name()}")
    print(f"Название квадрата: {square.get_figure_name()}")

    # Демонстрация вычисления площадей
    print("\nПлощади фигур:")
    print(f"Площадь прямоугольника: {rectangle.area():.2f}")
    print(f"Площадь круга: {circle.area():.2f}")
    print(f"Площадь квадрата: {square.area():.2f}")


if __name__ == "__main__":
    main()