import pygame

def test_sounds():
    pygame.init()
    pygame.mixer.init()
    
    try:
        laser_sound = pygame.mixer.Sound("sounds/space-laser.wav")
        laser_sound.play()
        pygame.time.delay(2000)  # Espera 2 segundos para ouvir o som
    except pygame.error as e:
        print(f"Falha ao carregar ou tocar o som: {e}")

    pygame.quit()

if __name__ == "__main__":
    test_sounds()
