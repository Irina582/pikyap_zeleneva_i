from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def demonstrate_seaborn_simple():
    """
    Простая демонстрация seaborn - гистограмма площадей фигур
    """
    print("\n" + "=" * 50)
    print("Демонстрация работы с Seaborn:")

    try:
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd

        # Создаем данные для гистограммы
        N = 5

        # Создаем фигуры
        rectangle = Rectangle(N, N, "синий")
        circle = Circle(N, "зеленый")
        square = Square(N, "красный")

        # Собираем данные в DataFrame
        data = {
            'Фигура': ['Прямоугольник', 'Круг', 'Квадрат'],
            'Площадь': [rectangle.area(), circle.area(), square.area()],
            'Цвет': ['синий', 'зеленый', 'красный']
        }

        df = pd.DataFrame(data)

        # Создаем гистограмму
        plt.figure(figsize=(10, 6))
        plot = sns.barplot(data=df, x='Фигура', y='Площадь', palette=['blue', 'green', 'red'])

        # Настройки графика
        plot.set_title('Площади геометрических фигур', fontsize=16, fontweight='bold')
        plot.set_xlabel('Фигура', fontsize=12)
        plot.set_ylabel('Площадь', fontsize=12)

        # Добавляем значения на столбцы
        for i, row in df.iterrows():
            plot.text(i, row['Площадь'] + 0.1, f"{row['Площадь']:.2f}",
                      ha='center', va='bottom', fontweight='bold')

        # Сохраняем график
        plt.tight_layout()
        plt.savefig('figures_histogram.png', dpi=150)
        print("✓ Гистограмма сохранена как 'figures_histogram.png'")

        # Показываем информацию о seaborn
        print(f"✓ Используется Seaborn версии {sns.__version__}")

    except ImportError as e:
        print(f"✗ Ошибка: Не удалось импортировать seaborn")
        print(f"  Установите: pip install seaborn matplotlib pandas")
        print(f"  Детали: {e}")
    except Exception as e:
        print(f"✗ Ошибка при построении графика: {e}")
        # Сохраняем график
    plt.tight_layout()
    plt.savefig('figures_histogram.png', dpi=150)
    print("✓ Гистограмма сохранена как 'figures_histogram.png'")
    plt.show()

def main():
    """
    Основная функция программы
    """
    # Номер варианта
    N = 5

    print("=" * 50)
    print("ГЕОМЕТРИЧЕСКИЕ ФИГУРЫ")
    print("=" * 50)

    # Создаем объекты согласно заданию
    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    # Выводим подробную информацию о каждой фигуре
    print("\n1. ПРЯМОУГОЛЬНИК:")
    print(f"   Название: {rectangle.get_figure_name()}")
    print(f"   Цвет: {rectangle.color_obj.color}")
    print(f"   Ширина: {rectangle.width}")
    print(f"   Высота: {rectangle.height}")
    print(f"   Площадь: {rectangle.area():.2f}")
    print(f"   Строковое представление: {rectangle}")

    print("\n2. КРУГ:")
    print(f"   Название: {circle.get_figure_name()}")
    print(f"   Цвет: {circle.color_obj.color}")
    print(f"   Радиус: {circle.radius}")
    print(f"   Площадь: {circle.area():.2f}")
    print(f"   Строковое представление: {circle}")

    print("\n3. КВАДРАТ:")
    print(f"   Название: {square.get_figure_name()}")
    print(f"   Цвет: {square.color_obj.color}")
    print(f"   Сторона: {square.side}")
    print(f"   Площадь: {square.area():.2f}")
    print(f"   Строковое представление: {square}")

    # Итоговая таблица
    print("\n" + "=" * 50)
    print("ИТОГОВАЯ ТАБЛИЦА:")
    print("-" * 50)
    print(f"{'Фигура':<15} {'Цвет':<10} {'Параметр':<10} {'Значение':<10} {'Площадь':<10}")
    print("-" * 50)
    print(f"{'Прямоугольник':<15} {'синий':<10} {'ширина':<10} {N:<10} {rectangle.area():<10.2f}")
    print(f"{'Круг':<15} {'зеленый':<10} {'радиус':<10} {N:<10} {circle.area():<10.2f}")
    print(f"{'Квадрат':<15} {'красный':<10} {'сторона':<10} {N:<10} {square.area():<10.2f}")
    print("-" * 50)

    # Сумма площадей
    total_area = rectangle.area() + circle.area() + square.area()
    print(f"\nСуммарная площадь всех фигур: {total_area:.2f}")

    # Демонстрируем работу seaborn (гистограмма)
    demonstrate_seaborn_simple()

    print("\n" + "=" * 50)
    print("ПРОГРАММА ЗАВЕРШЕНА")
    print("=" * 50)


if __name__ == "__main__":
    main()