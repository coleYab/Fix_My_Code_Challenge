#!/usr/bin/python3
""" Documentations """


class Square():
    """ Documentations """

    def __init__(self, *args, **kwargs):
        """ Documentations """

        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the Square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Documentations """

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Documentations """

        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Documentations """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
