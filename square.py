class Square:
    def __init__(self,length):
        self.lenth=length
    def calculate_area(self):
        return  self.lenth*self.lenth
class Rectangle(Square):
    def __init__(self, length, breadth):
        super().__init__(length)
        self.__breadth=breadth
    def calculate_area(self):
        return self.lenth*self.__breadth
    def get_breadth(self):
        return self.__breadth
class Cuboid(Rectangle):
    def __init__(self, length, breadth, heigth):
        super().__init__(length, breadth)
        self.__height=heigth
    def calculate_surface_area(self):
        return 2*(super().calculate_area()+(self.get_breadth()*self.__height)+(self.lenth*self.__height))
box=Cuboid(30,10,10)
print("surface area:",box.calculate_surface_area())
print("area of one side:",box.calculate_area())


