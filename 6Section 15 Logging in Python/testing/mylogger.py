import logging

# Remove all existing handlers
# for handler in logging.root.handlers[:]:
#     logging.root.removeHandler(handler)

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S:'
)


# logging.debug('this is a logging msg')
# logging.info('info')
# logging.warning('Warning')
# logging.error('Error')
# logging.critical('Critical')