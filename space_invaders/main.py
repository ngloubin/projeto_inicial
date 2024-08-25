import pygame
import random
from settings import WIDTH, HEIGHT, FPS, PLAYER_VEL, LASER_VEL, ENEMY_VEL
from entities import Player, Enemy
from assets import BG

pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

def redraw_window(window, player, enemies, lives, level, score, lost, lost_font, main_font):
    window.blit(BG, (0, 0))
    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
    level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
    score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))

    window.blit(lives_label, (10, 10))
    window.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
    window.blit(score_label, (WIDTH / 2 - score_label.get_width() / 2, 10))

    for enemy in enemies:
        enemy.draw(window)

    player.draw(window)

    if lost:
        lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
        window.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    # Game variables
    level = 0
    lives = 5
    score = 0
    lost = False
    lost_count = 0

    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    player = Player(300, 630)
    enemies = []
    wave_length = 5

    while run:
        clock.tick(FPS)
        redraw_window(WIN, player, enemies, lives, level, score, lost, lost_font, main_font)

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 2:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.get_width() < WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL > 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.get_height() < HEIGHT:
            player.y += PLAYER_VEL
        if keys[pygame.K_SPACE]:
            player.shoot()

        player.move_lasers(-LASER_VEL, enemies)

        for enemy in enemies[:]:
            enemy.move(ENEMY_VEL)
            enemy.move_lasers(LASER_VEL, player)

            if random.randrange(0, 2*FPS) == 1:
                enemy.shoot()

            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

            if player.collide(enemy):
                player.health -= 10
                enemies.remove(enemy)

    pygame.quit()

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()

if __name__ == "__main__":
    main_menu()
