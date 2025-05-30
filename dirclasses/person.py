from abc import ABC, abstractmethod

class Person():
    moods=("happy", "tired", "lazy")
    def __init__(self,name,money,mood,healthRate):
        self.name=name
        self.money=money
        self.__mood=mood
        self.__healthRate=healthRate


    @property
    def HealthRate(self):
        return self.__healthRate
    @HealthRate.setter
    def HealthRate(self,healthrate):
        if(healthrate>=0 and healthrate<=100):
            self.__healthRate=healthrate
        else:
            print("health rate must be between 0 and 100")

    @property
    def Mood(self):
        return self.__mood

    @Mood.setter
    def Mood(self, mood_value):
        if mood_value in Person.moods:
            self.__mood = mood_value
        else:
            raise ValueError(f"Mood must be one of {Person.moods}")

    def sleep(self, hours):
        if hours == 7:
            self.__mood = "happy"
        elif hours < 7:
            self.__mood = "tired"
        elif hours > 7:
            self.__mood = "lazy"
        return self.__mood


    def eat(self,meals):
            if (meals == 3):
                self.__healthRate=100
            elif (meals == 2):
                self.__healthRate=75
            elif (meals == 1):
                self.__healthRate=50
    def buy(self,items):
        self.money-=(len(items)*10)
