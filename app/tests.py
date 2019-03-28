import unittest
import requests
from Crawl_libraries import Crawl_libraries
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_if_search_url_works(self, search_term='cars'):
        SEARCH_URL = f'http://www.google.com/search?q={search_term}'
        request = requests.get(SEARCH_URL)

        self.assertIs(request.status_code, 200)

    def test_os_platform(self):
        linux = 'posix'
        windows = 'nt'

        self.assertEquals(os.name , linux)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()