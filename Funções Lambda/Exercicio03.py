import pandas as pd

df = pd.DataFrame({
    'produto':['Arroz','Feijão','Azeite','Macarrão','Café','Biscoito','Queijo','Presunto'],
    'preco':[5.90, 8.50, 32.90, 4.20, 18.90, 3.50, 28.90, 22.50],
    'categoria':['grão','grão','óleo','massa','bebida','snack','laticínio','frios']
})

df['preco_promo'] = df['preco'].apply(lambda n:
round(n * 0.85, 2) if n > 25 # Premium
else round(n * 0.95, 2) if n <= 25 # Demais
else n)

'''
Outro modo:
df['preco_promo'] = df.apply(lambda n:
n['preco'] * 0.85 if n['faixa'] == 'Premium'
else n['preco'] * 0.95, axis=1)

Obs: Necessário ter a coluna faixa no df para fazer deste modo
'''


print(df)