import pandas as pd

df = pd.DataFrame({
    'ticker': ['PETR4','VALE3','ITUB4','BBDC4','MGLU3','PETR4','VALE3','ITUB4','BBDC4','MGLU3'],
    'setor': ['Petróleo','Mineração','Banco','Banco','Varejo','Petróleo','Mineração','Banco','Banco','Varejo'],
    'preco': [36.50, 68.20, 27.10, 15.40, 4.80, 37.80, 70.50, 26.50, 14.90, 5.20],
    'variacao': [1.2, -0.5, 2.1, -1.3, 3.5, -0.8, 1.1, 0.4, -2.2, 4.1],
    'volume': [52000, 38000, 91000, 67000, 23000, 48000, 41000, 87000, 72000, 19000],
    'sessao': ['manhã','manhã','manhã','manhã','manhã','tarde','tarde','tarde','tarde','tarde']
})

# Tarefa 1 | Selecione apenas as ações do setor banco de ticker, preço e variação
print(df.loc[df['setor'] == 'Banco', ['ticker', 'preco', 'variacao']])
print()

# Tarefa 2 | Filtre ações com variações positivas > 0, e volume acima de 50k
print(df.loc[(df['variacao'] > 0) & (df['volume'] > 50000)])
print()

# Tarefa 3 | Crie uma coluna 'sinal' com valor 'compra' se variacao > 1.5, e 'aguardar' nos demais casos
df.loc[df['variacao'] > 1.5, 'sinal'] = 'compra'
df.loc[df['variacao'] <= 1.5, 'sinal'] == 'aguardar'
print(df)
print()

# Tarefa 4 | Exiba as 3 primeiras e as 2 últimas linhas do DataFrame usando iloc.
print(df.iloc[0:3, -2:])
print()

# Tarefa 5 | Calcule o preço médio e o volume total por setor. Use agg() com 'mean' e 'sum'.
print(df.groupby('setor')['preco']['volume'].agg(['mean', 'sum']))