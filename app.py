print("💡 Calculadora Consumo de Energia Elétrica 💡")
aparelho = input("Digite o nome do Aparelho: ")
potencia = float(input("Digite a Potência do Aparelho (em Watts): "))
horas = float(input("Digite o Tempo de Uso Diário (em horas): "))
consumo_diario = (potencia * horas) / 1000  # Convertendo para kWh
consumo_mensal = consumo_diario * 30  # Considerando 30 dias

print(f"\nO consumo diário do {aparelho} é: {consumo_diario:.2f} kWh")
print(f"O consumo mensal do {aparelho} é: {consumo_mensal:.2f} kWh")    

custo_kwh = float(input("Digite o Custo do kWh (em R$): "))
custo_diario = consumo_diario * custo_kwh   
custo_mensal = consumo_mensal * custo_kwh
print(f"\nO custo diário do {aparelho} é: R$ {custo_diario:.2f}")
print(f"O custo mensal do {aparelho} é: R$ {custo_mensal:.2f}")     
