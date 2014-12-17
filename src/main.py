try:
    import ConfigParser as configparser
except ImportError:
    import configparser
import datetime
import logging.config

import pandas.io.data as web
log = logging.getLogger(__name__)

def init_logging():
    try:
        logging.config.fileConfig('logging.ini')
    except configparser.NoSectionError:
        raise IOError('nao')

if __name__ == '__main__':
    
    init_logging()
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2013, 1, 27)

    f = web.DataReader("F", 'yahoo', start, end)
    values = f.columns.values.tolist()
