import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'mes': ['Jan','Fev','Mar','Abr','Mai','Jun'],
    'vendas': [150, 210, 180, 240, 300, 275],
    'custos': [90, 130, 110, 160, 200, 175],
    'lucro': [60, 80, 70, 80, 100, 100]
})

# gráfico de linha básico
df.plot(x='mes', y='vendas', kind='line')

# múltiplas colunas no mesmo gráfico
df.plot(x='mes', y=['vendas','custos','lucro'], kind='line')

# gráfico de barras verticais
df.plot(x='mes', y='vendas', kind='bar')

# histograma de distribuição
df['vendas'].plot(kind='hist', bins=5)

# gráfico de dispersão
df.plot(kind='scatter', x='custos', y='vendas')

df['mm3'] = df['vendas'].rolling(window=3).mean()
df.plot(x='mes', y=['vendas', 'mm3'], figsize=(10, 4), marker='o')
plt.show()