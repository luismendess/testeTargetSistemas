# Define o faturamento mensal de cada Estado
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def calcula_percentual(faturamento):
    #faturamento total da distribuidora
    total_faturamento = sum(faturamento.values())
    
    print("Faturamento mensal por estado e percentual de representação:")
    # Calcula o percentual de cada estado e imprime
    for estado, valor in faturamento.items():
        percentual = (valor / total_faturamento) * 100
        print(f"{estado}: R${valor:.2f} - {percentual:.2f}%")

# Chama a função para calcular e imprimir os percentuais
calcula_percentual(faturamento_mensal)