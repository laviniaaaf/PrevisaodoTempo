import os
import requests
import argparse

def obter_previsao(cidade, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={cidade}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados para as {cidade}: {response.status_code}.")
        return None

def obter_dados_previsao(cidades, api_key):
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
    return dados_previsao

def carregar_cidades(caminho_arquivo):
    base_path = os.path.dirname(__file__)
    caminho_arquivo = os.path.join(base_path, 'cidades.txt')
    try:
        with open(caminho_arquivo, 'r') as file:
            cidades = [linha.strip() for linha in file.readlines() if linha.strip()]
        return cidades
    except FileNotFoundError:
        print(f"Esse arquivo {caminho_arquivo} não foi encontrado!!!")
        return []

def main():
    parser = argparse.ArgumentParser(description = "Obter a previsão do tempo para cidades.")
    parser.add_argument('--api_key', required = True, type = str, 
                        help = 'Chave da API para a conexão com  o WeatherAPI.')
    parser.add_argument('--arquivo', type = str, 
                        help = 'Arquivo de texto contendo as cidades.')
    parser.add_argument('--cidades', nargs = '+', 
                        help = 'Lista das cidades para obter a previsão.')
    args = parser.parse_args()

    api_key = args.api_key

    if args.arquivo:
        cidades = carregar_cidades(args.arquivo)
    elif args.cidades:
        cidades = args.cidades
    else:
        print("Forneça um nome de arquivo com o '--arquivo' ou uma lista de cidades com '--cidades'.")
        return

    dados_previsao = obter_dados_previsao(cidades, api_key)
    print(dados_previsao)

if __name__ == "__main__":
    main()
