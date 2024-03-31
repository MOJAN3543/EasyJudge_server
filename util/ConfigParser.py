import configparser

def read():
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    return parser