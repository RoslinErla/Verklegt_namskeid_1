
class Employee():

    def __init__(self,name = "",ssn = "",address = "",phone_number = "",user_name = "",rank = "",permits = "",status = ""):
        self.__name = name
        self.__ssn= ssn
        self.__address = address
        self.__phone_number = phone_number
        self.__user_name = user_name
        self.__rank = rank
        self.__permit = permits
        self.__status = status

    def __str__(self):
        return "{:35} | {}-{} | {:30} | {}-{:8} | {:15} | {:25} | {:15}".format(self.__name, self.__ssn[:6], self.__ssn[6:], self.__address, self.__phone_number[:3],self.__phone_number[4:],self.__user_name, self.__rank, self.__permit)


    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def get_ssn(self):
        return self.__ssn

    def get_permit(self):
        return self.__permit


