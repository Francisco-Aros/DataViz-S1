#para instalar extensiones de pyhton, se debe hacer por terminal

import matplotlib.pyplot as plt
from numpy import size

plt.close()

days = [1,2,3,4,5,6,7]
temps = [18.4, 19.7, 12.3, 15.1, 17.8, 18.5, 20.4]
sizes = [18.4, 19.7, 12.3, 15.1, 17.8, 18.5, 20.4]

plt.scatter(x=days, y=temps, s=sizes)

plt.show()
