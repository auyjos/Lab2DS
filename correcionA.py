import pandas as pd

# Cargar el archivo original
file_path = 'consumo.csv'
df = pd.read_csv(file_path, encoding='latin1')

# Limpiar los nombres de las columnas
df.columns = df.columns.str.replace('\n', ' ')

# Reemplazar comas por puntos en los valores numéricos
columnas_numericas = df.columns[1:]
df[columnas_numericas] = df[columnas_numericas].replace({',': ''}, regex=True)
df[columnas_numericas] = df[columnas_numericas].replace(
    {'\.': '.'}, regex=True).astype(float)

# Guardar el DataFrame normalizado en un nuevo archivo CSV
df.to_csv('consumo_normalizado.csv', index=False)
