#Participação de um indivíduo no crime
# 5/5 = assasino
# 3/5 ou 4/5 = cúmplice
#2/5 = suspeita
# 0/5 ou 1/5 = inocente

while True:

    cont=0

    print ('Este é um questionário para indentificarmos sua relação com o assasinato.\n')
    print ('Por favor, responda "SIM" ou "NAO" para as seguintes perguntas:\n')
    
    a = input ('Telefonou para a vítima?:')
    if (a == 'SIM'):
        cont+=1
    b = input ('Esteve no local do crime?:')
    if (b == 'SIM'):
        cont+=1
    c = input ('Mora perto da vítima?:')
    if (c == 'SIM'):
        cont+=1
    d = input ('Devia para a vítima?:')
    if (d == 'SIM'):
        cont+=1
    e = input ('Já trabalhou com a vítima?:')
    if (e == 'SIM'):
        cont+=1

#Checando
    if cont <=1:
        print ('.\n')
        print ('Você é inocente.\n')
        print ('.\n')

    if cont == 2:
        print ('.\n')
        print ('Você é suspeito.\n')
        print ('.\n')

    if cont == 3:
        print ('.\n')
        print ('Você é cúmplice!\n')
        print ('.\n')

    if cont == 4:
        print ('.\n')
        print ('Você é cúmplice!\n')
        print ('.\n')

    if cont == 5:
        print ('.\n')
        print ('Você é o assasino!\n')
        print ('.\n')


        

            
        
