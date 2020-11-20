#Recebendo cinco números inteiros e definindo maior e menor

import time

while True:
    
    print ('Você me dirá cinco números inteiros e eu direi qual o maior e qual o menor.\n')

    a = int(input('N1:'))
    b = int(input('N2:'))
    c = int(input('N3:'))
    d = int(input('N4:'))
    e = int(input('N5:'))

    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    #
                    print ('Calculando...')
                    time.sleep(2)
                    print ('O "N1" é o maior.\n')

    if b > a:
        if b > c:
            if b > d:
                if b > e:
                    #
                    print ('Calculando...')
                    time.sleep(2)
                    print ('O "N2" é o maior.\n')


    if c > a:
        if c > b:
            if c > d:
                if c > e:
                    #
                    print ('Calculando...')
                    time.sleep(2)
                    print ('O "N3" é o maior.\n')


    if d > a:
        if d > b:
            if d > c:
                if d > e:
                    #
                    print ('Calculando...')
                    time.sleep(2)
                    print ('O "N4" é o maior.\n')

    if e > a:
        if e > b:
            if e > c:
                if e > d:
                    #
                    print ('Calculando...')
                    time.sleep(2)
                    print ('O "N5" é o maior.\n')


    if a < b:
        if a < c:
            if a < d:
                if a < e:
                    #
                    print ('O "N1" é o menor.\n')

    if b < a:
        if b < c:
            if b < d:
                if b < e:
                    #
                    print ('O "N2" é o menor.\n')


    if c < a:
        if c < b:
            if c < d:
                if c < e:
                    #
                    print ('O "N3" é o menor.\n')


    if d < a:
        if d < b:
            if d < c:
                if d < e:
                    #
                    print ('O "N4" é o menor.\n')

    if e < a:
        if e < b:
            if e < c:
                if e < d:
                    #
                    print ('O "N5" é o menor.\n')



    

    
