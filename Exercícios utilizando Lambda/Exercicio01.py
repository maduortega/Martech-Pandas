def main():
    n = input('Digite os valores das transações: ')
    
    # Map, aplique a função int em n.split(' ') --> n.separar pelos espaços
    lista = map(float, n.split(' '))
    
    # Criamos uma função classificatória que fica guardada na variável verificar
    verificar = lambda v: ('Baixa' if v <= 100
    else 'Média' if v <= 1000
    else 'Alta' if v <= 5000 
    else 'Crítica')
    
    # Percorremos cada valor na lista, e para cada valor pedimos para verificar sua classificação
    # e imprimi-la. Ou seja, para cada valor ele imprime o valor e sua classificação
    for i in lista:
        print(f'{i} --> {verificar(i)}')

if __name__ == '__main__':
    main()