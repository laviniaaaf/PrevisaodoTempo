import unittest
import pandas as pd

from plot import get_dataframe, analysis_data

class TestPlot(unittest.TestCase):
    def test_get_dataframe(self):
        dados = [
            {"Cidade": "São Paulo", "Temperatura (°C)": 25.0, "Umidade (%)": 60},
            {"Cidade": "Rio de Janeiro", "Temperatura (°C)": 28.0, "Umidade (%)": 65}
        ]
        df = get_dataframe(dados)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertIn("Cidade", df.columns)
    
    def test_exibir_analise_dados(self):
        dados = [
            {"Cidade": "São Paulo", "Temperatura (°C)": 25.0, "Umidade (%)": 60, "Pressão (hPa)": 1013, "Velocidade do Vento (km/h)": 10},
            {"Cidade": "Rio de Janeiro", "Temperatura (°C)": 28.0, "Umidade (%)": 65, "Pressão (hPa)": 1015, "Velocidade do Vento (km/h)": 12}
        ]
        df = get_dataframe(dados)
        try:
            analysis_data(dados)
            success = True
        except Exception as e:
            success = False
            print(f"Erro na função de análise: {e}")
        
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
