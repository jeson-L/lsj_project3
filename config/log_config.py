import logging
from logging import handlers


def log_config():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)

    ls = logging.StreamHandler()
    lf = logging.handlers.TimedRotatingFileHandler(filename='./log/txl.log', when='h', backupCount=3, encoding='utf-8')

    fmt = '%(asctime)s 【%(filename)s %(funcName)s %(message)s】'
    formatter = logging.Formatter(fmt=fmt, datefmt='%Y-%m-%d %H:%M:%S')

    ls.setFormatter(formatter)
    lf.setFormatter(formatter)

    logger.addHandler(ls)
    logger.addHandler(lf)

    return logger
