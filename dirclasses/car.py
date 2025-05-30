
class Car:
    def __init__(self, name,fuelRate,velocity):
        self.name=name
        self.__fuelRate=fuelRate
        self.__velocity=velocity

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self.__velocity = value
        else:
            raise ValueError("Velocity must be between 0 and 200")

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self.__fuelRate = value
        else:
            raise ValueError("Fuel rate must be between 0 and 100")



    def run(self, distance, velocity):
        self.velocity = velocity
        remaining_distance = distance
        travelled = 0

        while remaining_distance > 0 and self.fuelRate > 0:
            step = min(10, remaining_distance)
            self.fuelRate -= self.fuelRate * 0.1  # decrease by 10%
            travelled += step
            remaining_distance -= step

        if remaining_distance == 0:
            print(f"Arrived at destination. Fuel left: {self.fuelRate:.2f}%")
            self.stop(0)
        else:
            print(f"Car stopped early after {travelled} km. Fuel depleted.")
            self.stop(remaining_distance)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance == 0:
            print("Arrived at destination.")
        else:
            print(f"Stopped with {remaining_distance:.2f} km remaining due to no fuel.")
