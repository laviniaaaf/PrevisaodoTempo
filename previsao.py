import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def obter_previsao(cidade, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={cidade}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados para {cidade}: {response.status_code}")
        return None

api_key = " " #coloque sua chave
cidades = ["Rio de Janeiro", "Salvador", "Sao Paulo", "Londres", "Paris", "Toronto", "Vancouver"]  
dados_previsao = []

for cidade in cidades:
    previsao = obter_previsao(cidade, api_key)
    if previsao:
        dados_previsao.append({
            "Cidade": cidade,
            "Temperatura (°C)": previsao['current']['temp_c'],
            "Umidade (%)": previsao['current']['humidity'],
            "Descrição": previsao['current']['condition']['text'],
            "Pressão (hPa)": previsao['current']['pressure_mb'],
            "Data": previsao['location']['localtime'],
            "Sensação Térmica (°C)": previsao['current']['feelslike_c'],  
            "Velocidade do Vento (km/h)": previsao['current']['wind_kph'],  
        })

# Criar o DataFrame com os dados
df_previsao = pd.DataFrame(dados_previsao)
print(df_previsao)

# Análise dos dados
temperatura_media = df_previsao['Temperatura (°C)'].mean()
print(f"\nTemperatura média nas cidades: {temperatura_media:.2f} °C")

umidade_media = df_previsao['Umidade (%)'].mean()
cidades_alta_umidade = df_previsao[df_previsao['Umidade (%)'] > umidade_media]
print("\nCidades com umidade acima da média:")
print(cidades_alta_umidade[['Cidade', 'Umidade (%)']])

maior_pressao = df_previsao[df_previsao['Pressão (hPa)'] == df_previsao['Pressão (hPa)'].max()]
print("\nCidade com maior pressão:")
print(maior_pressao[['Cidade', 'Pressão (hPa)']])

maior_vento = df_previsao[df_previsao['Velocidade do Vento (km/h)'] == df_previsao['Velocidade do Vento (km/h)'].max()]
print("\nCidade com maior velocidade do vento:")
print(maior_vento[['Cidade', 'Velocidade do Vento (km/h)']])

# Visualização dos dados
plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
sns.barplot(x='Cidade', y='Temperatura (°C)', data=df_previsao, palette='coolwarm')
plt.title('Temperatura Atual por Cidade (°C)')
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
sns.barplot(x='Cidade', y='Umidade (%)', data=df_previsao, palette='Blues')
plt.title('Umidade Atual por Cidade (%)')
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
sns.scatterplot(x='Cidade', y='Velocidade do Vento (km/h)', data=df_previsao,  color='orange', s=100)
plt.title('Velocidade do Vento por Cidade (km/h)')
plt.xticks(rotation=45)

plt.subplot(2, 2, 4)
sns.barplot(x='Cidade', y='Pressão (hPa)', data=df_previsao, palette='Greens')
plt.title('Pressão Atmosférica por Cidade (hPa)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
