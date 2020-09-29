import sys
import os
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import init, Fore, deinit

def create_directory():
    args = sys.argv
    try:
        directory = args[1]
        # create directory if there's arg and directory doesn't exist already
        if len(directory) > 0 and not os.path.exists(directory) :
            os.mkdir(directory)
        return directory
    except IndexError:
        print("The script should be called with 1 argument - the name of directory")
        exit()


def check_validity(answer):
    return answer.find('.') != -1

def truncate_filename(name):
    # name = name[:name.find(".")]  # get rid of .com, .org after .
    # return name
    # # or another way to truncate
    parts = name.split(".")  # split into two parts
    if len(parts) != 1:
        name = ".".join(parts[:-1])
    else:
        name = name
    return name

def display_file(path):
    try:
        with open(path) as file:
            print(file.read())
    except FileNotFoundError:
        print(f'File {path} does not exist')

def save_file(path, text):
    with open(path, 'w+') as out_file:
        out_file.write(text)
        print(path, " saved.")

def get_page(url):
    r = requests.get(url)
    r.raise_for_status()
    return r

def process_url(url):
    if not url.startswith('https://') :
        url = 'https://' + url
    return url

def parse_html(req):
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a',
            'ul', 'li', 'ol']
    soup = BeautifulSoup(req.content, 'html.parser')
    text = []
    for tag in tags:
        tag_list = soup.select(tag)
        for elem in tag_list:
            # print(elem.text)
            # text.append(elem.get_text())
            if elem.name == 'a':
                print(Fore.BLUE + elem.text)
                text.append(elem.get_text())
            else:
                print(Fore.WHITE + elem.text)
                text.append(elem.get_text())
    return ''.join(text)

def main():
    buttons = ['exit', 'back', 'quit', 'clear']
    valid_sites = ['bloomberg.com', 'nytimes.com']
    history = deque()

    directory = create_directory()

    while True :
        choice = input("What do you like to search? Exit to quit.  ").lower()

        if choice in buttons:

            if (choice == "exit") or (choice == "quit"):
                exit()

        # if back, display prev page
            if choice == "back":
                try:
                    current_path = history.pop()
                    prev_path = f'{directory}/{history[-1]}.txt'
                    #prev_path = f'{directory}/{prev_page}.txt'
                    display_file(prev_path)
                   # history.append(prev_page)
                except IndexError:
                    print("History is clear.")
                    pass  # silent error

            if choice == 'clear':
                pass

        else:
            # if file already exists, then display contents
            path = f'{directory}/{choice}.txt'
            if os.path.isfile(path):
                display_file(path)
                history.append(truncate_filename(choice))
            else:
                if check_validity(choice):
                    url = process_url(choice)
                    page = get_page(url)
                    init()  # initialize colorama
                    parse = parse_html(page)
                    short_name = truncate_filename(choice)

                    path = f'{directory}/{short_name}.txt'
                    save_file(path, parse)
                    display_file(path)
                    history.append(truncate_filename(choice))
                # otherwise URL itself is not valid
                else:
                    print("error 1 - URL is not valid.  needs .")

import sys
import os
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import init, Fore, deinit

def create_directory():
    args = sys.argv
    try:
        directory = args[1]
        # create directory if there's arg and directory doesn't exist already
        if len(directory) > 0 and not os.path.exists(directory) :
            os.mkdir(directory)
        return directory
    except IndexError:
        print("The script should be called with 1 argument - the name of directory")
        exit()


def check_validity(answer):
    return answer.find('.') != -1

def truncate_filename(name):
    # name = name[:name.find(".")]  # get rid of .com, .org after .
    # return name
    # # or another way to truncate
    parts = name.split(".")  # split into two parts
    if len(parts) != 1:
        name = ".".join(parts[:-1])
    else:
        name = name
    return name

def display_file(path):
    try:
        with open(path) as file:
            print(file.read())
    except FileNotFoundError:
        print(f'File {path} does not exist')

def save_file(path, text):
    with open(path, 'w+') as out_file:
        out_file.write(text)
        print(path, " saved.")

def get_page(url):
    r = requests.get(url)
    r.raise_for_status()
    return r

def process_url(url):
    if not url.startswith('https://') :
        url = 'https://' + url
    return url

def parse_html(req):
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a',
            'ul', 'li', 'ol']
    soup = BeautifulSoup(req.content, 'html.parser')
    text = []
    for tag in tags:
        tag_list = soup.select(tag)
        for elem in tag_list:
            # print(elem.text)
            # text.append(elem.get_text())
            if elem.name == 'a':
                print(Fore.BLUE + elem.text)
                text.append(elem.get_text())
            else:
                print(Fore.WHITE + elem.text)
                text.append(elem.get_text())
    return ''.join(text)

def main():
    buttons = ['exit', 'back', 'quit', 'clear']
    valid_sites = ['bloomberg.com', 'nytimes.com']
    history = deque()

    directory = create_directory()

    while True :
        choice = input("What do you like to search? Exit to quit.  ").lower()

        if choice in buttons:

            if (choice == "exit") or (choice == "quit"):
                exit()

        # if back, display prev page
            if choice == "back":
                try:
                    current_path = history.pop()
                    prev_path = f'{directory}/{history[-1]}.txt'
                    #prev_path = f'{directory}/{prev_page}.txt'
                    display_file(prev_path)
                   # history.append(prev_page)
                except IndexError:
                    print("History is clear.")
                    pass  # silent error

            if choice == 'clear':
                pass

        else:
            # if file already exists, then display contents
            path = f'{directory}/{choice}.txt'
            if os.path.isfile(path):
                display_file(path)
                history.append(truncate_filename(choice))
            else:
                if check_validity(choice):
                    url = process_url(choice)
                    page = get_page(url)
                    init()  # initialize colorama
                    parse = parse_html(page)
                    short_name = truncate_filename(choice)

                    path = f'{directory}/{short_name}.txt'
                    save_file(path, parse)
                    display_file(path)
                    history.append(truncate_filename(choice))
                # otherwise URL itself is not valid
                else:
                    print("error 1 - URL is not valid.  needs .")



if __name__ == '__main__':
    main()



if __name__ == '__main__':
    main()

