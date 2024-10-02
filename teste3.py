import json

def calcular_faturamento(filename):
    
    with open(filename, 'r') as file:
        faturamento_dias = json.load(file)
    #verifica os dias em que o faturamento foi diferente de 0
    dias_com_faturamento = [dia['valor'] for dia in faturamento_dias if dia['valor'] > 0]

    if not dias_com_faturamento:
        print("Não há faturamento registrado no mês.")
        return

    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

    #verifica os dias em que o faturamento foi maior que a média
    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_faturamento)

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias acima da média: {dias_acima_da_media}")

calcular_faturamento('dados.json')
