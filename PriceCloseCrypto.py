# Instalando bibliotecas necessárias.
# pip install yfinance

# Importando bibliotecas necessárias.
import yfinance as yf       # Para Importar base de dados.
import pandas as pd         # Para análise de dados.

# Lista com o nome das criptos.
criptos = ['BTC-USD', 'ETH-USD', 'ADA-USD', 'BNB-USD', 'DOT-USD', 'LINK-USD']

# Criar dataFrame e Importar preço de fechamento no período de 2021 até a data atual.
criptos_df = pd.DataFrame()
for cripto in criptos:
    criptos_df[cripto] = yf.download(cripto, start='2021-01-01')['Close']

# Renomear colunas.
criptos_df = criptos_df.rename(
    columns={'BTC-USD': 'BTC', 'ETH-USD': 'ETH', 'ADA-USD': 'ADA', 'BNB-USD': 'BNB', 'DOT-USD': 'DOT', 'LINK-USD': 'LINK'})

# Limpar elementos NULOS.
criptos_df.dropna()

# Exportar base de dados no formato CSV.
criptos_df.to_csv('PriceCloseCrypto.csv')

# Mostrar os dados importados.
print(criptos_df)
