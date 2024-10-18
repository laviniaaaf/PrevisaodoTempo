import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def criar_dataframe(dados_previsao):
    return pd.DataFrame(dados_previsao)

def exibir_analise_dados(dados_previsao):
    df_previsao = pd.DataFrame(dados_previsao)
    
    temperatura_media = df_previsao['Temperatura (°C)'].mean()
    print(f"\nA temperatura média das cidades é de: {temperatura_media:.2f}°C.\n")
   
    print("\nResumo dos dados:\n")
    print(df_previsao.describe())

    umidade_media = df_previsao['Umidade (%)'].mean()
    cidades_alta_umidade = df_previsao[df_previsao['Umidade (%)'] > umidade_media]
    print("\nCidades com umidade acima da média:\n")
    print(cidades_alta_umidade[['Cidade', 'Umidade (%)']])

    maior_pressao = df_previsao[df_previsao['Pressão (hPa)'] == df_previsao['Pressão (hPa)'].max()]
    print("\nCidade com maior pressão:")
    print(maior_pressao[['Cidade', 'Pressão (hPa)']])

    maior_vento = df_previsao[df_previsao['Velocidade do Vento (km/h)'] == df_previsao['Velocidade do Vento (km/h)'].max()]
    print("\nCidade com maior velocidade do vento:")
    print(maior_vento[['Cidade', 'Velocidade do Vento (km/h)']])
 
    df_previsao.plot(
        kind='barh', 
        x='Cidade', 
        y='Temperatura (°C)', 
        color='skyblue', 
        legend=False, 
        title='Temperatura agora nas Cidades'
    )
    plt.xlabel('Temperatura (°C)')
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

def graficos(df_previsao):
    plt.figure(figsize=(14, 8))

    plt.subplot(2, 2, 1)
    sns.barplot(x = 'Cidade', y = 'Temperatura (°C)', data = df_previsao, palette = 'RdYlBu')
    plt.title('Temperatura Atual por Cidade (°C)')
    plt.xticks(rotation=45)

    plt.subplot(2, 2, 2)
    sns.barplot(x = 'Cidade', y = 'Umidade (%)', data = df_previsao, palette = 'Blues')
    plt.title('Umidade Atual (%): ')
    plt.xticks(rotation=45)

    plt.subplot(2, 2, 3)
    sns.scatterplot(x = 'Cidade', y = 'Velocidade do Vento (km/h)', data = df_previsao, color = 'orange', s = 100)
    plt.title('Velocidade do Vento por (km/h): ')
    plt.xticks(rotation=45)

    plt.subplot(2, 2, 4)
    sns.barplot(x = 'Cidade', y='Pressão (hPa)', data = df_previsao, palette = 'Greens')
    plt.title('Pressão Atmosférica por Cidade (hPa): ')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
