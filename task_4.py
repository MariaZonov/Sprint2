class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = self.get_hours(hours, rest_days)
        self.rest_days = rest_days
        self.email = self.get_email(email, name)

    @staticmethod
    def get_hours(hours, rest_days):
        if hours is None:
            return (7 - rest_days) * 8
        return hours

    @classmethod
    def get_email(cls, email, name):
        if email is None:
            return f"{name}@email.com"
        return email

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment

employee = EmployeeSalary('Olga', 35, 2, None)

print(employee.hours)
print(employee.email)
print(employee.salary())