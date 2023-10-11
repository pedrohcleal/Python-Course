import pygame

azul = (50, 100,213)
laranja = (205,201,0)

dimensoes = (600,600)

#posição inicial do quadrado
x=300
y=300
d = 20

lista_cobra =

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('snake da kenzi') #nome da aba no windows

tela.fill(azul) #preencher cor da tela

clock = pygame.time.Clock()

def desenha_cobra():
    pygame.draw.rect(tela, laranja, [x,y,d,d])
    for unidade in lista_cobra:
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])

def mover_cobra():
    delta_x = 0
    delta_y = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -d
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = d
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -d
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = d

    x_novo = lista_cobra[-1][0] + delta_x
    y_novo = lista_cobra[-1][1] + delta_y

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]
    
    return x, y

while True:
    pygame.display.update()
    desenha_cobra()
    x , y = mover_cobra()
    print(x,y)
    clock.tick(10)
