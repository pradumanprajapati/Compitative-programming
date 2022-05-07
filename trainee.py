class Trainee:
    def __init__(self,is_colored_tag,trainee_name,trainee_salary):
        self.__is_colored_tag=is_colored_tag
        self.trainee_name=trainee_name
        self.__trainee_salary=trainee_salary
    def get_is_colored_tag(self):
        return self.__is_colored_tag
    def get_trainne_salary(self):
        return self.__trainee_salary
trainee_obj=Trainee(True,"Rose",20000)
print(trainee_obj.trainee_name)
print(trainee_obj.__trainee_salary)
print(trainee_obj.__is_colored_tag)