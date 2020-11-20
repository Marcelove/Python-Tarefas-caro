#QUESTÃO 1
#p=(b+(n/b))/2

n = int(input('Digite o número que você deseja obter a raiz quadrada:')) #n
b = 2 #base
p= 0

while abs(n - p) >= 0.0001:
    p=(b+(n/b))/2
    p = p**2
    b = p

print('A raiz quadrada de', (n), 'é:', (b))
    
    


    

    

