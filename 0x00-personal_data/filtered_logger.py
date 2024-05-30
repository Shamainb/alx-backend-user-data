#!/usr/bin/env python3
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        def filter_datum(datum):
            return self.REDACTION if datum in self.fields else datum


def filter_datum(fields, redaction, message, separator):
    """
    Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character
    is separating all fields in the log line (message)
    """
    pattern = f'({separator})({"|".join(fields)})(?={separator}|$)'
    return re.sub(pattern, f'\\1{redaction}', message)
