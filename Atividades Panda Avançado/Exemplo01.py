import pandas as pd

dates = pd.date_range('2024-01', periods=12, freq='ME')
vendas = pd.Series([120,135,110,150,160,145,
170,155,165,180,175,190], index=dates)

print(vendas)
print()

# Converter DatetimeIndex → PeriodIndex mensal
vendas.index = vendas.index.to_period('M') # Transforma só no mês (print)
# Adendo, se houver várias datas em Jan, ele faria um Sum pra apresentar esse mês em to_period

print(vendas.index[:3])
print(vendas)
