try:
    import ConfigParser as configparser
except ImportError:
    import configparser

import mock
import sys
sys.path.append('../src')
import unittest

import main

class InitLogger(unittest.TestCase):

    @mock.patch('main.logging.config')
    def test_ioerr_is_raised_if_no_logging_file(self, mock_logging):
        mock_logging.fileConfig.side_effect = configparser.NoSectionError('foo')

        self.assertRaises(IOError, main.init_logging)

if __name__ == '__main__':
    unittest.main()
