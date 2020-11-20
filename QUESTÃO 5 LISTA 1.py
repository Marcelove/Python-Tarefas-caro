#Tempo de vida de um fumante

while True:
                x = int(input('Digite quantos cigarros você fuma por dia: '))
                if x != int:
                                y = int(input('Agora, digite a quantos anos você fuma: '))

                                z = (x/6)  #horas perdidas
                                m = (z*365) #horas totais perdidas
                                tt = (m/24) #dias perdidos

                                print ('Você perdeu ', int(tt), ' dias de vida :(. \n')

