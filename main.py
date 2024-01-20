import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)

# Dimensões da tela
largura_tela = 800
altura_tela = 600

# Tamanho da cobra e da comida
tamanho_cobra = 20
tamanho_comida = 20

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Snake')

# Relógio para controlar a velocidade do jogo
clock = pygame.time.Clock()

# Função para desenhar a cobra na tela
def desenhar_cobra(tamanho_cobra, lista_cobra):
    for posicao in lista_cobra:
        pygame.draw.rect(tela, cor_cobra, [posicao[0], posicao[1], tamanho_cobra, tamanho_cobra])

# Função para exibir mensagem na tela
def mensagem(msg, cor):
    fonte = pygame.font.SysFont(None, 25)
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura_tela / 6, altura_tela / 3])

# Função principal do jogo
def jogo():
    game_over = False
    game_fim = False

    # Posição inicial da cobra
    posicao_x = largura_tela / 2
    posicao_y = altura_tela / 2

    # Variação da posição da cobra
    variacao_x = 0
    variacao_y = 0

    # Lista para armazenar as partes da cobra
    lista_cobra = []
    tamanho_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_tela - tamanho_comida) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_comida) / 20.0) * 20.0

    while not game_over:

        while game_fim == True:
            tela.fill(cor_fundo)
            mensagem("Fim de jogo! Pressione C para jogar novamente ou Q para sair", (255, 255, 255))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_fim = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    variacao_x = -tamanho_cobra
                    variacao_y = 0
                elif event.key == pygame.K_RIGHT:
                    variacao_x = tamanho_cobra
                    variacao_y = 0
                elif event.key == pygame.K_UP:
                    variacao_y = -tamanho_cobra
                    variacao_x = 0
                elif event.key == pygame.K_DOWN:
                    variacao_y = tamanho_cobra
                    variacao_x = 0

        if posicao_x >= largura_tela or posicao_x < 0 or posicao_y >= altura_tela or posicao_y < 0:
            game_fim = True

        posicao_x += variacao_x
        posicao_y += variacao_y
        tela.fill(cor_fundo)
        pygame.draw.rect(tela, cor_comida, [comida_x, comida_y, tamanho_comida, tamanho_comida])
        cabeca_cobra = []
        cabeca_cobra.append(posicao_x)
        cabeca_cobra.append(posicao_y)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > tamanho_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                game_fim = True

        desenhar_cobra(tamanho_cobra, lista_cobra)
        pygame.display.update()

        if posicao_x == comida_x and posicao_y == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_comida) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_comida) / 20.0) * 20.0
jogo()