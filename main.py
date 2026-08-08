from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
import pygame

def main() -> None:
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill(color='black')
        pygame.display.flip()

if __name__ == "__main__":
    main()