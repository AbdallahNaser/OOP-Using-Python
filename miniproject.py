from abc import ABC, abstractmethod
import re
import json
from dirclasses.person import Person
from dirclasses.emp import Employee
from dirclasses.person import Person
from dirclasses.office import Office
from dirclasses.car import Car




cars = [
    Car("fiat 128", 50, 100),
    Car("BMW", 80, 90),
    Car("Honda", 70, 80),
    Car("Kia", 90, 95),
    Car("Ford", 60, 85),
    Car("Mazda", 100, 100),
    Car("Tesla", 100, 120),
]

employees = [
    Employee("Samy", 1000, "happy", 100, 1, cars[0], "Samy@gmail.com", 3000, 20),
    Employee("nayera", 1200, "tired", 90, 2, cars[1], "nayera@yahoo.com", 3200, 18),
    Employee("Mona", 800, "lazy", 80, 3, cars[2], "mona@outlook.com", 3100, 15),
    Employee("Ahmed", 950, "happy", 85, 4, cars[3], "ahmed@gmail.com", 3300, 10),
    Employee("Omar", 2000, "tired", 60, 5, cars[4], "omar@gmail.com", 3400, 25),
    Employee("Nada", 1800, "lazy", 70, 6, cars[5], "nada@yahoo.com", 3500, 12),
    Employee("Youssef", 1500, "happy", 90, 7, cars[6], "youssef@live.com", 3000, 30),
]

office = Office("ITI")
for emp in employees:
    office.hire(emp)

print("--- Employees in Office ---")
for emp in office.get_all_employees():
    print(f"{emp.name}: Salary = {emp.Salary}, Mood = {emp.Mood}, Health = {emp.HealthRate}")


# Check lateness (simulate moving at 7:00 AM)
print("--- Checking Lateness ---")
for emp in employees:
    office.check_lateness(emp.Id, moveHour=7)


office.check_lateness(1,9)
office.check_lateness(1,9)
office.check_lateness(1,9)
#after check the late

print("--- Employees in Office ---")
for emp in office.get_all_employees():
    print(f"{emp.name}: Salary = {emp.Salary}, Mood = {emp.Mood}, Health = {emp.HealthRate}")




print("--- Simulating Work, Eating, and Driving ---")
employees[0].work(9)
employees[1].eat(2)
employees[2].sleep(6)
employees[3].drive()
employees[4].refuel(20)
employees[5].send_mail("hr@company.com", "Leave Request", "I'd like to take a day off.", "HR Manager")

print("--- Final Employee Info ---")
for emp in office.get_all_employees():
    print(f"{emp.name} - Mood: {emp.Mood}, Health: {emp.HealthRate}, Salary: {emp.Salary}, Fuel: {emp.car.fuelRate:.2f}")




#check car
test_car = Car("TestCar", 50, 100)
test_car.run(100, 100)

print(f"Fuel before: {cars[0].fuelRate}")
employees[0].refuel(30)
print(f"Fuel after: {cars[0].fuelRate}")

# Fire someEmployee
office.fire(7)
print("Employees after firing ID 7:")
for emp in office.get_all_employees():
    print(emp.name)


#test send email
employees[0].send_mail("manager@company.com", "ay 7aga", "This is a test email", "Manager")
with open("message.txt", 'r') as f:
    print(f.read())

#get details of one employee
emp = employees[0]
print(f"Employee Name: {emp.name}")
print(f"Employee Email: {emp.Email}")
print(f"Employee Mood: {emp.Mood}")
print(f"Employee Salary: {emp.Salary}")
print(f"Employee Car Name: {emp.car.name}")
print(f"Office Name: {office.name}")
print(f"Number of Employees: {len(office.get_all_employees())}")



with open("office_data.json", "w") as json_file:
    json.dump(office.to_dict(), json_file, indent=4)







