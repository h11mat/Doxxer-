import sys
import os
import time
import signal
import webbrowser

print("\033]0;Spy Dox Tracker\007")

def signal_handler(signal, frame):
    clear_screen()
    display_logo()
    print(' [\033[32mX] You pressed Ctrl+C!')
    time.sleep(2)
    exit_menu()

signal.signal(signal.SIGINT, signal_handler)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    clear_screen()
    print("""\033[32m

                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣤⣤⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⢀⣀⣠⠀⣶⣤⣄⣉⣉⣉⣉⣠⣤⣶⠀⣄⣀⡀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⣶⣾⣿⣿⣿⣿⣦⣄⣉⣙⣛⣛⣛⣛⣋⣉⣠⣴⣿⣿⣿⣿⣷⣶⠀⠀⠀
                            ⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣆⠀⠀⠀⢠⡄⠀⠀⠀⣰⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢀⣠⣶⣾⣿⡆⠸⣿⣶⣶⣾⣿⣿⣷⣶⣶⣿⠇⢰⣿⣷⣶⣄⡀⠀⠀⠀
                            ⠀⠀⠺⠿⣿⣿⣿⣿⣿⣄⠙⢿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣿⣿⣿⣿⣿⠿⠗⠀⠀
                            ⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣷⡄⠈⠙⠛⠛⠋⠁⢠⣾⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣀⣤⣬⣿⣿⣿⣇⠐⣿⣿⣿⣿⠂⣸⣿⣿⣿⣥⣤⣀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠘⠻⠿⠿⢿⣿⣿⣿⣧⠈⠿⠿⠁⣼⣿⣿⣿⡿⠿⠿⠟⠃⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⠀⣶⣦⠀⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     Dox Tracker By Spy Discord: @root.spy Server : https://discord.gg/5Xsr657yaF
     """)

MENU_OPTIONS = """
    1. Nom
    2. Numéro de Téléphone
    3. Mort
    4. Adresse IP
    99. About
    0. Exit
"""

TRACKER_OPTIONS_NAME = """
    1. Pipl          10. Twitter
    2. Facebook      11. Beenverified
    3. Spokeo        12. Peoplelooker     
    4. Flickr        13. Myspace 
    5. Linkedin      14. Pagesjaunes   
    6. Google plus   15. Libramemoria
    7. Tumblr        16. Avis-de-deces     
    8. Youtube       00. All
    9. Peekyou       
==============================
    99. Back         0. Exit
"""

TRACKER_OPTIONS_PHONE = """
    1. Okcaller        
    2. Facebook     
    3. France-inverse   
    4. Whitepages     
    5. Anywho             
    6. Canada411      
    7. Pagesjaunes       
    00. All
=========================
    99. Back         0. Exit
"""

TRACKER_OPTIONS_DECEASED = """
    1. Libramemoria  
    2. Avis-de-deces 
    3. Enmemoria 
    00. All
=============================
    99. Back         0. Exit
"""

TRACKER_OPTIONS_IP = """
    1. G-force 
    2. whatismyipaddress
    3. Whois
    00. All
==============================
    99. Back         0. Exit
"""

BASE_URLS = {
    'name': [
        'https://pipl.com/search/?q=',
        'https://www.facebook.com/search/top/?init=quick&q=',
        'https://www.spokeo.com/',
        'https://www.flickr.com/search/people/?username=',
        'https://fr.linkedin.com/pub/dir/',
        'https://plus.google.com/s/',
        'https://www.tumblr.com/search/',
        'http://www.youtube.com/results?search_query=',
        'https://www.peekyou.com/',
        'https://twitter.com/search?f=users&vertical=default&q=',
        'https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn=',
        'https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn=',
        'https://myspace.com/search?q=',
        'https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=',
        'http://www.libramemoria.com/avis/?Nom=',
        'https://www.avis-de-deces.net/avis/par-nom/?lastname=',
    ],
    'phone': [
        'http://www.okcaller.com/',
        'https://www.facebook.com/search/top/?init=quick&q=',
        'http://www.france-inverse.com/annuaire-inverse/',
        'https://www.whitepages.com/phone/',
        'https://www.anywho.com/phone/',
        'http://canada411.pagesjaunes.ca/fs/',
        'https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui=',
    ],
    'deceased': [
        'http://www.libramemoria.com/avis/?Nom=',
        'https://www.avis-de-deces.net/avis/par-nom/?lastname=',
        'http://enmemoria.lavanguardia.com/buscar?keywords=',
    ],
    'ip': [
        'https://www.g-force.ca/en/hosting/ip-whois?ip=',
        'http://whatismyipaddress.com/ip/',
        'https://dig.whois.com.au/ip/',
    ],
}

def menu():
    display_logo()
    time.sleep(1)
    print(MENU_OPTIONS)
    opt = input("  Select: ")
    if opt == "1":
        search_name()
    elif opt == "2":
        search_phone()
    elif opt == "3":
        search_deceased()
    elif opt == "4":
        search_ip()
    elif opt == "99":
        clear_screen()
        webbrowser.open('https://discord.gg/5Xsr657yaF')
        menu()
    elif opt == "0":
        exit_menu()
    else:
        display_error()

def search_name():
    search("name", TRACKER_OPTIONS_NAME, ["Name: ", "First name: "])

def search_phone():
    search("phone", TRACKER_OPTIONS_PHONE, ["Number: "])

def search_deceased():
    search("deceased", TRACKER_OPTIONS_DECEASED, ["Name: ", "First name: "])

def search_ip():
    search("ip", TRACKER_OPTIONS_IP, ["IP: "])

def search(category, options_text, prompts):
    clear_screen()
    display_logo()
    time.sleep(1)
    inputs = [input(prompt) for prompt in prompts]
    print(options_text)
    tracker = input("Dox Tracker:~\033[32m/$ ")
    handle_tracker_input(category, inputs, tracker)

def handle_tracker_input(category, inputs, tracker):
    if tracker.isdigit():
        idx = int(tracker) - 1
        if 0 <= idx < len(BASE_URLS[category]):
            webbrowser.open(BASE_URLS[category][idx] + ' '.join(inputs))
            time.sleep(2)
            menu()
        elif tracker == "00":
            for url in BASE_URLS[category]:
                webbrowser.open(url + ' '.join(inputs))
                time.sleep(2)
            menu()
        elif tracker == "99":
            menu()
        elif tracker == "0":
            exit_menu()
        else:
            display_error()
    else:
        display_error()

def display_error():
    clear_screen()
    display_logo()
    print("\033[32m[ERROR] selection invalid!")
    time.sleep(3)
    menu()

def exit_menu():
    clear_screen()
    display_logo()
    time.sleep(1)
    print(" Thanks for using Dox Tracker By Spy")
    time.sleep(2)
    print("[\033[32mX]...\033[1;32mClosing")
    time.sleep(1)
    clear_screen()
    sys.exit()

menu()
