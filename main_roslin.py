from model.VoyageM import Voyage
from IO.voyageIO import VoyageIO


a = VoyageIO()
a.load_voyage_from_file()
print(a)

inp = input()