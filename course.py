class Course:
    course_list=['Surveying','Manufacturing',"Programming"]
    fee_list=[3500,4200,2500]
    def __init__(self,course):
        self.__course=course
    def set_course(self,course):
        self.__course=course
    def get_course(self):
        return self.__course
    def identify_course_fee(self):
        for index in range(len(Course.course_list)):
            if Course.course_list[index]==self.__course:
                course_fee=Course.fee_list[index]
                return course_fee
        return -1
class SoftwareCourse(Course):
    software_course_list=["Machine learning","Web Design "]
    def __init__(self, software_course_name, course):
        super().__init__(course)
        self.__software_course_name = None
        self.software_course_name=software_course_name
        course_base_fee=0
        if self.__software_course_name in software_course_name:
            self.set_course("Programming")
