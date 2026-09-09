distancia = float(input("digite a distância até o destino em km: "))
consumo = float(input("digite o consumo em km: "))
preço = float (input("digite o preço da gasolina: "))

litros = distancia / consumo 
custo = litros * preço 

print(f"O custo da viagem será de: R$ {custo:.2f}")