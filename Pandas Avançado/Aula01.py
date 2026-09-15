import pandas as pd

periodo1 = pd.date_range('2022-01', periods=24, freq='ME') # ME --> Final de cada mês
periodo2 = pd.date_range('2023-01', periods=24, freq='ME') # ME --> Final de cada mês

print(periodo1)
print()
print(periodo2)
print()

# Faz uma combinação e trás em ordem os dois períodos em comum
inter = periodo1.intersection(periodo2)
print(inter)