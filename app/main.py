from Crawl_libraries import Crawl_libraries
import sys, os
from collections import OrderedDict

sep = '=' * 20


def menu():
    clear()
    """ Show Main """
    choice = None
    while choice != 'q':
        print('Enter q to exit')
        for key, value in menu_loop.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Choice: ').lower().strip()
        
        if choice == 'q':
            print(sep)
            print('Bye :)')
            break

        if choice in menu_loop:
            menu_loop[choice]()
        else:
            print('Wrong input.'.center(20, ' '))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_program():
    '''Run web crawler program '''
    clear()

    print('Please enter a search term and then press [Enter].')
    search_term = input('# ')
    choice = None
    cl = Crawl_libraries(search_term)
    
    clear()
    while choice != 'q':
        print('Enter q to return to main.')
        for key, value in sub_menu_loop.items():
            print('{}) {}'.format(key, value.__doc__))

        choice = input('Choice: ').lower().strip()
        print(sep)

        if choice == 'q':
            clear()
            break

        if choice in sub_menu_loop:
            sub_menu_loop[choice](cl)
            
# Main menu.
menu_loop = OrderedDict([
    ('1', run_program)
])

def search_top_five_libraries(obj):
    '''Search top 5 most used libraries'''
    obj.get_top_five_libraries()

def print_links_from_searched_page(obj):
    '''Print searched results links'''
    print('Search term result links:', end='\n\n')
    for i, link in enumerate(obj.extract_main_result_links_from_page(), start=1):
        print(f'{i}) {link}')
    print(sep, end='\n\n')

def print_downloaded_page(obj):
    '''Print the results page'''
    print(obj.get_google_search_page())
    print(sep, end='\n\n')

# Sub menu
sub_menu_loop = OrderedDict([
    ('1', search_top_five_libraries),
    ('2', print_links_from_searched_page),
    ('3', print_downloaded_page)
])

if __name__ == "__main__":
    menu()