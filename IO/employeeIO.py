from model.employeeM import Employee
import csv


class employeeIO:
    EMPLOYEE_FILE = "./files/employee.csv"

    def __init__(self):
        pass

    def load_employee_from_file_alphabetically(self):
        pass

    def load_employee_from_file_by_status(self):
        pass

    def Add_employee_to_file(self,name, ssn, phone, user_name, rank, permits, status):
        with open(self.EMPLOYEE_FILE, "a", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name,ssn,phone, user_name, rank, permits, status])

