class Airplane():
    def __init__(self, manufacturer, type_ID, plane_insignia, model): #, capacity=0, empty_weight=0, max_takeoff_weight=0, length=0, height=0, wingspan=0):
            self.__manufacturer = manufacturer
            self.__type_ID = type_ID
            self.__plane_insignia = plane_insignia
            self.__model = model
    
    def __str__(self):
        return "{},{},{},{}".format(self.__manufacturer, self.__type_ID, self.__plane_insignia, self.__model)
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_typeID(self):
        return self.__type_ID
    
    def get_plane_insignia(self):
        return self.__plane_insignia

    def get_model(self):
        return self.__model