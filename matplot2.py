# Carga los precios de las consolas desde el archivo .csv y 
# crea un gráfico que muestre el precio promedio de cada una; 
# otro gráfico que indique durante cuántos días los PC son más caros que las consolas; 
# y un desglose que muestre, entre las consolas, durante cuántos días cada una fue la más económica.

import pandas as pd
import matplotlib.pyplot as plt

# crea un gráfico que muestre el precio promedio de cada una; 
df_contsolak = pd.read_csv("precios_consolas.csv")

xbox_bataz = 0
ps5_bataz = 0
switch_bataz = 0
pc_bataz = 0

for fila in df_contsolak.values:
    xbox_bataz += fila[1]
    ps5_bataz += fila[2]
    switch_bataz += fila[3]
    pc_bataz += fila[4]

xbox_bataz = xbox_bataz / 365
ps5_bataz = ps5_bataz / 365
switch_bataz = switch_bataz / 365
pc_bataz = pc_bataz / 365

y = [xbox_bataz, ps5_bataz, switch_bataz, pc_bataz]
x = ["Xbox", "PS5", "Switch", "PC"]
colores = ['tomato', '#33FF57', "#33FFF5", "#FF33EE"]

plt.bar(x, y, color=colores)
plt.title("Contsolen prezioen batazbestekoa")
plt.show()


# otro gráfico que indique durante cuántos días los PC son más caros que las consolas; 
egun_pc_gareztiago = 0
egun_pc_merkeago = 0


for fila in df_contsolak.values:
    if fila[4] > fila[1] and fila[4] > fila[2] and fila[4] > fila[3]:
        egun_pc_gareztiago += 1
    else:
        egun_pc_merkeago += 1

x2 = ["egun_pc_gareztiago", "egun_pc_merkeago"]
y2 = [egun_pc_gareztiago, egun_pc_merkeago]

barras = plt.bar(x2, y2, color=colores)
plt.bar_label(barras, padding=-20)
plt.title("Zenbat egun pc gareztiago edo merkeago contsolak baino.")
plt.show() 


# y un desglose que muestre, entre las consolas, durante cuántos días cada una fue la más económica.
xbox_merkea = 0
ps5_merkea = 0
switch_merkea = 0

for fila in df_contsolak.values:
    if fila[1] < fila[2] and fila[1] < fila[3]:
        xbox_merkea += 1
    elif fila[2] < fila[1] and fila[2] < fila[3]:
        ps5_merkea += 1
    elif fila[3] < fila[1] and fila[3] < fila[2]:
        switch_merkea +=1

x3 = ["zenbat egun xbox", "zenbat egun ps5", "zenbat egun switch"]
y3 = [xbox_merkea, ps5_merkea, switch_merkea]

colores2 = ["#04CC29", "#0035C5", "#EB0303"]

barras = plt.bar(x3, y3, color=colores2)
plt.bar_label(barras, padding=-20)
plt.title("Zenbat egun kontsola bakoitza kontsola merkeagoa izan da.")
plt.show() 


