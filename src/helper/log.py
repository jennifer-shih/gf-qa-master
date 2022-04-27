import logging
from pathlib import Path

from rich.logging import RichHandler

"""
Logger 為 singleton object，使用時只需初始化一次後，之後便可直接取用相同 logger。
若需使用不同的 logger，只要再次宣告即可。
init:
    Logger(name='One', level='Debug', need_saving_file=True)
usage:
    Logger.getLogger().info('XXXX')
    Logger.getLogger().warning('XXXX')

這裡我們不建立一個method寫log，而是需要getLogger()之後call warning的原因是要記錄該log的行數。
如果定義一個method，使之變成Logger.info('XXXX')，則log記錄到的行數永遠都會是log.py中該method定義的行數。
"""


class Logger:
    _log_name = None
    _instance = None
    _path = None

    def __new__(cls, **kwargs):
        name = kwargs.pop("name", None)
        level = kwargs.pop("level", "INFO")
        path = kwargs.pop("path", "")
        enable_rich_log = kwargs.pop("enable_rich_log", True)

        if name != None:
            cls._log_name = name
            cls._level = level
            cls._path = path
            cls._enable_rich_log = enable_rich_log
        else:
            if cls._log_name == None:
                raise Exception("Need to init Logger first")

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, name=None, level="INFO", path=None, enable_rich_log=True):
        if logging.getLogger(self._log_name).hasHandlers() == False:
            self.__init_logger(name, level, path, enable_rich_log)

    def __init_logger(self, name, str_level, path, enable_rich_log):
        level = self.__str_to_level(str_level)
        logger = logging.getLogger(self._log_name)
        FORMAT = "[%(asctime)s.%(msecs)03d] %(levelname)-8s %(message)-80s  (%(filename)s:%(lineno)s)"
        RICH_FORMAT = "%(message)s  (%(filename)s:%(lineno)s)"
        formatter = logging.Formatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
        rich_formatter = logging.Formatter(RICH_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
        logger.setLevel(level)

        # use rich log?
        if enable_rich_log:
            rh = RichHandler()
            rh.setFormatter(rich_formatter)
            logger.addHandler(rh)
        else:
            sh = logging.StreamHandler()
            sh.setFormatter(formatter)
            logger.addHandler(sh)

        if path:
            p = Path(path)
            log_folder = p.parent
            # make sure log folder exist
            if not log_folder.exists():
                log_folder.mkdir(parents=True)
            # add file handler
            fh = logging.FileHandler(filename=str(p), mode="w", encoding="utf8")
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        """
        TimedRotatingFileHandler: https://www.itread01.com/content/1563349863.html
        suffix 設定要特別注意，格式即是判斷rotate的依據。python會判斷末位數字的差值是否超過
        我們設定的 when * interval。如果要以秒數分割，suffix必須設定到秒位；以分數分割，
        suffix必須設定到分位
        """
        # if need_saving_file:
        #     log_folder = gl.log_path/str(log_name)
        #     log_file = log_folder/(str(log_name) + '.log')
        #     # make sure log folder exist
        #     if not log_folder.exists():
        #         log_folder.mkdir(parents=True)
        #     # add rotating file handler
        #     th = handlers.TimedRotatingFileHandler(filename=str(log_file), when='M', interval=1, backupCount=10, encoding='utf-8')
        #     th.suffix = "%Y-%m-%d_%H-%M" + '.log'
        #     th.setFormatter(formatter)
        #     logger.addHandler(th)

    @staticmethod
    def __str_to_level(level):
        level_map = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
        }
        level = level.upper()
        if level in level_map:
            return level_map[level]
        else:
            raise Exception("Log level [{0}] not in {1}".format(level, level_map.keys()))

    @classmethod
    def getLogger(cls):
        return logging.getLogger(cls._log_name)

    @classmethod
    def getName(cls):
        return str(cls._log_name)

    @classmethod
    def getFilePath(cls):
        return str(cls._path)


class LogFormat:
    @staticmethod
    def Feature(text):
        return text

    @staticmethod
    def Scenario(text):
        return "  {0}".format(text)

    @staticmethod
    def Step(text):
        return "    {0}".format(text)

    @staticmethod
    def Action(text):
        return "      {0}".format(text)
