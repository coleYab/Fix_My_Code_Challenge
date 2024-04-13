#!/usr/bin/python3
""" Documentations """


class Square():
    """ Documentations """

    def __init__(self, *args, **kwargs):
        """ Documentations """

        self.__width = 0
        self.__height = 0
        if (len(kwargs)) == 0:
            if (len(args)) == 1:
                self.width = args[0]
                self.height = args[0]
        for key, value in kwargs.items():
            if "size" in kwargs.keys():
                self.width = kwargs["size"]
                self.height = kwargs["size"]
                break
            setattr(self, key, value)

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width has to be integer")
        if value < 0:
            raise ValueError("width has to be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height has to be integer")
        if value < 0:
            raise ValueError("height has to be > 0")
        self.__height = value

    def area_of_my_square(self):
        """ Area of the Square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Documentations """

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Documentations """

        return f"{self.width}/{self.height}"


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
    s.width = 23
    print(s)
