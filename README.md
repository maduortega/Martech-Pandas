# Martech Pandas

Este repositório reúne exercícios, exemplos e atividades de estudo em **Python**, com foco em manipulação e análise de dados utilizando **Pandas**.

O material aborda desde operações essenciais com `DataFrame` até recursos um pouco mais avançados, como agrupamentos, filtros condicionais, criação de colunas, funções `lambda`, séries temporais, índices de data e visualização de dados com `matplotlib`.

## Conteúdos Abordados

- Criação e manipulação de `DataFrames`
- Seleção de dados com `loc` e `iloc`
- Filtros condicionais
- Agrupamentos com `groupby`
- Agregações com `agg`
- Criação de colunas calculadas
- Uso de funções `lambda`
- Aplicação de funções com `apply`
- Ordenação de dados
- Uso de `map`, `filter` e `sorted`
- Trabalhos com datas usando `date_range`, `DatetimeIndex` e `PeriodIndex`
- Consolidação de dados com `concat`
- Visualizações com gráficos de linha, barras, histograma e dispersão
- Cálculo de média móvel

## Projetos e Exercícios em Destaque

| Arquivo | Tema | Principais práticas |
| --- | --- | --- |
| [`Pandas/Atividade01.py`](Pandas/Atividade01.py) | Análise de ações por setor, preço, variação, volume e sessão. | Filtros com `loc`, criação de coluna de sinal, seleção com `iloc` e agrupamentos. |
| [`Pandas/Exemplo02.py`](Pandas/Exemplo02.py) | Análise de vendas, custos e lucro ao longo dos meses. | Gráficos com `matplotlib`, múltiplas séries, histograma, dispersão e média móvel. |
| [`Funções Lambda/Exercicio02.py`](<Funções Lambda/Exercicio02.py>) | Classificação de produtos por faixa de preço. | `apply(lambda)`, condicionais encadeadas e criação de coluna categórica. |
| [`Funções Lambda/Exercicio03.py`](<Funções Lambda/Exercicio03.py>) | Cálculo de preço promocional. | Regras condicionais, arredondamento e transformação de valores numéricos. |
| [`Atividades Panda Avançado/Exericicio01.py`](<Atividades Panda Avançado/Exericicio01.py>) | Consolidação de vendas entre bases de SP e RJ. | `concat`, conversão de datas, definição de índice temporal e `PeriodIndex`. |

## Estrutura do Repositório

```text
.
├── Atividades Panda Avançado/
│   ├── Exemplo01.py
│   ├── Exemplo02.py
│   └── Exericicio01.py
├── Exercícios utilizando Lambda/
│   ├── Exercicio01.py
│   ├── Exercicio02.py
│   └── Exercicio03.py
├── Funções Lambda/
│   ├── Exemplo01.py
│   ├── Exercicio01.py
│   ├── Exercicio02.py
│   ├── Exercicio03.py
│   └── Exercicio04.py
├── Pandas Avançado/
│   └── Aula01.py
├── Pandas/
│   ├── Atividade01.py
│   ├── Exemplo01.py
│   └── Exemplo02.py
└── LICENSE
```

## Descrição das Pastas

### Pandas

Contém exemplos e atividades introdutórias de análise de dados com Pandas.

Principais temas:

- Criação de `DataFrames`
- Seleção de linhas e colunas
- Filtros por condição
- Agrupamentos por categoria
- Cálculo de estatísticas por grupo
- Visualização de dados com `matplotlib`
- Média móvel com `rolling`

### Pandas Avançado

Reúne exemplos voltados ao uso de datas e períodos em Pandas.

Principais temas:

- Criação de sequências de datas com `pd.date_range`
- Frequência mensal com `freq='ME'`
- Comparação entre períodos
- Interseção entre índices temporais

### Atividades Panda Avançado

Contém exercícios práticos com séries temporais e consolidação de bases.

Principais temas:

- Conversão de datas com `pd.to_datetime`
- Transformação de `DatetimeIndex` em `PeriodIndex`
- Agrupamento de vendas por trimestre
- Concatenação de bases com `pd.concat`
- Organização de dados por índice temporal

### Funções Lambda

Reúne exemplos de aplicação de funções anônimas em estruturas de dados e `DataFrames`.

Principais temas:

- Criação de colunas com `apply(lambda)`
- Reajuste de valores numéricos
- Classificação de preços
- Cálculo de descontos
- Construção de labels a partir de colunas existentes
- Ordenação personalizada com `lambda`

### Exercícios utilizando Lambda

Contém exercícios de lógica com funções `lambda`, listas, tuplas e funções nativas do Python.

Principais temas:

- Classificação de transações por valor
- Ordenação de produtos por valor total
- Filtragem de leituras críticas de sensores
- Uso de `map`
- Uso de `filter`
- Uso de `sorted` com chave personalizada

## Tecnologias Utilizadas

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Funções lambda**
- **Manipulação de dados**
- **Análise exploratória**
- **Séries temporais**

## Como Executar os Arquivos

Para executar os scripts, é necessário ter o Python instalado. Também é preciso instalar as bibliotecas usadas nos exemplos:

```bash
pip install pandas numpy matplotlib
```

Depois, acesse a pasta do arquivo desejado pelo terminal e execute:

```bash
python nome_do_arquivo.py
```

Exemplo:

```bash
python Exemplo01.py
```

Alguns scripts exibem resultados diretamente no terminal. Outros, como os exemplos com `matplotlib`, podem abrir janelas com gráficos.

## Observações

Os dados utilizados nos exercícios são criados diretamente dentro dos próprios arquivos `.py`, por meio de listas, dicionários e `DataFrames`. Por isso, não é necessário baixar bases externas para reproduzir os exemplos atuais.

Há um arquivo com o nome `Exericicio01.py` dentro da pasta `Atividades Panda Avançado`. O nome foi mantido na documentação como aparece no repositório.

## Objetivo do Repositório

Este repositório tem como objetivo organizar os estudos de **Pandas aplicado à análise de dados**, registrando práticas de seleção, transformação, agregação, visualização e tratamento de informações em Python.

## Autoria

Desenvolvido como parte dos estudos em Python, Pandas e análise de dados.
