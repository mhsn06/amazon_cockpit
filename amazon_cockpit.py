#!/root/amazon_stock_hunter/amazon_hunter_script/amazon_cockpit/amazon_cockpit/bin/python

import time
from subprocess import call

"""
Menu Items
"""


menu_items = ["Quit",
              "Start",
              "Pause ",
              "Resume",
              "Stop",
              "Get Status"
              "Show Live"]

welcome_message = "*** Welcome to the cockpit of amazon scraper ***"
farewell_message = "*** Landing the bird... Thanks for flying ***"
primary_instruction  = "Please enter the number indicated on the left of the expected Action."              
    
def print_menu_items(menu_items):
    """
    Prints the action items from an array of strings
    """
    for i, mi in enumerate(menu_items):
        print str(i) + " : " + mi
          
def select_menu():
    """
    shows menu and provide option to select menu
    """
    selection = None
    while True:
        print_menu_items(menu_items)
        try:
            print primary_instruction
            selection=int(raw_input('Enter your choice here: '))
            
            if selection >= 0 and selection < len(menu_items):
                return selection
            raise Exception
        except:
            print "\nERROR: Invalid input.\n"

            
def start_scraper():
    print "starting the scraper"
        #todo start the scraper
    
    call(["systemctl", "start", "amazon.service"])

    print "scraper started"
    

def pause_scraper():
    pass

def stop_scraper():
    call(["systemctl", "stop", "amazon.service"])

def resume_scraper():
    pass

def show_live():
    pass

def get_scraper_status():
    call(["systemctl", "status", "amazon.service"])
            
while True:
    print welcome_message
    
    selection = select_menu()
    
    if selection == 0:
        print farewell_message
        break
    elif selection == 1:
        start_scraper()
    elif selection == 4:
        stop_scraper()
    elif selection == 5:
        get_scraper_status()
    else:
        print "you have selected " +  menu_items[selection]
    