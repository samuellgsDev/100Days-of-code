# Criar uma calculador de gorjetas
# Dia 2
ContaTotal = float(input("Qual foi o valor total da conta ? "))
Gorjeta = float(input("Quantos por cento você quer dar de gorjeta ? "))
DividirConta = int(input("Com quantas pessoas voce irá dividir a conta ? "))
ValorGorjeta = ((Gorjeta / 100)*ContaTotal)
NovaContaTotal = ((ContaTotal + ValorGorjeta)/DividirConta)
ValorFinal = round(NovaContaTotal, 2)
print(f"A Conta total ( com a gorjeta inclusa) deu {ValorFinal} por pessoa")
