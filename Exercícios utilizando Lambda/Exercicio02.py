def main():
    produtos = [
        ("Mouse", 80, 120),
        ("Notebook", 4500, 12),
        ("Teclado", 150, 85),
        ("Monitor", 1200, 30),
    ]
        
    # Ele faz o calculo para ordenar apenas, ele não vai apresentar o calculo feito na impressão
    ordenado = sorted(produtos, key=lambda v: v[1] * v[2])
    
    print(ordenado)

if __name__ == '__main__':
    main()