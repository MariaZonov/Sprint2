class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment

employee1 = EmployeeSalary.get_hours('Olga', None, 2, 'olga@email.com')

print(employee1.hours)
print(employee1.salary())

employee2 = EmployeeSalary.get_email('Anna', 35, 2, None)

print(employee2.email)
print(employee2.salary())