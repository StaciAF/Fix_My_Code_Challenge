#!/usr/bin/python3
""" nothing imported """


class Square:
    """ defines Square class """

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_Square(self):
        """ Area of the square """
        return (self.width ** 2)

    def perimeter_of_my_Square(self):
        """ Perimeter of the square """
        return (self.width * 4)

    def __str__(self):
        """ string rep of square """
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_Square())
    print(s.perimeter_of_my_Square())
