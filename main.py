import pygame, controls
from gun import Gun
from pygame.sprite import Group
from statistic import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 790))
    pygame.display.set_caption('Armed Forces of Ukraine against кussian orcs')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    orks = Group()
    controls.create_army(screen, orks)
    stats = Stats()
    sc = Scores(screen,stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, orks, bullets)
            controls.update_bullets(screen, stats, sc, orks, bullets)
            controls.update_orks(stats, screen, sc, gun, orks, bullets)

run()