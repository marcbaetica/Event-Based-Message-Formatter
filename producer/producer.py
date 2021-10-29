class Producer:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def broadcast(self, message):
        [subscriber.format(message, self.name) for subscriber in self.subscribers]
