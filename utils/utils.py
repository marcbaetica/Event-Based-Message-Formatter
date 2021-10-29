from utils.formatter import Decoder


def print_notification(subscriber_name, producer_name, message, encoding=None):
    decoded_message = Decoder.format_message(message, encoding) if encoding else message
    print(f'[{subscriber_name}] received message from [{producer_name}]: "{decoded_message}"')
