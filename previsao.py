import os
import requests
import argparse

def get_forecast(cidade, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={cidade}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados para as {cidade}: {response.status_code}.")
        return None

def get_forecast_data(cidades, api_key):
    dados_previsao = []
    for cidade in cidades:
        previsao = get_forecast(cidade, api_key)
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
    return dados_previsao

def load_cities(caminho_arquivo):
    base_path = os.path.dirname(__file__)
    caminho_arquivo = os.path.join(base_path, 'cidades.txt')
    try:
        with open(caminho_arquivo, 'r') as file:
            cidades = [linha.strip() for linha in file.readlines() if linha.strip()]
        return cidades
    except FileNotFoundError:
        print(f"Esse arquivo {caminho_arquivo} não foi encontrado!!!")
        return []
