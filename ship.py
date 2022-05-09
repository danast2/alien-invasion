#класс с описанием корабля

import pygame


class Ship():

    def __init__(self,ai_settings, display):
        #ввод атрибута настроек,который наследует из класса с настройками игры
        self.ai_settings=ai_settings

        # Загрузка изображения корабля и получение прямоугольника.
        self.display = display
        self.image = pygame.image.load('images/space_ship.png')
        #прямоугольная переменная rect с картинкой
        self.rect = self.image.get_rect()
        #сохраняем прямоугольник экрана в переменную display_rect
        self.display_rect = display.get_rect()

        #задаём переменной rect параметры
        #переменная rect  содержит те же координаты (centerx) что и прямоугльник экрана (display_rect)
        self.rect.centerx=self.display_rect.centerx
        #аналогично и со стороной всего есть 4 стороны (top bottom left right)
        self.rect.bottom = self.display_rect.bottom

        # Сохранение вещественной координаты центра корабля.
        self.center=float(self.rect.centerx)

        #флаг перемещения вправо
        self.moving_right=False

        # флаг перемещения влево
        self.moving_left = False



    def blitme(self):
        #рисует корабль в текущей позиции
        #метод blit отрисовывает заданную ему поверхность
        #в него нужно передать саму поверхность (self.image)
        #и координаты для отрисовку этой поверхности (self.rect)
        #self.rect содаржит координаты по (х) центр по икс экрана
        #а по (у) нижнюю грань экрана
        #метод blit выглядит так: display.blit((какая-то поверхность),(x,y))
        self.display.blit(self.image,self.rect)

    def update(self):
        #перемещаем корабль вправо если self.moving_right==True
        #и Выражение self.rect.right возвращает координату x правого края прямоугольника корабля
        #если эта координата меньше координаты правого края прямоугольника экрана,то совершается перемещение
        if self.moving_right and self.rect.right<self.display_rect.right:
            #настраиваем скорость корабля
            self.center+=self.ai_settings.ship_speed_factor
        # перемещаем корабль вправо если self.moving_left==True
        # и Выражение self.rect.left возвращает координату x левого края края прямоугольника корабля
        #если эта координата больше нуля,то движение будет совершено
        if self.moving_left and self.rect.left>0:
            #настраиваем скорость корабля
            self.center-=self.ai_settings.ship_speed_factor
        #в self.rect.centerx сохраняется только целая
        self.rect.centerx=self.center

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.center=self.display_rect.centerx