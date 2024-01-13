import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - [%(name)s] - %(levelname)s: %(message)s")

# info 信息输出到文件
infoRotatingHandler = RotatingFileHandler(maxBytes=20 * 1024 * 1024, backupCount=10, filename=f'info.log', encoding='utf8')
infoRotatingHandler.setFormatter(formatter)
infoRotatingHandler.setLevel(logging.INFO)
logger.addHandler(infoRotatingHandler)

# error 信息输出到文件
errorRotatingHandler = RotatingFileHandler(maxBytes=20 * 1024 * 1024, backupCount=10, filename=f'error.log', encoding='utf8')
errorRotatingHandler.setFormatter(formatter)
errorRotatingHandler.setLevel(logging.ERROR)
logger.addHandler(errorRotatingHandler)

# console 输出
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.setLevel(logging.INFO)
