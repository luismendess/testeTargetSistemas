def fibonacci(valor_inserido):
    valor_0, valor_1 = 0, 1
    while valor_0 < valor_inserido:
        valor_0, valor_1 = valor_1, valor_0 + valor_1
    return valor_0 == valor_inserido

try:
    numero_usuario = int(input("Informe um número: "))
    if fibonacci(numero_usuario):
        print("O número informado pertence à sequência de Fibonacci.")
    else:
        print("O número informado não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")