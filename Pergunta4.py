# define o valor de faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

# calcula o valor total mensal
total = sum(faturamento.values())

# calcula o percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    percentuais[estado] = percentual

# exibe os resultados
for estado, percentual in percentuais.items():
    print('{}: {:.2f}%'.format(estado, percentual))
