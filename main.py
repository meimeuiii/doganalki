import pygame

from player import Player
from vorog import Vorog

window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
background = pygame.transform.scale(
    pygame.image.load("background.png"),(700,500)
)

yaremiu = Player(100,100,50,50,"sprite1.png",10)
svyatik = Vorog(500,100,70,70,"sprite2.png",6)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    yaremiu.move()
    svyatik.move()
    window.blit(background,(0,0))
    yaremiu.draw(window)
    svyatik.draw(window)
    pygame.display.flip()
    fps.tick(60)