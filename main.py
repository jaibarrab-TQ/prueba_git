import pandas as pd

# Crear datos con duplicados
data = {
    'id': [1, 2, 3, 2, 4, 5, 3],
<<<<<<< HEAD
    'nombre': ['Ana', 'JuanZ', 'PedroX', 'Juan', 'Lucía', 'Carlos', 'Pedro']
=======
    'nombre': ['Ana', 'Juan', 'Pedro', 'Juan', 'Lucía', 'Carlos', 'Pedro']
>>>>>>> duplicados
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Eliminar duplicados basado en la columna 'id'
df_sin_duplicados = df.drop_duplicates(subset='id')

print(df_sin_duplicados)
print('con este codigo se eliminan los ultimos registros del df')