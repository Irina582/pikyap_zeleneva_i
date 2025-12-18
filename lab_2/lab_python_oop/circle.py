from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math


class Circle(Figure):
    """
    Класс 'Круг' наследуется от класса 'Геометрическая фигура'
    """

    FIGURE_NAME = "Круг"

    def __init__(self, radius, color):
        """
        Конструктор класса Circle

        Args:
            radius (float): Радиус круга
            color (str): Цвет круга
        """
        self.radius = radius
        self.color_obj = Color(color)

    def area(self):
        """
        Метод для вычисления площади круга

        Returns:
            float: Площадь круга
        """
        return math.pi * (self.radius ** 2)

    def get_figure_name(self):
        """
        Метод для получения названия фигуры

        Returns:
            str: Название фигуры
        """
        return Circle.FIGURE_NAME

    def __str__(self):
        """
        Метод для строкового представления объекта

        Returns:
            str: Строковое представление круга
        """
        return "{0} {1} радиусом {2} и площадью {3:.2f}".format(
            self.get_figure_name(),
            self.color_obj.color,
            self.radius,
            self.area()
        )