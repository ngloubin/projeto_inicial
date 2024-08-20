import pygame
import sys
import os

# Inicializa o Pygame
pygame.init()

# Define as constantes
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Caminhos para os arquivos de áudio
laser_path = 'laser.wav'
explosion_path = 'explosion.wav'

# Verifica se os arquivos existem
if not os.path.isfile(laser_path):
    print(f"Erro: O arquivo de som do tiro '{laser_path}' não foi encontrado.")
if not os.path.isfile(explosion_path):
    print(f"Erro: O arquivo de som da explosão '{explosion_path}' não foi encontrado.")

# Cria a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Carrega os efeitos sonoros
laser_sound = pygame.mixer.Sound(laser_path)  # Caminho para o som do tiro
explosion_sound = pygame.mixer.Sound(explosion_path)  # Caminho para o som da explosão
 
# Função para criar a imagem da nave do jogador
def create_player_image():
    image = pygame.Surface((32, 16), pygame.SRCALPHA)
    image.fill(BLACK)
    pygame.draw.polygon(image, RED, [(16, 0), (32, 16), (0, 16)])  # Nave estilizada
    return image

# Função para criar a imagem do invasor
def create_invader_image():
    image = pygame.Surface((24, 16), pygame.SRCALPHA)
    image.fill(BLACK)
    pygame.draw.polygon(image, GREEN, [(12, 0), (24, 16), (0, 16)])  # Invasor estilizado
    pygame.draw.rect(image, GREEN, (6, 12, 12, 4))  # Detalhe inferior
    return image

# Função para criar a imagem da bala
def create_bullet_image():
    image = pygame.Surface((4, 10), pygame.SRCALPHA)
    image.fill(BLACK)
    pygame.draw.rect(image, WHITE, (0, 0, 4, 10))  # Bala estilizada
    return image

# Define a classe para os invasores
class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = create_invader_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.health = 1

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH - 24 or self.rect.x < 0:
            self.speed = -self.speed

# Define a classe para a nave do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = create_player_image()
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - self.rect.width / 2
        self.rect.y = HEIGHT - self.rect.height - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        # Evita que o jogador saia da tela
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

# Define a classe para as balas
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = create_bullet_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# Cria os invasores
invaders = pygame.sprite.Group()
for i in range(5):
    for j in range(3):
        invader = Invader(i * 40 + 20, j * 40 + 20)
        invaders.add(invader)

# Cria a nave do jogador
player = Player()

# Cria o grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(invaders)

# Cria o grupo de balas
bullets = pygame.sprite.Group()

# Inicializa a pontuação
score = 0

# Define a função para lidar com eventos
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet(player.rect.x + (player.rect.width - 4) // 2, player.rect.y)
            bullets.add(bullet)
            all_sprites.add(bullet)
            laser_sound.play()

# Define a função para atualizar o jogo
def update():
    all_sprites.update()
    bullets.update()

    # Verifica se o jogador colidiu com algum invasor
    if pygame.sprite.spritecollideany(player, invaders):
        game_over()
        pygame.quit()
        sys.exit()

    # Verifica colisão entre balas e invasores
    for bullet in pygame.sprite.groupcollide(bullets, invaders, True, True):
        global score
        score += 1
        explosion_sound.play()

# Define a função para desenhar o jogo
def draw():
    screen.fill(BLACK)
    all_sprites.draw(screen)
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (10, 10))

# Define a função para o jogo sobre
def game_over():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Score: " + str(score), 1, WHITE)
    screen.blit(text, (WIDTH / 2 - 100, HEIGHT / 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)  # Pausa para que o jogador veja a tela de Game Over

# Loop principal do jogo
clock = pygame.time.Clock()
while True:
    handle_events()
    update()
    draw()
    pygame.display.flip()
    clock.tick(60)
