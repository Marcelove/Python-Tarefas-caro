#QUESTÃO 2
ver = 0

senha = input('Digite a senha desejada:')
a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
b = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
c = '0 1 2 3 4 5 6 7 8 9'.split()
d = '$ # @'.split()

for car in senha:
    if car in a:
        ver = 1

for car in senha:
    if car in b:
        if ver == 1:
            ver = 2


for car in senha:
    if car in c:
        if ver == 2:
            ver = 3
        


for car in senha:
    if car in d:
        if ver == 3:
            ver = 4

if len(senha) >= 6:
    if len(senha) <=12:
        
        ver = 5


        
if ver == 5:
    #x = senha.split()
    #print (senha[0:-1])
    print (senha)

else:
    print ('Senha inválida')
                          
                          
                
        
        


