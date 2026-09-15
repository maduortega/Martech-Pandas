import pandas as pd

df = pd.DataFrame({
    'produto':['Arroz','Feijão','Azeite','Macarrão','Café','Biscoito','Queijo','Presunto'],
    'preco':[5.90, 8.50, 32.90, 4.20, 18.90, 3.50, 28.90, 22.50],
    'categoria':['grão','grão','óleo','massa','bebida','snack','laticínio','frios']
})

df['ordenado'] = sorted(df['produto'], key=lambda w: len(w))

# Printa em ordem crescente essa coluna do df
print(sorted(df['produto'], key=lambda w: len(w)))
print()

# Agora, com esta coluna adicionada no df, vamos printar do mesmo modo
print(df)