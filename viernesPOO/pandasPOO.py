importar pandas como pd

clase MiDataFrame(pd.DataFrame):
       def __init__(uno mismo, argumentos):
         super().__init__(argumentos)
         imprimir(argumentos)

       def prom_columnas(self):
       devolver self.mean()

datos = {
    'A': [24.0, 33.2, 30.2, 29.4, 29.3],
    'B': [34.0, 30.2, 31.2, 29.4, 29.3]
}

df = MiDataFrame(datos)
imprimir(df.prom_columnas())