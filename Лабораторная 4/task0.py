class Games(object):
    """ Базовый класс игры.
    :param name: Имя игры
    :param game_type: Тип игры
    :param cost: Стоимость игры (в рублях)
    """
    def __init__(self, name: str, game_type: str, cost: float):
        if (not isinstance(name, str)) or (not isinstance(game_type, str)) or (not isinstance(cost, float)):
            raise TypeError("Недопустимый тип")
        self._name = name
        self._game_type = game_type
        self._cost = cost

    def __str__(self):
        return f'Игра: {self._name}. Тип игры: {self._game_type}. Стоимость {self._cost} р.'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r},' \
               f'game_type={self._game_type!r},' \
               f'cost={self._cost})'

    @property
    def name(self) -> str:
        """ Геттер. """
        return self._name

    @property
    def game_type(self) -> str:
        """ Геттер. """
        return self._game_type

    @property
    def cost(self) -> float:
        """ Геттер. """
        return self._cost

    @staticmethod
    def warning() -> None:
        """ Выводит на экран уведомление об абсолютной безопасности игры. """
        print(f'Эта игра абсолютно безопасна.')

    def purchase_calc_opportunity(self, cost: float) -> None:
        """ Метод для оценивания возможности покупки игры. """
        if cost - self._cost < 0:
            print(f'Вы не можете позволить себе эту игру!')
        else:
            print(f'Вы можете позволить себе эту игру!')


class ComputerGames(Games):
    """ Унаследованный класс компьютерной игры.
    :param name: Имя игры
    :param cost: Стоимость игры (в рублях)
    :param is_online_game: Является ли эта компьютерная игра онлайн-игрой.
    """
    def __init__(self, name: str, cost: float, is_online_game: bool = False):
        if not isinstance(is_online_game, bool):
            raise TypeError('Недопустимый тип')
        super().__init__(name=name, game_type='Компьютерная игра', cost=cost)
        self._is_online_game = is_online_game

    def __str__(self):
        if self._is_online_game:
            return f'Игра: {self._name}. Тип игры: {self._game_type}. Стоимость {self._cost} р. Онлайн игра.'
        else:
            return f'Игра: {self._name}. Тип игры: {self._game_type}. Стоимость {self._cost} р. Оффлайн игра.'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r},' \
               f'cost={self._cost},i' \
               f's_online_game={self._is_online_game})'

    @property
    def is_online_game(self) -> bool:
        """ Геттер. """
        return self._is_online_game

    @staticmethod
    def warning() -> None:
        """
        Выводит на экран возможные предупреждения о влиянии игры на здоровье.\n
        Перегружен, потому что нужна другая строчка в выводе.
        """
        print(f'Осторожно! Компьютерные игры вызывают аутизм!')
