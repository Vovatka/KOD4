class Shape:
    def __init__(self):
        self._position = (0, 0)
        self._scale = 1
        self._color = None

    def set_positon(self, position):
        self._position = position

    def set_scale(self, scale):
        self._scale = scale

    def set_color(self, color):
        self._color = color

    def get_position(self):
        return self._position

    def get_scale(self):
        return self._scale

    def get_color(self):
        return self._color

    def info(self):
        print(f'Position: {self._position}',
              f'Scale: {self._scale}',
              f'Color: {self._color}',
              sep='\n')

    def area(self):
        print('Area: ', end='')


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.__width = 0
        self.__length = 0

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def set_width(self, width):
        self.__width = width

    def set_length(self, length):
        self.__length = length

    def info(self):
        super().info()
        print(f'Width: {self.__width}',
              f'Length: {self.__length}',
              sep='\n')

    def area(self):
        super().area()
        print(self.__length * self.__width)


class Trapezoid(Shape):
    def __init__(self):
        super().__init__()
        self.__top_base = 0
        self.__bottom_base = 0
        self.__h = 0

    def get_top_base(self):
        return self.__top_base

    def get_bottom_base(self):
        return self.__bottom_base

    def get_h(self):
        return self.__h

    def set_top_base(self, top_base):
        self.__top_base = top_base

    def set_bottom_base(self, bottom_base):
        self.__bottom_base = bottom_base

    def set_h(self, h):
        self.__h = h

    def info(self):
        super().info()
        print(f'Top base: {self.__top_base}',
              f'Bottom base: {self.__bottom_base}',
              f'H: {self.__h}',
              sep='\n')

    def area(self):
        super().area()
        print((self.__top_base + self.__bottom_base) *
              self.__h * 0.5)


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.__radius = 0

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def info(self):
        super().info()
        print(f'Radius: {self.__radius}')

    def area(self):
        super().area()
        print(3.14 * self.__radius * self.__radius)


rect = Rectangle()
rect.set_color('black')
rect.set_width(20)
rect.set_length(10)
rect.info()
rect.area()
print('----------------')
trap = Trapezoid()
trap.set_top_base(10)
trap.set_bottom_base(20)
trap.set_h(5)
trap.info()
trap.area()
print('----------------')
circle = Circle()
circle.set_radius(10)
circle.info()
circle.area()
