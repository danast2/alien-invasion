import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий пришельца"""

    def __init__(self, ai_settings, display):
        """Инициализирует пришельца и даёт его начальную позицию"""
        super().__init__()
        self.dispay=display
        self.ai_settings=ai_settings

        #Загрузка изображения пришельца и назначение атрибута rect,который содержит прямоугольную картинку пришельца
        self.image=pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #Каждый пришелец появляется в углу экрана
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #Сохранение точной позиции пришельцев
        self.x=float(self.rect.x)


    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.dispay.blit(self.image,self.rect)

    def update(self):
        """Перемещает пришельца вправо"""
        #self.ai_settings.fleet_direction нужно для того,чтобы задать направление пришельцев
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)

        #точное значение хранится в self.x,здесь идёт передача значения
        #прямоугольнику пришельца для обновления его позиции
        self.rect.x=self.x

    def check_edges(self):
        """Возращает True ,если пришелец находится у края экрана"""

        display_rect = self.dispay.get_rect()
        if self.rect.right >= display_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
