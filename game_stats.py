class GameStats():
    """ Отслеживание статистики для игры """

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # запуск игры в активном состоянии
        self.game_active = True

    def reset_stats(self):
        """Инициализирует статистику в ходе игры"""
        # оставшиеся корабли

        self.ships_left = self.ai_settings.ship_limit

