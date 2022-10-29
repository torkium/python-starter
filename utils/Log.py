import logging
from datetime import datetime
import os
# Classe de gestion des logs
class Log:

    def init(root_folder):
        Log.ROOT_FOLDER = root_folder
        Log.LOG_FILES = {
            logging.DEBUG: datetime.now().strftime(
                root_folder + "logfilee_%Y_%m_%d_%H_%M_%S_DEBUG.log"
            ),
            logging.INFO: datetime.now().strftime(
                root_folder + "logfilee_%Y_%m_%d_%H_%M_%S_INFO.log"
            ),
            logging.ERROR: datetime.now().strftime(
                root_folder + "logfilee_%Y_%m_%d_%H_%M_%S_ERROR.log"
            ),
            logging.WARNING: datetime.now().strftime(
                root_folder + "logfilee_%Y_%m_%d_%H_%M_%S_WARNING.log"
            ),
            "ALL": datetime.now().strftime(root_folder + "logfilee_%Y_%m_%d_%H_%M_%S.log"),
    }

    formatLOG = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    def insert(text, level=logging.INFO):
        os.makedirs(Log.ROOT_FOLDER, exist_ok=True)
        infoLog = logging.FileHandler(Log.LOG_FILES[level], encoding="UTF-8")
        infoLog.setFormatter(Log.formatLOG)
        logger = logging.getLogger(Log.LOG_FILES[level])
        logger.setLevel(level)
        infoLogAll = logging.FileHandler(Log.LOG_FILES["ALL"], encoding="UTF-8")
        infoLogAll.setFormatter(Log.formatLOG)
        loggerAll = logging.getLogger(Log.LOG_FILES["ALL"])
        loggerAll.setLevel(level)

        if not logger.handlers:
            logger.addHandler(infoLog)
            loggerAll.addHandler(infoLogAll)
            if level == logging.INFO:
                logger.info(text)
                loggerAll.info(text)
            if level == logging.ERROR:
                logger.error(text)
                loggerAll.error(text)
            if level == logging.DEBUG:
                logger.debug(text)
                loggerAll.debug(text)
            if level == logging.WARNING:
                logger.warning(text)
                loggerAll.warning(text)
        infoLog.close()
        infoLogAll.close()
        logger.removeHandler(infoLog)
        loggerAll.removeHandler(infoLogAll)
        return