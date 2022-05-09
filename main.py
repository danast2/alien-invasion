import pygame
#настройки
from settings import Settings
#корабль
from ship import Ship
#игровые функции
import game_functions as gf
#импортируем группу для пуль(что-то вроде расширенного списка)
from pygame.sprite import Group
from alien import Alien
#игровая статистика
from game_stats import GameStats

def run_game():
    pygame.init()
    #создание экземпляра на основе класса Settings
    ai_settings=Settings()

    #задаём параметры экрана через экземпляр с настройками
    display=pygame.display.set_mode((ai_settings.display_width,ai_settings.display_height))
    pygame.display.set_caption(ai_settings.caption)

    #создание корабля
    ship = Ship(ai_settings, display)

    #создание группы для хранения пуль
    bullets=Group()

    #создание группы для хранения пришельцев
    aliens=Group()

    gf.create_fleet(ai_settings, display, aliens, ship)

    stats = GameStats(ai_settings)

    while True:
        #сначала происходит обработка событий
        gf.check_events(ai_settings, display, ship, bullets)

        if stats.game_active:
            #после обработка событий проиходит обновление позиции корабля
            ship.update()

            #обновляет позицию пули на экране
            gf.update_bullets(aliens, bullets, ai_settings, display, ship)

            #обновление позиции пришельцев
            gf.update_aliens(ai_settings, stats, display, ship, aliens, bullets)

        #дальше идёт отрисовка экрана на основе обработанных событий
        gf.update_screen(ai_settings, display, ship, bullets, aliens)



run_game()
