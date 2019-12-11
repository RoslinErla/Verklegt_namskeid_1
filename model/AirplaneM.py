class Airplane():
    def __init__(self,Manufacturer = "", Type_ID = "" ,Plane_insignia = "",Model = ""):
            self.__manufacturer = Manufacturer
            self.__type_ID = Type_ID
            self.__plane_insignia = Plane_insignia
            self.__model = Model

    
    def __str__(self):
        return "{:12} | {:15} | {:15} | {:6}".format(self.__manufacturer, self.__type_ID, self.__plane_insignia, self.__model)
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_typeID(self):
        return self.__type_ID
    
    def get_plane_insignia(self):
        return self.__plane_insignia

    def get_model(self):
        return self.__model