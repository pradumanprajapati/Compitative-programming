class Employee:
    def __init__(self,salary,pf):
        self.__init__salary=salary
        self.pf=pf
    def calculate_total_salary(self,bonus):
        bonus=self.__init__salary*5/100
        return 3*(bonus+self.__init__salary)
    def get_salary(self):
        return self.__init__salary
class ContractEmployee(Employee):
    contract_period=9
    def __init__(self, salary, pf):
        super() .__init__(salary, pf)
    def calculate_total_salary(self):
        salary=super().calculate_total_salary(1000)






