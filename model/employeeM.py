
class Employee():

    def __init__(self,name,ssn,address,phone_number,user_name,rank, status = "At work", permits = ""):
        self.__name = name
        self.__ssn= ssn
        self.__phone_number = phone_number
        self.__user_name = user_name
        self.__rank = rank
        self.__permit = permits
        self.__status = status

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.__name, self.__ssn, self.__phone_number,self.__user_name,self.__rank, self.__permit,self.__status)


    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__ssn

    def get_phoneNumber(self):
        return self.__phone_number

    def get_user_name(self):
        return self.__user_name
    
    def get_rank(self):
        return self.__rank

    def get_permit(self):
        return self.__permit

    def get_status(self):
        return self.__status


