from model.AirplaneM import Airplane
from model.employeeM import Employee
from model.VoyageM import Voyage
from model.DestinationM import Destination


from logic.Airplane_LL import AirplaneLL
from logic.Employee_LL import EmployeeLL
from logic.Voyage_LL import VoyageLL
from logic.Destination_LL import DestinationLL

from UI.Main_UI import MainUI
from UI.Airplane_UI import AirplaneUI
from UI.Employee_UI import EmployeeUI
from UI.Voyage_UI import VoyageUI
from UI.Destination_UI import DestinationUI


from IO.airplaneIO import AirplaneIO
from IO.employeeIO import EmployeeIO
from IO.voyageIO import VoyageIO
from IO.destinationIO import DestinationIO


ui = MainUI()
ui.main_menu()
