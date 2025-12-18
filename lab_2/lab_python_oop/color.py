class Color:
    """
    Класс 'Цвет фигуры' для описания цвета геометрической фигуры
    """

    def __init__(self, color):
        """
        Конструктор класса Color

        Args:
            color (str): Название цвета
        """
        self._color = color

    @property
    def color(self):
        """
        Свойство для получения цвета

        Returns:
            str: Название цвета
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Сеттер для установки цвета

        Args:
            value (str): Новое название цвета
        """
        if not isinstance(value, str):
            raise ValueError("Цвет должен быть строкой")
        self._color = value

    def __str__(self):
        """
        Строковое представление объекта Color
        """
        return self._color