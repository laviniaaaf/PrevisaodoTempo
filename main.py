import argparse
from previsao import obter_dados_previsao, carregar_cidades
from plot import criar_dataframe, exibir_analise_dados, graficos

def main():
    
    # Configuração dos  argumentos de linha de comando
    parser = argparse.ArgumentParser(description =  "Obter previsão do tempo para cidades.")
    parser.add_argument('--api_key', required = True, type = str, help = 'Chave da API para o WeatherAPI.')
    parser.add_argument('--arquivo', type = str, help = 'Nome do arquivo de texto contendo as cidades.')
    parser.add_argument('--cidades', nargs = '+', help = 'Lista de cidades para obter a previsão.')
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

    for dado in dados_previsao:
        print(dado)

    df_previsao = criar_dataframe(dados_previsao)

    if dados_previsao:
        criar_dataframe(dados_previsao)
        exibir_analise_dados(dados_previsao)
        graficos(df_previsao)

if __name__ == "__main__":
    main()
