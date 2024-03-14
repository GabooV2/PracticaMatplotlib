import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ahorros = np.random.randint(50,100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.ylim(0, 100)            # Configuramos el límite vertical
plt.xlim(1, 4)              # Configuramos el límite horizontal
plt.show()                  # Finalmente lo mostramos