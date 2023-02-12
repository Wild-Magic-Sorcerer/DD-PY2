class Games(object):
    """ Базовый класс игры. """
    def __init__(self, name: str, game_type: str, cost_roubles: float):
        if (not isinstance(name, str)) or (not isinstance(game_type, str)) or (not isinstance(cost_roubles, float)):
            raise TypeError("Недопустимый тип")
        self._name = name
        self._game_type = game_type
        self._cost_roubles = cost_roubles

    def __str__(self):
        return f'Игра: {self._name}. Тип игры: {self._game_type}. Стоимость {self._cost_roubles} р.'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r},' \
               f'game_type={self._game_type!r},' \
               f'cost_roubles={self._cost_roubles})'

    @property
    def name(self) -> str:
        """ Геттер. """
        return self._name

    @property
    def game_type(self) -> str:
        """ Геттер. """
        return self._game_type

    @property
    def cost_roubles(self) -> float:
        """ Геттер. """
        return self._cost_roubles

    @staticmethod
    def possible_warning() -> None:
        """ Выводит на экран уведомление об абсолютной безопасности игры. """
        print(f'Эта игра абсолютно безопасна.')

    def purchase_calc(self, money_roubles: float) -> None:
        """ Метод для оценивания возможности покупки игры. """
        if money_roubles - self._cost_roubles < 0:
            print(f'Вы не можете позволить себе эту игру!')
        else:
            print(f'Вы можете позволить себе эту игру!')


class ComputerGames(Games):
    """ Унаследованный класс компьютерной игры. """
    def __init__(self, name: str, cost_roubles: float, is_online_game: bool = False):
        if not isinstance(is_online_game, bool):
            raise TypeError('Недопустимый тип')
        game_type: str = 'Компьютерная игра'
        super().__init__(name, game_type, cost_roubles)
        self._is_online_game = is_online_game

    def __str__(self):
        if self._is_online_game:
            return f'Игра: {self._name}. Тип игры: {self._game_type}. Стоимость {self._cost_roubles} р. Онлайн игра.'
        else:
            return f'Игра: {self._name}. Тип игры: {self._game_type}. Стоимость {self._cost_roubles} р. Оффлайн игра.'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r},' \
               f'cost_roubles={self._cost_roubles},i' \
               f's_online_game={self._is_online_game})'

    @property
    def is_online_game(self) -> bool:
        """ Геттер. """
        return self._is_online_game

    @staticmethod
    def possible_warning() -> None:
        """
        Выводит на экран возможные предупреждения о влиянии игры на здоровье.\n
        Перегружен, потому что нужна другая строчка в выводе.
        """
        print(f'Осторожно! Компьютерные игры вызывают аутизм!')
        