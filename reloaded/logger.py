import os
import logging

file_path = os.path.join(os.path.expanduser('~'), 'reloaded.log')


logger = logging.getLogger()
hdlr = logging.FileHandler(file_path)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
