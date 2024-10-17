# Configuração de log
import logging


class Log:

    def __init__(self, mailsender_id):

        self.mailsender_id = mailsender_id

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"logs/{mailsender_id}/app.log")
            ]
        )

        self.logger = logging.getLogger(__name__)

    def post_log(self, message, grade):
        try:
            if grade == "info":
                return self.logger.info(message)
            elif grade == "erro":
                return self.logger.error(message)
            elif grade == "critical":
                return self.logger.critical(message)

        except Exception as e:
            print(f"ocorreu um erro ao gerar os logs: {e}")
