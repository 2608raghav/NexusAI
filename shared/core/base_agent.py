from shared.logging.logger import logger


class BaseAgent:

    def __init__(
        self,
        name: str,
        version: str
    ):

        self.name = name

        self.version = version

        logger.info(
            f"{self.name} initialized."
        )

    def health(self):

        return {

            "agent": self.name,

            "version": self.version,

            "status": "healthy"

        }