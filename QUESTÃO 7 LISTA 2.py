#Indentificando se o ano é bissexto ou não.
import time

while True:

    print ('Iremos lhe informar se o ano é bissexto ou não.\n')

    ano = float(input('Digite o ano que deseja consultar:'))

    

    if ano%400 == 0:
        print ('Verificando...')
        time.sleep(2)
        print ('Esse ano é bissexto!\n')
        print ('.\n')

    elif ano%100 == 0:
        print ('Verificando...')
        time.sleep(2)
        print ('Esse ano não é bissexto!\n')
        print ('.\n')

    elif ano%4 == 0:
        print ('Verificando...')
        time.sleep(2)
        print ('Esse  é bissexto!\n')
        print ('.\n')

    else:
        print ('Verificando...')
        time.sleep(2)
        print ('Esse ano não é bissexto!\n')
        print ('.\n')
        
        
        

