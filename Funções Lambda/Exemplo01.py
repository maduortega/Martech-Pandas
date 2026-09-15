import pandas as pd

df = pd.DataFrame({
    'nome' : ['Ana','Bruno','Carla','Diego'],
    'salario': [1200,950,1500,800]
})

# Aplicar reajuste de 10% em toda a coluna
# Criamos uma nova coluna que recebe o salário com um reajuste de 10%
df['novo_sal'] = df['salario'].apply(lambda x: x * 1.1)
print(df)