def main():
    leituras = [
    ("S1", 35),
    ("S2", 82),
    ("S3", 47),
    ("S4", 91),
    ("S5", 65),
    ]
    
    # O filter já contém um if, não precisamos colocar um if dentro
    # Verificamos se o índice 1 da tupla é >= a 70 (crítico), e aplicamos isso em leituras
    critico = list(filter(lambda x: x[1] >= 70, leituras))
    
    # Não colocamos print pois ele retorna algo, então só colocamos o f''
    # Pegamos os dados do crítico para avaliar o estado
    avisar = map(lambda x: f'Sensor {x[0]} em estado crítico', critico)
    
    for m in avisar:
        print(m)

if __name__ == '__main__':
    main()