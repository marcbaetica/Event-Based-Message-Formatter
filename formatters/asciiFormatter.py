from utils.utils import print_notification


class ASCIIFormatter:
    def __init__(self, name):
        self.name = name

    def subscribe(self, producer):
        producer.subscribe(self)

    def format(self, message, producer_name):
        print_notification(self.name, producer_name, message)

