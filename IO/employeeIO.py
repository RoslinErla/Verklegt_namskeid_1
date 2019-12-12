from model.employeeM import Employee
import csv
import string
from datetime import datetime

class EmployeeIO:
    EMPLOYEE_FILE = "./files/employee.csv"
    VOYAGE_FILE = "./files/voyage.csv"
    CONSTANT_LIST = ["SSN", "NAME", "ADDRESS", "PHONE_NUMBER", "USER_NAME", "RANK", "PERMIT", "STATUS" ]

    def __init__(self):
        self.__employee_list = list()
        self.__employee_set = set()
        self.__ssn_set = set()
        self.__user_name_set = set()
        self.__header = "{:35} | {:11} | {:30} | {:12} | {:15} | {:25} | {:15}" \
        .format("Name", "SSN", "Address", "Phone_number", "User_name", "Rank", "Permit")
        self.__employee = Employee()

    def make_ssn_set(self):
        with open(self.EMPLOYEE_FILE, "r",encoding= "Latin-1") as the_file:
            reader = csv.reader(the_file)
            for line in reader:
                self.__ssn_set.add(line[0])
    
    def make_user_name_set(self):
        with open(self.EMPLOYEE_FILE, "r", encoding= "Latin-1") as the_file:
            reader = csv.reader(the_file)
            for line in reader:
                self.__ssn_set.add(line[0])

    def get_set(self):
        self.make_ssn_set()
        return self.__ssn_set

    def get_user_name_set(self):
        self.make_user_name_set()
        return self.__user_name_set


    def load_employee_from_file(self,sort_type):
        print(self.__header)

        with open(self.EMPLOYEE_FILE, "r", encoding="Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"])
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
        self.__employee_list = list()
        return strengur

    def display_pilots(self,sort_type):
        print(self.__header)

        with open(self.EMPLOYEE_FILE, "r", encoding="Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                if line["Rank"].lower() == "captain" or line["Rank"] == "co-pilot":
                    employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"])
                    self.__employee_list.append(employee)
            if sort_type == "alpha":
                sorted_list = self.sort_to_display(self.__employee_list,"alpha")
            elif sort_type == "permit":
                sorted_list = self.sort_to_display(self.__employee_list, "type_id")
            self.__employee_list = sorted_list

    def display_by_licence(self,licence):
        print(self.__header)
        with open(self.EMPLOYEE_FILE, "r", encoding= "Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                if line["Permit"].lower() == licence.lower():
                    employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"])
                    self.__employee_list.append(employee)
            sorted_list = self.sort_to_display(self.__employee_list,"alpha")
            self.__employee_list = sorted_list

    def display_flight_attendants(self):
        print(self.__header)

        with open(self.EMPLOYEE_FILE, "r", encoding="Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                if line["Rank"] == "flight attendant" or line["Rank"] == "flight service manager":
                    employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"])
                    self.__employee_list.append(employee)
            sorted_list = self.sort_to_display(self.__employee_list,"alpha")
            self.__employee_list = sorted_list

    def display_one_employee(self,ssn):
        self.__employee_list = list()
        print(self.__header)

        with open(self.EMPLOYEE_FILE, "r", encoding="Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                if line["SSN"] == ssn:
                    employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"],line["Status"])
                    self.__employee_list.append(employee)

    def sort_to_display(self, a_list, sort_type):
        if sort_type == "alpha":
            a_list.sort(key = lambda x: x.get_name())
            return a_list

        elif sort_type =="status":
            a_list = sorted(a_list, key = lambda x: x.get_name())
            a_list.sort(key = lambda x: x.get_status())
            return a_list

        elif sort_type == "type_id":
            a_list = sorted(a_list, key = lambda x: x.get_name())
            a_list.sort(key = lambda x: x.get_permit())
            return a_list

    def Add_employee_to_file(self, name, ssn, address, phone, user_name, rank, permits):
        with open(self.EMPLOYEE_FILE, "a", encoding="Latin-1", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name,ssn, address, phone, user_name, rank, permits])

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

    def change_employee(self, ssn, change, new):
        change_index = self.CONSTANT_LIST.index(change.upper())

        with open(self.EMPLOYEE_FILE) as thefile:
            reader = csv.reader(thefile.readlines())

        with open(self.EMPLOYEE_FILE, "w", encoding= "Latin-1", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for line in reader:
                if line[0] == ssn:
                    line[change_index] = new
                    writer.writerow(line)
                    break
                else:
                    writer.writerow(line)
            writer.writerows(reader)

    def display_status(self,date):
        year,month,day = date.split("/")
        date = "{}-{}-{}".format(year,month,day)

        with open(self.EMPLOYEE_FILE) as csvfile:
            employee_reader = csv.DictReader(csvfile)
            for line in employee_reader:
                a = False
                with open(self.VOYAGE_FILE) as the_file:
                    for elements in csv.DictReader(the_file):
                        if (elements["departure time out"].split("T")[0] == date or elements["departure time to RVK"].split("T")[0] == date) and (elements["captain/pilot"] == line["User_name"] or elements["co-pilot"] == line["User_name"]):
                            employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"],"at work")
                            try:
                                bla = [emp for emp in self.__employee_list if emp.get_user_name() == line["User_name"]]
                                if len(bla) > 0:
                                    print('bla: ', bla)
                                    index = self.__employee_list.index(bla[0])
                                    print(index)
                                    if index > -1:
                                        self.__employee_list[index] = employee
                                else:
                                    self.__employee_list.append(employee)
                            except ValueError:
                                self.__employee_list.append(employee)
                            a = True
                        if not a:
                            a = True
                            employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"],"not at work")
                            self.__employee_list.append(employee)
        
        sorted_list = self.sort_to_display(self.__employee_list,"status")
        self.__employee_list = sorted_list

    def display_status1(self,date):
        year,month,day = date.split("/")
        date = "{}-{}-{}".format(year,month,day)
        
        with open(self.VOYAGE_FILE) as csvfile:
            voyage_reader = csv.DictReader(csvfile)
            for elements in voyage_reader:
                with open(self.EMPLOYEE_FILE) as thefile:
                    print('cap', elements["captain/pilot"])
                    for line in csv.DictReader(thefile):
                        a = False
                        print('username', line["User_name"])
                        if (elements["departure time out"].split("T")[0] == date or elements["departure time to RVK"].split("T")[0] == date) and (elements["captain/pilot"] == line["User_name"] or elements["co-pilot"] == line["User_name"]):
                            employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"],"at work")
                            self.__employee_list.append(employee)
                            a = True
                        if not a:
                            employee = Employee(line["Name"],line["SSN"],line["Address"],line["Phone_number"], line["User_name"],line["Rank"],line["Permit"],"not at work")

        sorted_list = self.sort_to_display(self.__employee_list,"status")
        self.__employee_list = sorted_list






