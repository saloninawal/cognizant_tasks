# advanced_payroll_system.py
class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        if self.hours_worked > 40:
            overtime_hours = self.hours_worked - 40
            overtime_pay = overtime_hours * self.hourly_rate * 1.5
            regular_pay = 40 * self.hourly_rate
            total_pay = regular_pay + overtime_pay
        else:
            total_pay = self.hours_worked * self.hourly_rate
        return total_pay

class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self):
        total_pay = super().calculate_pay()
        return total_pay + self.bonus

# Instantiate objects for Employee and Manager
employee = Employee("John Doe", 45, 20)
manager = Manager("Jane Smith", 50, 30, 500)

# Calculate and print the total pay for both
print(f"{employee.name} total pay: ${employee.calculate_pay():.2f}")
print(f"{manager.name} total pay: ${manager.calculate_pay():.2f}")
