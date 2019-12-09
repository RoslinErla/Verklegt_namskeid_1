class Airplane():
    def __init__(self,Manufacturer = "", Type_ID = "" ,Plane_insignia = "",Model = "", status = ""): #, capacity=0, empty_weight=0, max_takeoff_weight=0, length=0, height=0, wingspan=0):
            self.__manufacturer = Manufacturer
            self.__type_ID = Type_ID
            self.__plane_insignia = Plane_insignia
            self.__model = Model
            self.__status = status
    
    def __str__(self):
        return "{:12} | {:15} | {:15} | {:6} | {:15}".format(self.__manufacturer, self.__type_ID, self.__plane_insignia, self.__model, self.__status)
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_typeID(self):
        return self.__type_ID
    
    def get_plane_insignia(self):
        return self.__plane_insignia

    def get_model(self):
        return self.__model