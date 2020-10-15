import numpy as np
from lab_ex3 import g
import lab_ex3
import math
a=np.pi/3
h=100
#np.tan(30)
B_deg=30
B_rad=np.radians(B_deg)

c=g*h*((np.tan(B_rad))**2)
o=2*((np.cos(a)**2))
q=1-(np.tan(B_rad)*(np.tan(a)))
w=(c/(o*q))**(1/2)

print(w)