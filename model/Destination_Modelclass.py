class Destination():
    def __init__(self, destination_id, destination_name):
        self.__destination_id = destination_id
        self.__destination_name = destination_name

    def __str__(self):
        pass

    def get_destinantion_id(self):
        return self.__destination_id

    def get_destinantion_name(self):
        return self.__destination_name