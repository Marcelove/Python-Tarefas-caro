#Calculando o desconto previdenciario de um funcionário

while True:

    print ('Olá! calcularemos o desconto previdenciário do seu salário.\n')

    x = float(input('Por favor, nos informe seu salário:'))

    d = x*0.11

    if d < 318.20:
        print ('O seu desconto foi de {} reais' .format(d))

    else:
        print ('Seu desconto foi de 318.20 reais')

    
              
    
