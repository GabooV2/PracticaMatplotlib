import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ahorros = [52, 104, 32, 65, 15, 76]

ahorros2 = np.random.randint(100, size=[6])

df = pd.DataFrame(ahorros, index=['Enero','Febrero','Marzo','Abril','Mayo','Junio'])

# EL EJE HORIZONTAL (X) SON LOS INDICES DEL ARRAY O DATAFRAME (POR DEFECTO SERIA 0,1,2,3,4 COMO POR EJEMPLO EN LA LISTA AHORROS)
# plt.plot(df)
df.plot()

plt.show()







