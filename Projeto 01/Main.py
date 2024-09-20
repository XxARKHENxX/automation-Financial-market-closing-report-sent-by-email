import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
from datetime import datetime
from pathlib import Path

from src import tickerMap
import SendMail
import win32com.client as win32

# Tickers das ações: Obtenha os tickers do Yahoo Finance
tickers = ["^BVSP", "^GSPC", "BRL=X", "ABEV3.SA", "PBR"] 

# Baixar dados do mercado para os últimos 6 meses
dados_mercado = yf.download(tickers, period="6mo")

#Filtrar dados apenas ajuste de fechamento
dados_mercado = dados_mercado["Adj Close"]

#Remover dados faltantes (Tratar dados)
dados_mercado = dados_mercado.dropna()

#Atualizar nomes das colunas (fique atento ao numero de colunas para renomear)
# dados_mercado.columns = tickers_Name
print(dados_mercado)

#Definir estilo de grafico
plt.style.use("cyberpunk")

#Criar Grafico
# plt.plot(dados_mercado["IBOVESPA"])
# plt.title("IBOVESPA")

#Exibir grafico
# plt.show()


for ticker in tickers:

    plt.plot(dados_mercado[ticker])
    name = tickerMap.FindName(ticker)
    if name is None:
        print(f"Nome não encontrado para o ticker '{ticker}'")
        continue
    plt.title(name)
    #Exibir grafico - apenas dps de salvar pq se nao dps salva imagem vazia
    # plt.show()

    # date_time = datetime.now()
    # Name_graf = date_time.strftime('%d-%m-%Y_%H-%M-%S') + "_" + name.lower() #salvar varios sem substituir
    Name_graf = name.lower()

    path = Path(f"graficos/{name}")
    if not path.exists():
        path.mkdir(parents=True)

    plt.savefig(path / f"{Name_graf}.png")
    # plt.clf()  # Limpar a figura para o próximo gráfico

retornos_Diarios = dados_mercado.pct_change() #(periods = 5)

# print(retornos_Diarios.head(10))
print(f"Retornos Diarios: \n{retornos_Diarios}")

#é necessario criar um dicionario novamente? pra evitar tantas variaveis
retorno_Ambev =     retornos_Diarios["ABEV3.SA"].iloc[-1]
retorno_Dolar =     retornos_Diarios["BRL=X"].iloc[-1]
retorno_Petrobras = retornos_Diarios["PBR"].iloc[-1]
retorno_Ibovespa =  retornos_Diarios["^BVSP"].iloc[-1]
retorno_SeP500 =    retornos_Diarios["^GSPC"].iloc[-1]

retorno_Ambev =     str(round(retorno_Ambev * 100, 2)) + "%"
retorno_Dolar =     str(round(retorno_Dolar * 100, 2)) + "%"
retorno_Petrobras = str(round(retorno_Petrobras * 100, 2)) + "%"
retorno_Ibovespa =  str(round(retorno_Ibovespa * 100, 2)) + "%"
retorno_SeP500 =    str(round(retorno_SeP500 * 100, 2)) + "%"



print("Porcentagem de fechamento:\n")

print(f"Ambev:     {retorno_Ambev}")
print(f"Dolar:     {retorno_Dolar}")
print(f"Petrobras: {retorno_Petrobras}")
print(f"Ibovespa:  {retorno_Ibovespa}")
print(f"S&P500:    {retorno_SeP500}")



SendMail.SendMail(retorno_Ibovespa, retorno_Dolar, retorno_SeP500)