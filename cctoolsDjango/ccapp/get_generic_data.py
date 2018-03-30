'''
Created on 25 Mar 2018

@author: adam.green
'''
import datetime, time, logging
import xlrd # for excel workbooks
###
### So we can use our django models here in this script
###
import sys, os
#from poetools_project.poe.common.character_tools import logger
proj_path = '/home/adam/workspace1/CCTools/cctoolsDjango'
#proj_path = '/Users/adam.green/Documents/workspace/cc-tools-pydev/cctoolsDjango'


# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cctoolsDjango.settings")
sys.path.append(proj_path)
# This is so my local_settings.py gets loaded.
os.chdir(proj_path)
# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from ccapp.models import Weapon, ValidGame


#logging.config.fileConfig('poe_tools_logging.conf')
#logger = logging.getLogger(__name__)
logger = logging.getLogger("cc_generic")
print("logger", logger.handlers, logger.level)
start_time = datetime.datetime.now()
logger.warn("Starting CC Tools at "+str(start_time))
print(__name__)

def upload_weapons():
    logger.warn("entering upload_weapons ",)
    for valid_game in ValidGame.objects.all():
        print(valid_game.name)
        fname = os.path.join(os.path.dirname(
                                             os.path.dirname(
                                                os.path.abspath(__file__))
                                                ),
                                            'cctoolsDjango/cctoolsDjango/data',
                                            valid_game.generic_data
                                            )
        print("fname", fname)
        xl_workbook = xlrd.open_workbook(fname)
        sheet_names = xl_workbook.sheet_names()
        print('Sheet Names', sheet_names)
        #logger.warn("importing data for ", valid_game.name())

def set_valid_games():
    VALID_GAMES = [{"name": "Panthers in the Fog",
                    "short_name": "PiTF", 
                    "generic_data": "Close Combat Panthers in the Fog Data Workbook v01.xlsm"}
                   ,]
    print("Valid Games ", VALID_GAMES)
    for x in VALID_GAMES:
        print("x ", x['name'])
        y = ValidGame(
                      name = x['name'],
                      short_name = x['short_name'],
                      generic_data = x["generic_data"]
                      )
        print("y ",y)
        y.save()

if __name__ == '__main__':
    pass
    print("hello world")
    logger.warn("log test ",)
    set_valid_games()
    upload_weapons()
    #print (logging.handlers) 
    pass