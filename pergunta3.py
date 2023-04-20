import xml.etree.ElementTree as ET

# carrega o arquivo XML
tree = ET.parse('faturamento_diario.xml')
root = tree.getroot()

# inicializa as variáveis
soma = 0
maior_valor = float('-inf')
menor_valor = float('inf')
dias_com_faturamento = 0
dias_sem_faturamento = 0
# percorre os elementos <dia>
for dia in root.findall('dia'):
    # verifica se o dia tem faturamento
    if dia.text is not None:
        # converte o valor para float e soma à variável soma
        valor = float(dia.text)
        soma += valor

        # verifica se o valor é maior ou menor que os valores já encontrados
        if valor > maior_valor:
            maior_valor = valor
        if valor < menor_valor:
            menor_valor = valor

        # incrementa o contador de dias com faturamento
        dias_com_faturamento += 1
    else:
        # incrementa o contador de dias sem faturamento
        dias_sem_faturamento += 1

# calcula a média mensal
media_mensal = soma / dias_com_faturamento

# exibe os resultados
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Dias sem faturamento: {dias_sem_faturamento}")
print(f"Número de dias com faturamento acima da média: {sum(float(dia.text) > media_mensal for dia in root.findall('dia') if dia.text is not None)}")
