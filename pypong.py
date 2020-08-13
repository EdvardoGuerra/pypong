import pygame

pygame.init()
pygame.font.init()
fonte = pygame.font.get_default_font()
titulo_font = pygame.font.SysFont(name=fonte, size=42, bold=True, italic=False)
texto_font = pygame.font.SysFont(name=fonte, size=32, bold=False, italic=False)

AMARELO = (255, 255, 0)
AZUL = (25, 63, 144)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

TELA_LARGURA = 1000
TELA_ALTURA = 600
QUADRA_LARGURA = 800
QUADRA_ALTURA = TELA_ALTURA

JOGANDO = 0
PAUSADO = 1
CONTINUA = True

tamanho_tela = (TELA_LARGURA, TELA_ALTURA)
tamanho_quadra = (QUADRA_LARGURA, QUADRA_ALTURA)

bola_raio = 10
bola_vel_x = 1
bola_vel_y = 1

tela = pygame.display.set_mode(size=tamanho_tela)
clock = pygame.time.Clock()
clock.tick(60)


class Quadra:
    def __init__(self, tamanho, cor):
        self.largura = tamanho[0]
        self.altura = tamanho[1]
        self.cor = cor
        self.traco_largura = 4
        self.traco_altura = int(self.altura / 21)
        self.traco_pos_x = int(self.largura / 2)

    def desenha(self):
        quadra_rect = pygame.Rect(0, 0, self.largura, self.altura)
        pygame.draw.rect(tela, PRETO, quadra_rect)
        for i in range(0, 23, 2):
            traco_rect = pygame.Rect(self.traco_pos_x, self.traco_altura * i, self.traco_largura, self.traco_altura)
            pygame.draw.rect(tela, BRANCO, traco_rect)

        titulo_txt = titulo_font.render('PyPong 0.1', 1, BRANCO)
        tela.blit(titulo_txt, (815, 20))
        placar_txt = texto_font.render('Placar', 1, BRANCO)
        tela.blit(placar_txt, (860, 80))


class Bola:
    def __init__(self, raio, vel_x, vel_y, cor, quadra):
        self.pos_x = int(quadra.largura / 2)
        self.pos_y = int(quadra.altura / 2)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.raio = raio
        self.cor = cor
        self.quadra = quadra

    def desenha(self):
        pygame.draw.circle(tela, self.cor, (self.pos_x, self.pos_y), self.raio)

    def move(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.desenha()
        if self.pos_x <= 0 or self.pos_x >= self.quadra.largura:
            self.vel_x *= -1
        if self.pos_y <= 0 or self.pos_y >= self.quadra.altura:
            self.vel_y *= -1


quadra = Quadra(tamanho_quadra, PRETO)
bola = Bola(bola_raio, bola_vel_x, bola_vel_y, VERMELHO, quadra)

while CONTINUA:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CONTINUA = False

    quadra.desenha()
    # bola.desenha()
    bola.move()

    pygame.display.flip()
    tela.fill(AZUL)

pygame.quit()
