'''
Created on 25 Mar 2018

@author: adam.green
'''
import datetime, logging


#logging.config.fileConfig('poe_tools_logging.conf')
#logger = logging.getLogger(__name__)
logger = logging.getLogger("poe_generic")
start_time = datetime.datetime.now()
logger.info("Staring CC Tools at "+str(start_time))
print(__name__)

if __name__ == '__main__':
    print("hello world")
    pass