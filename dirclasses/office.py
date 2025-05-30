
class Office:
    employeesNum = 0
    def __init__(self,name,employees=None):
        self.name=name
        self.employees=employees if employees else []
    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.Id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        employee = self.get_employee(empId)
        if employee:
            self.employees.remove(employee)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.Salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.Salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    def to_dict(self):
        return {
            "name": self.name,
            "employees": [emp.to_dict() for emp in self.employees],
            "employeesNum": Office.employeesNum
        }

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
