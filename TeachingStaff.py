class TEachingStaff:
    def __init__(self,salary,no_of_classess):
        self.__salary=salary
        self.__no_of_classess=no_of_classess
    def calculate_salary(self):
        new_salary=self.__salary
        if(self.__no_of_classess>4):
            hike=3
            new_salary+=(hike/100)*self.__salary
        else:
            hike=3
            new_salary+=(hike/100)*self.__salary
        print(new_salary)

class NonTeachingStaff:
    def __init__(self,salary):
        self.__salary=salary
    def calculate_salary(self):
        new_salary=self.__salary
        if(self.__salary>=20000):
            hike=5
            new_salary+=(hike/100*self.__salary)
            if(self.__salary>=20000):
                hike=5
                new_salary+=(hike/100)*self.__salary
            else:
                hike=0
            print(new_salary)