import ConfigParser
import os
import settings

BASE_DIR = settings.BASE_DIR

def update(PROBLEM):
    Config = ConfigParser.ConfigParser()
    conf_file = open(os.path.join(BASE_DIR,"config.ini"),'w')
    Config.add_section('Problems')
    Config.set('Problems','PROBLEM',PROBLEM)
    Config.write(conf_file)
    conf_file.close()

def get_problem():
    Config = ConfigParser.ConfigParser()
    Config.read(os.path.join(BASE_DIR,"config.ini"))
    PROBLEM = Config.get('Problems','PROBLEM')
    return PROBLEM