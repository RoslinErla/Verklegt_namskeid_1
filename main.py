# from model.AirplaneM import Airplane
# from model.VoyageM import Voyage
# from model.employeeM import Employee

# from logic.Airplane_LL import AirplaneLL
# from logic.Voyage_LL import VoyageLL
# from logic.Employee_LL import EmployeeLL

from UI.header import Frame
frame = Frame()
print(frame) 
from logic.Voyage_LL import VoyageLL
from model.VoyageM import Voyage
from UI.Voyage_UI import VoyageUI

#a = VoyageUI()
#a.voyage_menu()

from model.DestinationM import Destination
from logic.Destination_LL import DestinationLL

from UI.Main_UI import MainUI 

a = MainUI()
a.main_menu()