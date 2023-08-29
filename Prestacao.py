# Formatação
print()
print("************ CALCULAR PRESTAÇÕES ************")
print()

# Captura os Dados de Entrada
valorFinanciado = float (input("Digite o Valor Financiado: "))
valorEntrada = float (input("Digite o Valor de Entrada: "))
taxaJuros = float (input("Digite a Taxa de Juros: "))
numeroPrestacoes = int (input("Digite o Numero de Prestações: "))

# Faz o Calculo
valorCorrigido = valorFinanciado - valorEntrada
taxaJurosCorrigida = taxaJuros / 100
valorPrestacao = ((1 + taxaJurosCorrigida) ** numeroPrestacoes * taxaJurosCorrigida) / ((1 + taxaJurosCorrigida) ** numeroPrestacoes - 1) * valorFinanciado
valorFinal = valorPrestacao * numeroPrestacoes

# Printa na Tela
print()
print("************ RESULTADO ************")
print()
print("O Valor Financiado é: ", valorFinanciado)
print("O Valor de Entrada é: ", valorEntrada)
print("O Numero de Prestações é: ", numeroPrestacoes)
print("O Valor Final é: ", valorFinal)
print("O Valor das Prestaçoes são: ", valorPrestacao)
print()
print("************ PAULO HENRIQUE AZEVEDO DO NASCIMENTO ************")