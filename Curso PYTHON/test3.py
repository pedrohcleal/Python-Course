import math

def cakes(recipe, available):
    # Inicializa o valor mínimo como infinito, 
    # garantindo que qualquer valor será menor.
    min_value = float('inf')
    
    # Itera sobre os ingredientes necessários na receita.
    for ingredient in recipe:
        # Verifica se o ingrediente está disponível.
        if ingredient in available:
            # Calcula a quantidade de vezes que o 
            # ingrediente disponível pode ser dividido pela 
            # quantidade necessária na receita.
            div0 = (math.floor(available[ingredient] / recipe[ingredient]))
            
            # Atualiza o valor mínimo se a divisão for menor 
            # que o valor mínimo atual.
            if div0 < min_value:
                min_value = div0
        else:
            # Se um ingrediente necessário não estiver 
            # disponível, retorna 0 (receita não pode ser feita).
            return 0 
    
    # Retorna a quantidade mínima de vezes que 
    # a receita pode ser feita com os ingredientes disponíveis.
    return min_value
