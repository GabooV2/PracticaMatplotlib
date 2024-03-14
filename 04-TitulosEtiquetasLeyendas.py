import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

# plt.plot(ahorros)
# plt.plot(np.random.randint(100, size=[6]))
# plt.plot(np.random.randint(100, size=[6]))
# plt.plot(np.random.randint(100, size=[6]))
# plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
# plt.xlim(1, 4)                            # Configuramos el límite horizontal
# plt.title("Ahorros del primer semestre")  # Configuramos el título
# plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
# plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
# # plt.legend(["Evolución"], loc=0)          # Mostramos la leyenda
# plt.legend(["Pedro", "Marta", "Ana"])


# Por defecto se usa la opción 0 para detectar automáticamente el mejor sitio donde poner la leyenda:
# 0: best
# 1: upper right
# 2: upper left
# 3: lower left
# 4: lower right
# 5: right
# 6: center left
# 7: center right
# 8: lower center
# 9: upper center
# 10: center

df = pd.DataFrame(
    data=[
        np.random.randint(100, size=[6]), 
        np.random.randint(100, size=[6]), 
        np.random.randint(100, size=[6])],
    index=['Pedro','Marta','Ana'], 
    columns=['Enero','Febrero','Marzo','Abril','Mayo','Junio'])

# print(f"{df}\n")

# plt.plot(df)
# plt.plot(df.T)
# plt.xlim(1, 4)
# plt.title("Ahorros del primer semestre")
# plt.xlabel("Meses")
# plt.ylabel("Cantidad en €")
# plt.legend(['Pedro','Marta','Ana'])
# plt.show()

# EJEMPLO
# Tablas de multiplicar del 1 al 10
for t in range(1, 11):
    plt.plot(
        range(1, 11),                   # Eje X
        [t * n for n in range(1, 11)],  # Eje Y
        label=f"Tabla del {t}")         # Leyenda para cada serie
    
plt.title('Tablas')
plt.xlabel('Número')
plt.ylabel('Resultado')
plt.legend()
plt.show()

