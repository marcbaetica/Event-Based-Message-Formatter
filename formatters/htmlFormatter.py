from utils.utils import print_notification


class HtmlFormatter:
    def __init__(self, name):
        self.name = name

    def subscribe(self, producer):
        producer.subscribe(self)

    def format(self, message, producer):
        print_notification(self.name, producer, message, 'HTML')