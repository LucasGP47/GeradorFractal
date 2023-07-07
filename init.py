import turtle 

#setando o import da biblioteca
imp = turtle.Turtle()

#Declara os valores iniciais + o valor a ser escolhido que irá gerar o numero de fractais
ramos = int(input("Insira o valor de n: "))
angulo = 0.9
tamanho = 90

#Configura a imagem e a velocidade
imp.left(90)
imp.speed(100)
imp.setpos(0, 0)

#Função para gerar os fractais recursivamente
def desenhaArvore(angulo, ramos, aux):
    if angulo >= ramos:
        return 0
    else:
        imp.forward(tamanho * (0.8 ** angulo))
        imp.left(45 * (0.9 ** angulo))
        desenhaArvore(angulo+1, ramos, 0)
        imp.right(90 * (0.9 ** angulo))
        desenhaArvore(angulo + 1, ramos , 1)
        imp.left(45 * (0.9 ** angulo))
        imp.back(tamanho * (0.8 ** angulo))
        
#chama a função que cria a arvore
desenhaArvore(angulo, ramos, 0)

#Encerra o programa
turtle.done()