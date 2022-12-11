import doctest
import logging
import jsonschema

class Observer(object):
    def __init__(self, logger: logging.Logger = logging.getLogger('Observer'), config: str = None, validator: jsonschema.Validator = None):
        """
        Создание и подготовка к работе объекта "Observer". Проверяет сервисы systemd.

        :param logger: Логгер - Направление отправки логов работы программы.
        :param config: Глобальный адрес расположения файлов нстройки программы.
        :param validator: Валидатор схемы для валидации запросов, поступающих извне.

        Примеры:
        >>> server = Observer()  # инициализация экземпляра класса
        """
        self.logger = logger
        self.config = config
        self.validator = validator

    def getService(self, service: str) -> str:
        """
        Функция, которая возвращает статус сервиса sysmted.

        :param service: Имя сервиса systemd.

        :return: Статус работы сервиса (активен/неактивен/не загружен).

        Примеры:
        >>> server = Observer()
        >>> server.getService(service='observerd.service')
        """
        ...

    def getJournal(self, service: str, num: int = None) -> str:
        """
        Функция, которая возвращает последнеи num строчек журнала systemd (получаемый командой journalctl), связанных с сервисом service.

        :param service: Имя сервиса systemd.
        :param num: Число строек журнала systectl. Если не задан, то будет выведены все строчки текущего запуска.

        :raise TypeError: Если типы не совпадают, то выдётся ощибка.
        :return: Последние num срочек journalctl по этому сервису. Если num is None, то возвращается журнал текущего бута.

        Примеры:
        >>> server = Observer()
        >>> server.getJournal(service='observerd.service', num=5)
        >>> server.getJournal(service='chronyd.service')
        """
        if num is not None:
            if not isinstance(num, int):
                raise TypeError("Число строк должно быть либо int, либо не заданным.")
        ...

    def startListening(self, ip: str, port: int) -> None:
        """
        Функция, которая начинает прослушку на сокетах по адресу ip:port для принятия, валидации и обработки запросов.

        :raise TypeError: Если типы не совпадают, то выдётся ощибка.
        :return: Ничего. Прослушка идёт бесконечно до прерывания пользователем работы.

        Примеры:
        >>> server = Observer()
        >>> server.startListening(ip='127.0.0.1', port=10080)
        """
        if not isinstance(ip, str):
            raise TypeError("Адрес должен быть str.")
        elif not isinstance(port, int):
            raise TypeError("Порт должен быть int.")


class ServerTools(object):
    def __init__(self, logger: logging.Logger = logging.getLogger('STOOLZ'), silent: bool = False):
        """
        Создание и подготовка к работе объекта "ServerTools". Проверяет статусы работы различных систем.

        :param logger: Логгер - Направление отправки логов работы программы.
        :param silent: "Тихий" режим работы.

        Примеры:
        >>> stools = ServerTools(silent=True)  # инициализация экземпляра класса
        """
        self.logger = logger
        if silent:
            self.logger.addHandler(logging.NullHandler())


    def ping(self, ip: str, port: int, timeout: int = 5) -> tuple[bool, str]:
        """
        Пинг сервера через сокет.

        :param ip: IP адрес.
        :param port: Порт.
        :param timeout: Таймаут подключения.

        :return: Кортеж со статусом проверки и подробным текстовым описанием процессов проверки.

        Примеры:
        >>> stools = ServerTools(silent=True)
        >>> stools.ping(ip='127.0.0.1', port=10080)
        """
        ...

    def check_web(self,
                  ip: str,
                  port: int,
                  protocol: str = 'http',
                  text: str = '',
                  params: any = None) -> tuple[bool, str]:
        """
        Проверка успешного открытия веб-интерфейса.

        :param ip: IP адрес.
        :param port: Порт.
        :param protocol: Протокол для подключения к вуб-адресу.
        :param text: Текст, искомый на веб-странице.
        :param params: Дополнительные опциональные параметры подкоючения.

        :return: Кортеж со статусом проверки и подробным текстовым описанием процессов проверки.

        Примеры:
        >>> stools = ServerTools(silent=True)
        >>> stools.check_web(ip='8.8.8.8', port=80,text='google')
        """
        ...


    def get_domain_addr(self, domain: str, domain_compare: str = None) -> tuple[bool, str]:
        """
        Получение доменного адреса у машины и сравнение его с требуемым.

        :param domain: Доменное, из которого получаем ассоциированный доменный адрес.
        :param domain_compare: Доменный адрес для сравнения. Если не задан, то проверка не происходит.

        :return: Кортеж со статусом проверки и подробным текстовым описанием процессов проверки.

        Примеры:
        >>> stools = ServerTools(silent=True)
        >>> stools.get_domain_addr(domain='8.8.8.8', domain_compare='dns.google')
        """
        ...


class Sentry(object):
    def __init__(self, logger: logging.Logger = logging.getLogger('Observer'), config: str = None,
                 validator: jsonschema.Validator = None, pause: int = 10):
        """
        Создание и подготовка к работе объекта "Sentry". Отправляет запросы на машины с демонами Observer.

        :param logger: Логгер - Направление отправки логов работы программы.
        :param config: Глобальный адрес расположения файлов нстройки программы.
        :param validator: Валидатор схемы для валидации запросов, поступающих извне.
        :param pause: Пауза между проверками.

        Примеры:
        >>> watcher = Sentry(pause=3)  # инициализация экземпляра класса
        """
        self.logger = logger
        self.config = config
        self.validator = validator
        self.pause = pause


    def read_setting(self, config_filepath: str) -> None:
        """
        Чтение файла настроек.

        :param config_filepath: Глобальное расположение файла настроек.
        :raise FileNotFound: Если файл не найден, то выдётся ощибка.
        :return: Ничего не возращает.

        Примеры:
        >>> watcher = Sentry(pause=3)
        >>> watcher.read_setting(config_filepath='/etc/conf/stuff/file.txt')
        """
        ...

    def read_commands(self, commands_filepath: str) -> None:
        """
        Чтение файла команд из формата .yaml.

        :param commands_filepath: Глобальное расположение файла комманд.
        :raise FileNotFound: Если файл не найден, то выдётся ощибка.
        :return: Ничего не возращает.

        Примеры:
        >>> watcher = Sentry(pause=3)
        >>> watcher.read_commands(commands_filepath='/etc/conf/stuff/commands.yaml')
        """
        ...

    def run(self) -> None:
        """
        Запуск работы Sentry. Получает настройки, команды, подлючется по сокету к демонам с observer, проверяет результаты их работы.

        :return: Ничего не возращает.

        Примеры:
        >>> watcher = Sentry(pause=3)
        >>> watcher.run()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
