class Book:
    def __init__(self,title,author,publishing_year):
        self.title=title
        self.__author=author
        self.__publidhing_year=publishing_year
    def get_author(self):
        return self.__author
    def set_author(self,author):
        self.__author=author
book_obj1=Book("the Alchemist","Michael Scott",1988)
book_obj2=book_obj1

