from googlesearch import search
import requests
from lxml.html import fromstring   
import re 

errors = ['Page Not Found', '403 Forbidden', 'ERROR: The request could not be satisfied', 'Access to this page has been denied.', 'Access Denied', '404 Error (Page not found)']

def gsearch(message, start, number,language):
    def Link_title(URL):
        r = requests.get(URL)
        content = r.content
        try:
            tree = fromstring(content.decode())
        except:
            tree = fromstring(content)
        last = tree.findtext('.//title')
        return str(last)
    
    def titleforerror(j, links):
        s = j.split('.')
        if 'www' in s[0]:
            link = s[1]
        else:
            link = re.findall(r'https://[\'"]?([^\'" >]+)', s[0])
            link = link[0]
        links = '\n'+links +"№" + str(number) +" "+ link.title() + '\n' + str(j) + '\n'
        return links

    name = message
    links = ''
    number = number 
    for j in search(name, tld="co.in",  num=10, start = start, stop=10, pause=2.0): 

        try:
            if Link_title(j) == 'None' or Link_title(j) in errors:
                links = str(titleforerror(j, links))
            else:
                title = re.sub('\n', '',Link_title(j))
                links = '\n'+links +"№" + str(number) +" "+ title + '\n' + str(j) + '\n'
            number+=1
        except:
            print('Виникла помилка в парсингу назви сайту')
            links = str(titleforerror(j,links))
            number+=1
    if not links:
        return ('😢 Сформуйте будь ласка запит іншим чином.\nНа запит {} не знайдено жодного посилання.' if language == 'ukrainian' else '😢 Please formulate the query differently.\nNo link was found for query {}.').format(name)
    return links

