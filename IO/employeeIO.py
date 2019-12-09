from model.employeeM import Employee
import csv

class EmployeeIO:
    EMPLOYEE_FILE = "./files/employee.csv"

    def __init__(self):
        self.__employee_list = list()
        self.__header ="Name, SSN, Address, Phone_number, User_name, Rank, Permit, Status" 
        self.__employee = Employee("","","","","","","","")

    def get_employee_list(self):
        return self.__employee_list
            

    def load_employee_from_file(self,sort_type):
        print(self.__header)

        with open(self.EMPLOYEE_FILE, "r", encoding="Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Status"],line["Permit"])
                self.__employee_list.append(employee)

        if sort_type == "alpha":
            sorted_list = self.sort_to_display(self.__employee_list, sort_type)
        
        elif sort_type == "status":
            sorted_list = self.sort_to_display(self.__employee_list, sort_type)
        
        self.__employee_list = sorted_list

    def __str__(self):
        strengur = ''
        for employee in self.__employee_list:
            strengur += employee.__str__() + '\n'
        return strengur

    def sort_to_display(self, a_list, sort_type):
        if sort_type == "alpha":
            a_list.sort(key = lambda x: x.get_name())
            return a_list

        elif sort_type =="status":
            a_list.sort(key = lambda x: x.get_status())
            return a_list

    def Add_employee_to_file(self, name, ssn, phone, user_name, rank, permits, status):
        with open(self.EMPLOYEE_FILE, "a", encoding="Latin-1", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name,ssn,phone, user_name, rank, permits, status])

    def delete_employee(self, ssn):
        employee_file = list()
        with open(self.EMPLOYEE_FILE, "r", encoding="Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                if line[0] != (self.__employee.get_ssn or []):
                    employee_file.append(line)

        with open(self.EMPLOYEE_FILE, "a", encoding="Latin-1", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            for lists in employee_file:
                writer.writerow(lists)



