#Aprovando empréstimo bancário para a compra de uma casa.

while True:

    print ('Veremos e seu empréstimo para a compra da casa será aprovado.\n')

    c = float(input('Nos informe o valor da casa:'))
    s = float(input('Nos infrome seu salário:'))
    a = int(input('nos informe a quantidade de anos a pagar:'))

    meses = a*12
    p = c/meses

    vp = p/s

    if vp <= 0.30:
        print ('Prestação aceita!\n')
        print ('.\n')

    elif vp > 0.30:
        print ('Prestação negada.\n')
        print ('.\n')
    

    
    
