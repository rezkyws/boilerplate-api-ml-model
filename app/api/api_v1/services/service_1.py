# module specific business logic (will be use for endpoints)
from ..load_models import models
from ....core.logging import logger


class ServiceOne:
    def __init__(self) -> None:
        pass

    def get_inference(self, text):
        try:
            # do something here
            text = models.the_model

            return text, 1, None
        
        except Exception as e:
            logger.error('error while getting something :', e, 'with input :', text)

            return '', 0, e