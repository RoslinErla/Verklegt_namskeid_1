from model.employeeM import Employee
import csv


class employeeIO:
    EMPLOYEE_FILE = "./files/employee.csv"

    def __init__(self):
        self.__employee_list = list()

    def load_employee_from_file(self,sort_type):
        with open(self.EMPLOYEE_FILE, "r") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                employee = Employee(line["Name"],line["SSN"],line["Phone_number"],["User_name"],["Rank"],["Permits"],["Status"])
                self.__employee_list.append(employee)
        if sort_type == "alpha":
            sorted_list = self.sort_to_display(self.__employee_list, sort_type)
        
        elif sort_type == "status":
            sorted_list = self.sort_to_display(self.__employee_list, sort_type)
        
        sorted_list = self.__str__(sorted_list)        
        return sorted_list

    def __str__(self,the_list):
        return_str = ""
        for lists in the_list:
            return_str += lists
        return return_str

    def sort_to_display(self, a_list, sort_type):
        if sort_type == "alpha":
            return sorted(a_list)

        elif sort_type =="status":
            return a_list.sort(key = lambda x: x[7])

    def Add_employee_to_file(self, name, ssn, phone, user_name, rank, permits, status):
        with open(self.EMPLOYEE_FILE, "a", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name,ssn,phone, user_name, rank, permits, status])

