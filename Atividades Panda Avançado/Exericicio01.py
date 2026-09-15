import pandas as pd ; import numpy as np

df_sp = pd.DataFrame({'data': pd.date_range('2023-01',periods=18,freq='ME'),
'vendas': [150,160,140,np.nan,180,170,190,np.nan,200,210,np.nan,220,230,215,240,235,260,250]})

df_rj = pd.DataFrame({'data': pd.date_range('2023-07',periods=18,freq='ME'),
'vendas': [90,95,85,100,105,98,110,115,108,120,125,118,130,128,135,140,138,145]})

df_cli = pd.DataFrame({'id':[1,2,3,4], 'nome':['Ana','Bruno','Carla','Diego'],
'regiao':['SP','RJ','SP','RJ']})

df_ped = pd.DataFrame({'id':[1,2,1,3,4], 'valor':[500,800,300,600,450],
'data':['2024-01','2024-01','2024-02','2024-02','2024-03']})

df_novo = pd.concat([df_sp, df_rj],
    axis=0, # 0=linhas - linhas padrão | 1=colunas - Df Linha uma do lado da outra, Complicado
    ignore_index=True)

df_novo['data'] = pd.to_datetime(df_novo['data'], format='%d/%m/%Y')

# Definir a data como índice (permite gerar trimestre, gráfico, semestre)
df_novo = df_novo.set_index('data')

# Converte o índice para PeriodIndex Mensal
df_novo.index = df_novo.index.to_period('M')

print(df_novo)