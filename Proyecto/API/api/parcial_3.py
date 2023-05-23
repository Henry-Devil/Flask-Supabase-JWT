

import pandas as pd
import numpy as np
from matplotlib import pyplot as pyplot

original_df = pd.read_excel("api/bank-additional.xlsx")
print(original_df)
f_absoluta_sv = pd.value_counts(original_df['job'])
f_absoluta_sv

f_relativa_sv = 100 * original_df['job'].value_counts() / len(original_df['job'])
f_relativa_sv

grafica_1_sv = original_df['job'].value_counts().plot(kind='bar', title ='job')
print(grafica_1_sv)

grafico_2_sv = original_df['job'].value_counts().plot(kind = 'pie', autopct = '%.2f' , figsize = (6,6), title = 'job').legend(loc='upper left')
grafico_2_sv

f_absoluta_sv = pd.value_counts(original_df['housing'])
print(f_absoluta_sv)

f_relativa_sv = 100 * original_df['housing'].value_counts() / len(original_df['housing'])
f_relativa_sv

grafica_1_sv = original_df['housing'].value_counts().plot(kind='bar', title ='Prestamo de Vivienda')
grafica_1_sv

grafico_2_sv = original_df['housing'].value_counts().plot(kind = 'pie', autopct = '%.2f' , figsize = (6,6), title = 'Prestamo de Vivienda').legend(loc='upper left')
grafico_2_sv

f_absoluta_sv = pd.value_counts(original_df['loan'])
f_absoluta_sv

f_relativa_sv = 100 * original_df['loan'].value_counts() / len(original_df['loan'])
f_relativa_sv

grafica_1_sv = original_df['loan'].value_counts()#.plot(kind='bar', title ='Prestamo Personal')
print(grafica_1_sv)

grafico_2_sv = original_df['loan'].value_counts().plot(kind = 'pie', autopct = '%.2f' , figsize = (6,6), title = 'Prestamo Personal').legend(loc='upper left')
grafico_2_sv

"""---

VARIABLES CUANTITATIVAS

Se calcula media, mediana, moda, minimo, maximo, histograma y caja de bigotes de la Columna **campaign**
"""

media_ev = original_df['campaign'].mean()
media_ev

mediana_ev = original_df['campaign'].median()
mediana_ev

moda_ev = original_df['campaign'].mode()
moda_ev

maximo_ev = max(original_df['campaign'])
maximo_ev

min_ev = min(original_df['campaign'])
min_ev

grafica_1_sv = original_df['campaign'].value_counts()#.plot(kind='bar', title ='campaign')
print(grafica_1_sv)

bigotes_mv = pyplot.boxplot(x = original_df['campaign'])
pyplot.xlabel("campaign")
pyplot.ylabel("Cantidad")
bigotes_mv

"""limpieza 1"""

Q1 = original_df['campaign'].quantile(0.25)
print("Primer Cuartil", Q1)

Q3 = original_df['campaign'].quantile(0.75)
print("Tercer Cuartil", Q3)

IQR = Q3 - Q1
print("Rango Intercuartil", IQR)

Mediana = original_df['campaign'].median()
print("Mediana", Mediana)

Valor_Miniom = original_df['campaign'].min()
print("Valor Minimo", Valor_Miniom)

Valor_Maximo = original_df['campaign'].max()
print("Valor Máximo", Valor_Maximo)

BI_Calculado = (Q1 - 1.5 * IQR)
print("BI_CALCULADO \n", BI_Calculado)

BS_Calculado = (Q3 + 1.5 * IQR)
print("BS_CALCULADO \n", BS_Calculado)

ubicacion_outliers = ((original_df['campaign'] < BI_Calculado) | (original_df['campaign'] > BS_Calculado))
print("\n Ubicacion de Outliers \n", ubicacion_outliers)

outliers = original_df[ubicacion_outliers]
print("\n Lista de Outliers \n", outliers)

Outliers_Ordenados = outliers.sort_values("campaign")
Outliers_Ordenados

Ubicacion_sin_out = ((original_df['campaign'] >= BI_Calculado) & (original_df['campaign'] <= BS_Calculado))
sin_outliers = original_df[Ubicacion_sin_out]
sin_outliers

bigotes_mv = pyplot.boxplot(x = sin_outliers['campaign'])
pyplot.xlabel("campaign")
pyplot.ylabel("Cantidad")
bigotes_mv

"""---

Se calcula media, mediana, moda, minimo, maximo, histograma y caja de bigotes de la Columna **pdays**
"""

media_ev = original_df['pdays'].mean()
media_ev

mediana_ev = original_df['pdays'].median()
mediana_ev

moda_ev = original_df['pdays'].mode()
moda_ev

maximo_ev = max(original_df['pdays'])
maximo_ev

min_ev = min(original_df['pdays'])
min_ev

grafica_1_sv = original_df['pdays'].value_counts().plot(kind='bar', title ='pdays')
grafica_1_sv

bigotes_mv = pyplot.boxplot(x = original_df['pdays'])
pyplot.xlabel("pdays")
pyplot.ylabel("Cantidad")
bigotes_mv

"""SE REALIZA PRIMERA LIMPIEZA PARA LA COLUMNA: **pdays**

"""

Q1 = original_df['pdays'].quantile(0.25)
print("Primer Cuartil", Q1)

Q3 = original_df['pdays'].quantile(0.75)
print("Tercer Cuartil", Q3)

IQR = Q3 - Q1
print("Rango Intercuartil", IQR)

Mediana = original_df['pdays'].median()
print("Mediana", Mediana)

Valor_Miniom = original_df['pdays'].min()
print("Valor Minimo", Valor_Miniom)

Valor_Maximo = original_df['pdays'].max()
print("Valor Máximo", Valor_Maximo)

BI_Calculado = (Q1 - 1.5 * IQR)
print("BI_CALCULADO \n", BI_Calculado)

BS_Calculado = (Q3 + 1.5 * IQR)
print("BS_CALCULADO \n", BS_Calculado)

ubicacion_outliers = ((original_df['pdays'] < BI_Calculado) | (original_df['pdays'] > BS_Calculado))
print("\n Ubicacion de Outliers \n", ubicacion_outliers)

outliers = original_df[ubicacion_outliers]
print("\n Lista de Outliers \n", outliers)

Outliers_Ordenados = outliers.sort_values("pdays")
Outliers_Ordenados

Ubicacion_sin_out = ((original_df['pdays'] >= BI_Calculado) & (original_df['pdays'] <= BS_Calculado))
sin_outliers = original_df[Ubicacion_sin_out]
sin_outliers

bigotes_mv = pyplot.boxplot(x = sin_outliers['pdays'])
pyplot.xlabel("pdays")
pyplot.ylabel("Cantidad")
bigotes_mv

"""---

Se calcula media, mediana, moda, minimo, maximo, histograma y caja de bigotes de la Columna **cons.price.idx**
"""

media_ev = original_df['cons.price.idx'].mean()
media_ev

mediana_ev = original_df['cons.price.idx'].median()
mediana_ev

moda_ev = original_df['cons.price.idx'].mode()
moda_ev

maximo_ev = max(original_df['cons.price.idx'])
maximo_ev

min_ev = min(original_df['cons.price.idx'])
min_ev

grafica_1_sv = original_df['cons.price.idx'].value_counts()#.plot(kind='bar', title ='Price')
print(grafica_1_sv)

bigotes_mv = pyplot.boxplot(x = original_df['cons.price.idx'])
pyplot.xlabel("cons.price.idx")
pyplot.ylabel("Cantidad")
bigotes_mv

"""SE REALIZA PRIMERA LIMPIEZA PARA LA COLUMNA: **cons.price.idx**

"""

Q1 = original_df['cons.price.idx'].quantile(0.25)
print("Primer Cuartil", Q1)

Q3 = original_df['cons.price.idx'].quantile(0.75)
print("Tercer Cuartil", Q3)

IQR = Q3 - Q1
print("Rango Intercuartil", IQR)

Mediana = original_df['cons.price.idx'].median()
print("Mediana", Mediana)

Valor_Miniom = original_df['cons.price.idx'].min()
print("Valor Minimo", Valor_Miniom)

Valor_Maximo = original_df['cons.price.idx'].max()
print("Valor Máximo", Valor_Maximo)

BI_Calculado = (Q1 - 1.5 * IQR)
print("BI_CALCULADO \n", BI_Calculado)

BS_Calculado = (Q3 + 1.5 * IQR)
print("BS_CALCULADO \n", BS_Calculado)

ubicacion_outliers = ((original_df['cons.price.idx'] < BI_Calculado) | (original_df['cons.price.idx'] > BS_Calculado))
print("\n Ubicacion de Outliers \n", ubicacion_outliers)

outliers = original_df[ubicacion_outliers]
print("\n Lista de Outliers \n", outliers)

Outliers_Ordenados = outliers.sort_values("cons.price.idx")
Outliers_Ordenados

Ubicacion_sin_out = ((original_df['cons.price.idx'] >= BI_Calculado) & (original_df['cons.price.idx'] <= BS_Calculado))
sin_outliers = original_df[Ubicacion_sin_out]
sin_outliers

bigotes_mv = pyplot.boxplot(x = sin_outliers['cons.price.idx'])
pyplot.xlabel("Price")
pyplot.ylabel("Cantidad")
bigotes_mv