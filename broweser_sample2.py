import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, deinit


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

def save_page(file_name, text):
        deinit()
        with open(file_name, 'w+') as out_file:
            out_file.write(text)

def print_page(file_name):
    with open(file_name) as in_file:
        print(in_file.read())


def get_page(url):
    r = requests.get(url)
    r.raise_for_status()
    return r


def parse_html(req):
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a',
            'ul', 'li', 'ol']
    soup = BeautifulSoup(req.content, 'html.parser')
    text = []
    for tag in tags:
        tag_list = soup.select(tag)
        for elem in tag_list:
            if elem.name == 'a':
                print(Fore.BLUE + elem.text)
                text.append(elem.get_text())
            else:
                print(Fore.WHITE + elem.text)
                text.append(elem.get_text())
    return ''.join(text)



def browser():
    history = []
    while True:
        url = input().lower()
        if url == "exit":
            exit()
        elif url == "back":
            try:
                history.pop()
            except IndexError:
                pass
        else:
            history.append(url[0:len(url) - max(0, url[::-1].find(".") + 1)])
            if not url.startswith('https://'):
                url = 'https://' + url
            if url.endswith('com'):
                if url[-4] != '.':
                    url = '.'.join([url[:-3], url[-3:]])
            if not (url.endswith('.com') or url.endswith('.org')):
                url = url + '.com'
            file_name = dirName + "/" + history[-1] + ".txt"
            # print if file exists
            if os.path.isfile(file_name):
                print_page(file_name)
            if not os.path.isfile(file_name):
                request = get_page(url)
                init()
                parse = parse_html(request)
                save_page(file_name, parse)
                print_page(file_name)


# set directory, initiate browser
args = sys.argv

if len(args) != 2:
    print("The script should be called with one argument: the name of the directory to store web pages as files.")
else:
    dirName = args[1]
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    browser()