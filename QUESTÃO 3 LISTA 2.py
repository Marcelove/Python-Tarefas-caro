#Cálculo do IMC
#A fórmula é: IMC = Peso(Kg) / (Altura(m)*Altura(m))

while True:
    
    print('Olá! Veremos se você está acima do peso com base no seu IMC.\n')

    p = float(input('Digite seu peso em Kg:'))
    h = float(input('Digite sua altura em metros:'))

    z = (h*h)
    a = (p/z)

    if a > 25:
        print ('Você está acima do peso!\n')

    else:
        print ('Seu peso está em ordem.\n')


    
              
    
    
