#класс с настройками игры
class Settings:
    def __init__(self):
        #атрибуты экрана
        self.display_width = 1200
        self.display_height = 800

        #цвет бэкграунда
        self.bg_color = (230,230,230)
        #название
        self.caption="Инопланетное вторжение"
        #атрибут скорости корабля
        self.ship_speed_factor=1.5

        #Максимальное количетво кораблей
        self.ship_limit = 3



        #атрибуты пули
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_hight = 15
        self.bullet_color=60,60,60
        #максимально разрешённое количество пуль
        self.bullets_allowed=3

        #Настройки пришельца
        #скорость пришельца
        self.alien_speed_factor = 1
        #величина снижения флота пришельцев вниз (при достижении ими края)
        self.fleet_drop_speed = 100
        #fleet_direction = 1 - обозначает направление вправо (-1 обозначает движение влево)
        self.fleet_direction = 1

