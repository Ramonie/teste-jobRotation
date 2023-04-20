import xml.etree.ElementTree as ET

# parseia o xml e armazena em uma lista de tuplas (dia, valor)
tree = ET.parse('dados.xml')
root = tree.getroot()
faturamento = [(int(row.find('dia').text), float(row.find('valor').text)) for row in root]

# calcula o menor e o maior faturamento
menor_faturamento = min(faturamento, key=lambda x: x[1])
maior_faturamento = max(faturamento, key=lambda x: x[1])

# calcula a média mensal, ignorando os dias sem faturamento
faturamento_total = sum([f[1] for f in faturamento if f[1] != 0])
dias_com_faturamento = len([f for f in faturamento if f[1] != 0])
media_mensal = faturamento_total / dias_com_faturamento

# conta o número de dias com faturamento acima da média
dias_acima_da_media = len([f for f in faturamento if f[1] > media_mensal])

# exibe os resultados
print(f'Menor faturamento: dia {menor_faturamento[0]}, valor {menor_faturamento[1]}')
print(f'Maior faturamento: dia {maior_faturamento[0]}, valor {maior_faturamento[1]}')
print(f'Número de dias com faturamento acima da média: {dias_acima_da_media}')
