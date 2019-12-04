
class Employee():

    def __init__(self,name,ssn,address,phone_number,email,rank, permits = "", status = "At work"):
        self.__name = name
        self.__ssn= ssn
        self.__address = address
        self.__phone_number = phone_number
        self.__email = email
        self.__rank = rank
        self.__permit = permits
        self.__status = status


    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.__name, self.__id, self.__address, self.__phone_number,self.__email,self.__rank, self.__permits,self.__status)

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__id

    def get_address(self):
        return self.__address

    def get_phoneNumber(self):
        return self.__phone_number

    def get_email(self):
        return self.__email
    
    def get_rank(self):
        return self.__rank

    def get_permits(self):
        return self.__permit

    def get_status(self):
        return self.__status


