#QUESTÃO 3.
#Ponto original 0,0.
#CIMA 5.
#BAIXO 3.
#ESQUERDA 3.
#DIREITA 2.
#calcular a distância entre a posição atual e -
#o ponto original após uma seqüência de movimentos.

a = int(input('Digite a distância percorrida para cima:'))
b = int(input('Digite a distância percorrida para baixo:'))
b = -b

    
c = int(input('Digite a distância percorrida para esquerda:'))
d = int(input('Digite a distância percorrida para direita:'))
c = -c

y = (a+b)
x = (c+d)

print('y = ', (y),' and x = ', (x))

hipot = (y**2) + (x**2)
hipot = hipot**0.5                      #A distância entre os pontos é a hipotenusa.


print('The distance is:', int(hipot))



