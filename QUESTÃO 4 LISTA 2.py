#Checando triângulos e dizendo suas propiedads

while True:
    
    print ('Olá! Vamos ver se você consegue formar um triângulo com 3 valores de retas.')
    fi =  int(input('Digite o valor da primeira reta:\n'))
    se =  int(input('Digite o número da segunda reta:\n'))
    th =  int(input('Digite o número da terceira reta:\n'))

    if (fi+se) < th or (fi+th) < se or (th+se) < fi:
        print ('Não é um triângulo')
        print ('.\n')

    else:
        print ('.\n')
        print ('Sim! Um triângulo.\n')
       
        if fi == se == th:
            print ('Um triângulo equilátero')
            print ('.\n')

        elif fi == se or se == th or th == fi:
            print ('Um triângulo isósceles')
            print ('.\n')

        elif fi != se != th:
            print ('Um triângulo escaleno')
            print ('.\n')


    
