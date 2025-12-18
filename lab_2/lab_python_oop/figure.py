from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный класс 'Геометрическая фигура'
    """

    @abstractmethod
    def area(self):
        """
        Абстрактный метод для вычисления площади фигуры
        """
        pass

    @abstractmethod
    def get_figure_name(self):
        """
        Абстрактный метод для получения названия фигуры
        """
        pass

    def __repr__(self):
        """
        Метод для строкового представления объекта
        """
        return self.__str__()

    @abstractmethod
    def __str__(self):
        """
        Абстрактный метод для строкового представления
        """
        pass