#Preço pela diária e kilometragem

while True:
                x = int(input('Digite a kilometragem percorrida por você no carro alugado: \n'))
                if x != int:
                        y = int(input('Agora, digite o número de dias de uso: \n'))

                        z = (x*0.15)  #preço por kilometragem
                        m = (y*60)    #Preço da diária

                        print('O valor a ser pago é de: ', (m+z))
