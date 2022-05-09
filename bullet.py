import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    #класс для управления пулями,выпущенные кораблём
    def __init__(self,ai_settings,display,ship):
        #создание объекста пули в текущей позиции корабля
        super().__init__()
        self.display=display

        #создание пули в позиции (0,0) и назначение правильной позиции
        #Прямоугольник инициализируется в точке (0, 0) , но в следующих двух строках он перемещается
        #в нужную позицию,так как позиция пули напрямую зависит от позиции корабля

        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_hight)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #в строчках (self.rect.centerx=ship.rect.centerx и  self.rect.top=ship.rect.top) задаётся позиция пули
        #тоесть не важно какая координата у корабля,у пули есть заданные параметры rect.centerx и self.rect.top ,по которым она появится
        #уже отталкиваясь от этого self.y получает значение (y) из rect.y
        #тоесть пуля отрисовалась в rect.centerx и self.rect.top и уже оттуда достаётся (y)
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        """Перемещает пулю вверх по экрану."""
        #обновление позиции пули в вещественном формате
        self.y-=self.speed_factor
        #обновление позиции прямоугольника
        self.rect.y=self.y
    def draw_bullet(self):
        """Выводит пули на экран"""
        pygame.draw.rect(self.display,self.color,self.rect)

