import sys
import math


def get_coef_from_args(args, index, name):
    """
    Получение коэффициентов из командной строки
    Возвращение коэффициента или None, если не удалось
    """
    if len(args) > index: # существует ли элемент с таким индексом
        try:
            value = float(args[index])
            print(f"Коэффициент {name} = {value} ")
            return value
        except ValueError:
            print(f"Ошибка: коэффициент {name} задан некорректно в командной строке")

    return None


def get_coef_from_input(name):
    """
    Получение коэффициента с клавиатуры и проверка на корректность
    Повтор ввода до тех пор, пока не будет введено корректное значение
    """
    while True:
        try:
            value = input(f"Введите коэффициент {name}: ")
            # Заменяем запятые на точки для корректного преобразования
            value = value.replace(',', '.')
            value = float(value)
            return value
        except ValueError:
            print("Ошибка: введите действительное число! Попробуйте снова.")


def solve_biquadratic(a, b, c):
    """
    Решает биквадратное уравнение A*x^4 + B*x^2 + C = 0
    Возвращает список действительных корней
    """
    print(f"\nРешение уравнения: {a}*x^4 + {b}*x^2 + {c} = 0")

    # Вычисляем дискриминант для квадратного уравнения относительно y = x^2
    discriminant = b ** 2 - 4 * a * c
    print(f"Дискриминант: {discriminant}")

    if discriminant < 0:
        print("Действительных корней нет")
        return []

    # Вычисляем корни для y = x^2
    y1 = (-b + math.sqrt(discriminant)) / (2 * a)
    y2 = (-b - math.sqrt(discriminant)) / (2 * a)

    real_roots = []

    # Находим x из y1 = x^2
    if y1 >= 0:
        if y1 == 0:
            real_roots.append(0.0)
        else:
            root1 = math.sqrt(y1)
            root2 = -math.sqrt(y1)
            real_roots.extend([root1, root2])

    # Находим x из y2 = x^2 (если y2 != y1)
    if y2 >= 0 and abs(y2 - y1) > 1e-10:
        if y2 == 0:
            if 0.0 not in real_roots:
                real_roots.append(0.0)
        else:
            root1 = math.sqrt(y2)
            root2 = -math.sqrt(y2)
            # Добавляем только уникальные корни
            if root1 not in real_roots:
                real_roots.append(root1)
            if root2 not in real_roots:
                real_roots.append(root2)

    # Сортируем корни для красивого вывода
    real_roots.sort()

    return real_roots


def display_roots(roots):
    """
    Выводит корни уравнения в удобном формате
    """
    if not roots:
        print("Уравнение не имеет действительных корней")
        return

    print(f"Найдено действительных корней: {len(roots)}")
    for i, root in enumerate(roots, 1):
        print(f"x{i} = {root:.6f}")


def main():
    print("Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0")
    # Получаем аргументы командной строки (игнорируем имя скрипта)
    args = sys.argv[1:]

    # Получаем коэффициенты A, B, C
    coefficients = []
    for i, name in enumerate(['A', 'B', 'C']):
        # Пытаемся получить коэффициент из командной строки
        coef = get_coef_from_args(args, i, name)

        # Если не получилось из командной строки, запрашиваем с клавиатуры
        if coef is None:
            coef = get_coef_from_input(name)

        coefficients.append(coef)

    a, b, c = coefficients

    # Проверяем особый случай, когда A = 0
    if a == 0:
        print("\nОшибка: коэффициент A не может быть равен 0 для биквадратного уравнения!")
        print("Это приведет к вырождению уравнения в квадратное.")
        response = input("Хотите продолжить решение как квадратного уравнения? (y/n): ")
        if response.lower() != 'y':
            print("Программа завершена.")
            return

        # Решаем как квадратное уравнение B*x^2 + C = 0
        if b == 0:
            if c == 0:
                print("Уравнение 0 = 0 имеет бесконечное количество решений")
            else:
                print(f"Уравнение {c} = 0 не имеет решений")
            return
        else:
            # Квадратное уравнение относительно x^2
            x_squared = -c / b
            if x_squared < 0:
                print("Действительных корней нет")
                return
            elif x_squared == 0:
                roots = [0.0]
            else:
                roots = [math.sqrt(x_squared), -math.sqrt(x_squared)]

            display_roots(roots)
            return

    # Решаем биквадратное уравнение
    roots = solve_biquadratic(a, b, c)

    # Выводим результаты
    print("\n" + "=" * 50)
    display_roots(roots)
    print("=" * 50)


# Пример использования параметров командной строки
if __name__ == "__main__":
    main()
