#Crie a coluna 'label' que una produto e faixa no formato 'Produto — Faixa'
# (ex: 'Azeite — Premium'). Use apply(lambda) c
import pandas as pd

df = pd.DataFrame({
    'produto':['Arroz','Feijão','Azeite','Macarrão','Café','Biscoito','Queijo','Presunto'],
    'preco':[5.90, 8.50, 32.90, 4.20, 18.90, 3.50, 28.90, 22.50],
    'categoria':['grão','grão','óleo','massa','bebida','snack','laticínio','frios']
})

df['label'] = df.apply(lambda n:
    # Axis=1 para que eu trabalhe em cima da LINHA, não da coluna.
    f'{n['produto']} - {n['categoria']}', axis=1)

print(df)