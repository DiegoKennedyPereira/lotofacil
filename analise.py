# Importamos a lista de resultados do arquivo dados_lotofacil.py
from dados_lotofacil import resultados

# Criamos um dicionário para contar quantas vezes cada número de 1 a 25 aparece
# Começamos todos com zero
contagem = {i: 0 for i in range(1, 26)}

# Passamos por cada sorteio da nossa lista
for sorteio in resultados:
    # Para cada número que saiu no sorteio, aumentamos a contagem dele
    for numero in sorteio:
        contagem[numero] += 1

# Ordenamos os números para mostrar do mais frequente para o menos frequente
# Se houver empate na frequência, ordenamos pelo valor do número em ordem crescente
ranking = sorted(contagem.items(), key=lambda item: (-item[1], item[0]))

# Mostramos o resultado final formatado no terminal
print("Análise de frequência dos números da Lotofácil:")
for numero, quantidade in ranking:
    # O :02d faz com que números menores que 10 apareçam com um zero na frente (ex: 01, 02)
    print(f"Número {numero:02d}: {quantidade} vezes")
