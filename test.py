from model.AirplaneM import Airplane
from logic.Airplane_LL import Airplane_LL

a = Airplane("plane_type", "type_ID", "plane_insignia", "model")
print(a)

b = Airplane_LL('inp')
b.validate_info()