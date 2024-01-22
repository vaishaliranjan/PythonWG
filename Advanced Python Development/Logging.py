import logging
#This decides the basic level of the logging level
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)s] : %(message)s",level=logging.DEBUG, filename="logs.txt")
logger= logging.getLogger("test_logger")
logger.debug("This will not show up")
logger.info("This will not show up too")
logger.warning("This will show up")
logger.error("This will show up too")
logger.critical("This will show up tooooo")
'''
DEBUG
INFO
WARNING
ERROR
CRITICAL
'''

