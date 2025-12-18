from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    """
    Класс 'Прямоугольник' наследуется от класса 'Геометрическая фигура'
    """

    FIGURE_NAME = "Прямоугольник"

    def __init__(self, width, height, color):
        """
        Конструктор класса Rectangle

        Args:
            width (float): Ширина прямоугольника
            height (float): Высота прямоугольника
            color (str): Цвет прямоугольника
        """
        self.width = width
        self.height = height
        self.color_obj = Color(color)

    def area(self):
        """
        Метод для вычисления площади прямоугольника

        Returns:
            float: Площадь прямоугольника
        """
        return self.width * self.height

    def get_figure_name(self):
        """
        Метод для получения названия фигуры

        Returns:
            str: Название фигуры
        """
        return Rectangle.FIGURE_NAME

    def __str__(self):
        """
        Метод для строкового представления объекта

        Returns:
            str: Строковое представление прямоугольника
        """
        return "{0} {1} шириной {2}, высотой {3} и площадью {4:.2f}".format(
            self.get_figure_name(),
            self.color_obj.color,
            self.width,
            self.height,
            self.area()
        )