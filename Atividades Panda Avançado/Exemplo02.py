import pandas as pd
import numpy as np

# Cria um df vazio
df = pd.DataFrame()

# Cria colunas novas nesse df
df['data'] = pd.date_range('2024-01', periods=365,
freq='D')             # Gera no intervalo de 50 a 200, 365 valores diferentes
df['vendas'] = np.random.randint(50,200,365)

# Criar coluna de trimestre a partir de 'data'
df['trimestre'] = df['data'].dt.to_period('Q')

resultado = df.groupby('trimestre')['vendas'].sum()
print(resultado)