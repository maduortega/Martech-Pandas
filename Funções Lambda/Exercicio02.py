import pandas as pd

df = pd.DataFrame({
    'produto':['Arroz','Feijão','Azeite','Macarrão','Café','Biscoito','Queijo','Presunto'],
    'preco':[5.90, 8.50, 32.90, 4.20, 18.90, 3.50, 28.90, 22.50],
    'categoria':['grão','grão','óleo','massa','bebida','snack','laticínio','frios']
})

df['faixa'] = df['preco'].apply(lambda n:
'Barato' if n < 10
else 'Médio' if n >= 10 and n <= 25
else 'Premium' if n > 25 else 'Não classificado')

print(df)