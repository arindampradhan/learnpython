import ConfigParser


def update(PROBLEM):
    Config = ConfigParser.ConfigParser()
    conf_file = open("config.ini",'w')
    Config.add_section('Problems')
    Config.set('Problems','PROBLEM',PROBLEM)
    Config.write(conf_file)
    conf_file.close()

def get_problem():
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    PROBLEM = Config.get('Problems','PROBLEM')
    return PROBLEM