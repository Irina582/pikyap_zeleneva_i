from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс 'Квадрат' наследуется от класса 'Прямоугольник'
    """

    FIGURE_NAME = "Квадрат"

    def __init__(self, side, color):
        """
        Конструктор класса Square

        Args:
            side (float): Длина стороны квадрата
            color (str): Цвет квадрата
        """
        super().__init__(side, side, color)
        self.side = side

    def get_figure_name(self):
        """
        Метод для получения названия фигуры

        Returns:
            str: Название фигуры
        """
        return Square.FIGURE_NAME

    def __str__(self):
        """
        Метод для строкового представления объекта

        Returns:
            str: Строковое представление квадрата
        """
        return "{0} {1} со стороной {2} и площадью {3:.2f}".format(
            self.get_figure_name(),
            self.color_obj.color,
            self.side,
            self.area()
        )