import pandas as pd

df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Eva', 'Felipe', 'Gabi'],
    'idade': [23, 35, 28, 41, 30, 22, 38],
    'cidade': ['SP', 'RJ', 'SP', 'MG', 'RJ', 'SP', 'MG'],
    'salario': [3500, 7200, 4800, 9100, 5600, 3100, 8400],
    'departamento': ['TI', 'RH', 'TI', 'Financeiro', 'RH', 'TI', 'Financeiro']
})

print(df.loc[0:2, ['nome', 'cidade']])
print()
print(df.loc[df['cidade'].isin(['SP', 'MG'])])
print()

print(df.groupby('cidade')['salario'].mean())
print()
print(df.groupby('cidade')['salario'].agg(['mean', 'min', 'max']))
