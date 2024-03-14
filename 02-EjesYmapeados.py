import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generamos un array con ahorros de prueba
ahorros = np.random.randint(100, size=6)

# Gráficamos sin etiquetas
# plt.plot(ahorros)

# MAPEAMOS LOS DATOS
# Definimos una lista con los meses para el eje horizontal
# meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']

# # Mapeamos un rango de índices para el eje horizontal
# # xticks para mapear el eje X e yticks para mapear el eje Y
# plt.plot(ahorros)
# # plt.xticks([0,1,2,3,4,5], meses) 
# plt.xticks(range(len(meses)), meses) # puede ser asi o como esta en la lista anterior


# y = np.random.randint(20, size=[6])
# plt.plot(y)

# x = ["A", "B", "C", "D", "E", "F"]
# plt.plot(x, y)

# GRAFICOS INVERTIDOS
# plt.plot(y, x)

# EJEMPLO
x = np.random.randint(20, size=[6])
y = np.random.randint(20, size=[6])

plt.plot(x, y)
plt.show()