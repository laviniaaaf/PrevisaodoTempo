import argparse
from prevision import get_forecast_data, load_cities
from plot import get_dataframe, analysis_data, graph

def main():
    parser = argparse.ArgumentParser(description =  "Obter previsão do tempo para cidades.")
    parser.add_argument('--api_key', required = True, type = str, help = 'Chave da API para o WeatherAPI.')
    parser.add_argument('--arquivo', type = str, help = 'Nome do arquivo de texto contendo as cidades.')
    parser.add_argument('--cidades', nargs = '+', help = 'Lista de cidades para obter a previsão.')
    args = parser.parse_args()

    api_key = args.api_key

    if args.arquivo:
        cidades = load_cities(args.arquivo)
    elif args.cidades:
        cidades = args.cidades
    else:
        print("Forneça um nome de arquivo com o '--arquivo' ou uma lista de cidades com '--cidades'.")
        return

    dados_previsao = get_forecast_data(cidades, api_key)

    for dado in dados_previsao:
        print(dado)

    df_previsao = get_dataframe(dados_previsao)

    if dados_previsao:
        get_dataframe(dados_previsao)
        analysis_data(dados_previsao)
        graph(df_previsao)

if __name__ == "__main__":
    main()
