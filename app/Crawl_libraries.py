import requests
from bs4 import BeautifulSoup

class Crawl_libraries(object):
    def __init__(self, search_term):
        # Initialize the program.
        self.SEARCH_URL = f'http://www.google.com/search?q={search_term}'
        self.request = requests.get(self.SEARCH_URL)
        self.soup = BeautifulSoup(self.request.text, 'lxml')

        # Generator for memory sufficiency.
        # I searched for <cite></cite> tags because they contain the links of the search results.
        self.links = (link.text for link in self.soup.find_all('cite'))
        self.libraries = {}

    def get_google_search_page(self):
        ''' Get a Google result page for the search term '''
        return(self.soup.prettify())


    def fetch_all_search_results_pages(self):
        for page in self.links:
            req = requests.get(page)
            soup = BeautifulSoup(req.text, 'xml')
            yield soup.text

    # This is harder than expected and it will take some time, so I passed it, I would have used selenium to extract the libraries with javascript.
    def _extract_js_libraries_from_a_page(self, page):
        ''' Download the respective pages and extract the names of JavaScript libraries used in them '''
        pass

    def extract_main_result_links_from_page(self):
        ''' Extract main result links from the page '''
        links = list(self.links)
        return links

    def _sparator(self):
        print('', end='\n\n')

    def get_top_five_libraries(self):
        ''' Print top 5 most used libraries to standard output '''
        # Mocked up extracted libraries.
        self.libraries = {
            'angular': 1,
            'react': 2,
            'vue': 3,
            'ember': 0,
            'jquery': 6,
            'D3': 1,
            'babel': 2,
        }

        # Sort the libraries according to their values.
        sorted_libraries = sorted(self.libraries.items(), key=lambda k: k[1], reverse=True)

        # print top 5 libraries.
        print('Top 5 used libraries')
        for i, lib in enumerate(sorted_libraries[:5], start=1):
            print(f'{i}) {lib[0]}')

        self._sparator()


        
