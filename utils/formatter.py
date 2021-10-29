import csv


class Decoder:
    @classmethod
    def retrieve_formats_dictionary(cls, encoding):
        """Takes a type of conversion_dictionary as parameter and retrieves an conversion_dictionary dictionary.

        :param encoding: Encoding type to evaluate to. Acceptable values: 'Dec', 'Hex', 'Binary', 'HTML'
        :return: Dictionary representing the character conversion_dictionary in the format ascii: desired_encoding.
        """
        with open('conversion_dictionary/formatters_dict.csv', 'r') as f:
            encodings = csv.reader(f)
            headers = next(encodings)
            return {item[headers.index("Char")]: item[headers.index(encoding)] for item in encodings}

    @classmethod
    def format_message(cls, message, encoding):
        """Uses conversion_dictionary dictionary to convert ASCII characters from the message string into an conversion_dictionary of choice.

        :param message: The message to encode as a string of ASCII characters.
        :param encoding: Encoding type to evaluate to. Acceptable values: 'Dec', 'Hex', 'Binary', 'HTML'
        :return: The encoded message as a sting.
        """
        encoding = cls.retrieve_formats_dictionary(encoding)
        return ''.join([encoding[char] for char in message])
