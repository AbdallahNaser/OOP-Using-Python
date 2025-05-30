import re
from .person import Person
class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.__id = id
        self.car = car
        self.__email = email
        self.__salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.__mood = "happy"
        elif hours > 8:
            self.__mood = "tired"
        elif hours < 8:
            self.__mood = "lazy"
        return self.__mood

    @property
    def Id(self):
        return self.__id

    @Id.setter
    def Id(self, uid):
        self.__id = uid

    @property
    def Salary(self):
        return self.__salary

    @Salary.setter
    def Salary(self, salary):
        if (salary >= 1000):
            self.__salary = salary
        else:
            print("this salary is too low it must be 1000 or more")

    @property
    def Email(self):
        return self.__email

    @Email.setter
    def Email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if re.match(pattern, email):
            self.__email = email
        else:
            print("Invalid email format")

    def drive(self):
        self.car.run(self.distanceToWork, self.car.velocity)

    def refuel(self, gasamount):
        self.car.fuelRate += gasamount

    def to_dict(self):
        return {
            "name": self.name,
            "salary": self.Salary,
            "mood": self.Mood,
            "healthRate": self.HealthRate,
            "id": self.Id,
            "email": self.Email,
            "distanceToWork": self.distanceToWork,
            "car": {
                "name": self.car.name,
                "fuelRate": self.car.fuelRate,
                "velocity": self.car.velocity
            }
        }

    def send_mail(self, to, subject, msg, receiver_name):
        try:
            with  open("message.txt", 'w') as msgFile:
                if msgFile.writable():
                    print(msgFile.writelines(f"""From : {self.__email} 
                                                        To: {to}
                                                        subject: 

                                                        Hi, {receiver_name}
                                                        {msg}
                                                        thanks
                                                        """))
        except FileNotFoundError:
            print('you can not send message')
