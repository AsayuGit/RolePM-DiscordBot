import logging

class log():
    def __init__(self):
        self.logger = logging.getLogger("BotLogger")
        
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        
        fileHandler = logging.FileHandler("log.log", mode="a", encoding="utf-8", delay=None)
        fileHandler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)-8s %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )

        consoleHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)

        self.logger.addHandler(consoleHandler)
        self.logger.addHandler(fileHandler)

    def setVerbose(self, value: bool):
        if (value):
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.NOTSET)

    def debuglog(self, message: str):
        self.logger.debug(message)

    def infolog(self, message: str):
        self.logger.info(message)

    def warninglog(self, message: str):
        self.logger.warning(message)

    def errorlog(self, message: str):
        self.logger.error(message)

    def criticallog(self, message: str):
        self.logger.critical(message)