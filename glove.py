class Glove:
    def __init__(self,color):
        self.__color=color
    def get_color(self,):
        return self.__color
    def set_color(self,color):
        self.__color=color
class Minion:
    def __init__(self,glove):
        self.__glove=glove
        self.__color="Violet"
    def get_glove(self):
        return self.__glove
orange_glove=Glove("Orange")
blue_glove=Glove("Blue")
bob=Minion(blue_glove)
special_glove=orange_glove
blue_glove.set_color(special_glove.get_color())
print(bob.get_glove().get_color())