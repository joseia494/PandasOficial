# Importamos la libreria d Pandas, fundamental para analisis de datos
import pandas as pd
# Define la ruta del archivo csv que contiene los datos
# Si el archivo esta en el mismo directorio, basta con poner el nombre del achivo
path = 'Sesion_2/dragon_ball_z.csv'
# Nombrar a la base de datos
dragon_data = pd.read_csv(path, encoding='utf-8')
print(type(dragon_data))
print(dragon_data.head())
