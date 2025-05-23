from mylogger import logging

def add(a, b):
    logging.debug(f'addition is taking place between {a} and {b}')
    c = a+b
    logging.debug(f'addition is successfully done.. (between {a} and {b})')

    return c

add(13,54)
