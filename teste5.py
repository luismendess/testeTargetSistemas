def inverter_string(palavra):
    # Inicializa uma nova string vazia
    string_invertida = ""
    
    # Itera sobre a string original em ordem reversa
    for i in range(len(palavra) - 1, -1, -1):
        string_invertida += palavra[i]
    #retorna a string invertida
    return string_invertida

# Entrada da string (pode ser alterada ou definida pelo usuário)
entrada = input("Informe uma string para inverter : ")

#salva a string invertida em resultado chamando a função
resultado = inverter_string(entrada)
#imprime a entrada e a string invertida
print(f"String original: {entrada}")
print(f"String invertida: {resultado}")