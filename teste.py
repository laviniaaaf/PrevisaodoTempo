import pandas as pd
import numpy as py
import re
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "air_quality.csv")

df = pd.read_csv(csv_path)

nulos = df.isnull().sum()
print("Antes da remoção de nulos:\n", nulos)

df_sem_nulos = df.dropna()
#print(df_sem_nulos)

nulos_após_remoção = df_sem_nulos.isnull().sum()
print("\nDepois da remoção de nulos:\n", nulos_após_remoção)

# Extraia a data usando expressões regulares (regex) da coluna “Date”, alocando as saídas em uma coluna chamada “data_formatada”. Respeite o formato dd/mm/aaaa.
def extrair_data(data):
    padrao = r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})'
    resultado = re.search(padrao, data)
    if resultado:
        dia, mes, ano = resultado.groups()
        if len(ano) == 2:
            ano = '20' + ano
        return f"{int(dia):02}/{int(mes):02}/{ano}"
    return None  

df['data_formatada'] = df['Date'].apply(extrair_data)
print("\nCom a data formatada: \n", df[['Date', 'data_formatada']])

# Extraia a hora usando expressões regulares (regex) da coluna “Date”, alocando as saídas em uma coluna chamada “hora_formatada”. Respeite o formato hh:mm:ss.
def extrair_hora(data):
    padrao = r'(\d{2}):(\d{2})'
    resultado = re.search(padrao, data)
    if resultado:
        hora, minuto = resultado.groups()
        return f"{hora}:{minuto}:00"
    return None  

df['hora_formatada'] = df['Date'].apply(extrair_hora)
print("\nCom a hora formatada: \n",df[['Date', 'hora_formatada']])

# Realize uma análise exploratória básica dos dados, fornecendo as principais informações das colunas presentes neste CSV.
print("Dataframe: \n", df_sem_nulos)

print("\nEstatísticas descritivas: \n")
print(df_sem_nulos.describe(include='all'))  

print("\nTipos de dados das colunas:\n")
print(df_sem_nulos.dtypes)

print("\nDistribuição de valores únicos por coluna: \n")
for coluna in df_sem_nulos.columns:
    print(f"\nColuna: {coluna}")
    print(df_sem_nulos[coluna].value_counts())


# Vizualização : boxplots para cada coluna numérica no DataFrame para visualizar a presença de outliers.
num_cols = df_sem_nulos.select_dtypes(include=['float64', 
                                                'int64']).columns

for col in num_cols:
    plt.figure(figsize = (10, 6))
    sns.boxplot(y = df_sem_nulos[col])
    plt.title(f'Boxplot de {col}')
    plt.show()

# IQR para identificar outliers
Q1 = df_sem_nulos[num_cols].quantile(0.25)
Q3 = df_sem_nulos[num_cols].quantile(0.75)
IQR = Q3 - Q1

outliers_iqr = ((df_sem_nulos[num_cols] < (Q1 - 1.5 * IQR)) | (df_sem_nulos[num_cols] > (Q3 + 1.5 * IQR))).any(axis=1)
print(f"\n Número de outliers identificados pelo IQR: {sum(outliers_iqr)}")

# Análise de Correlação

## A correlação mede a relação entre duas variáveis, indicando a força e a direção da relação e a  matriz de correlação é uma tabela que mostra os coeficientes de correlação entre todas as combinações de variáveis numéricas em um dataframe
## Porque fazer essa análise? a análise de correlação ajuda a identificar quais variáveis estão relacionadas e como elas se influenciam, umas com as outras. Os coeficientes próximos de +1 ou -1 indicam uma forte correlação positiva ou negativa, 
# enquanto coeficientes próximos de 0 indicam pouca ou nenhuma correlação.

print("Colunas numéricas:", num_cols)
correlation_matrix = df_sem_nulos[num_cols].corr()  
print("\nMatriz de correlação:")
print(correlation_matrix)

plt.figure(figsize=(10, 
                    8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Heatmap da Matriz de Correlação')
plt.show()
