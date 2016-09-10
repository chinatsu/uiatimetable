import pickle
import requests
import arrow
from dateutil import tz
from bs4 import BeautifulSoup

PICKLE_DIR = 'pickles/'

def get_course(course):
    return BeautifulSoup(requests.get('http://timeplan.uia.no/swsuiah/XMLEngine/default.aspx?ModuleByWeek&' +
                                      'p1=;{};&p2=32;33;34;35;36;37;38;39;'.format(course) +
                                      '40;41;42;43;44;45;46;47;48;49;50;51').text, 'lxml')

def get_timetable(courses):
    soups = []
    for course in courses:
        soups.append(get_course(course))

    weeks = {}
    for x in range(32, 52):
        weeks[x] = []
    for soup in soups:
        for x in soup.find_all('table'): # each table is a week
            week = int(x.find('td').text.split(' ')[1][:-1]) # return of the hacky integer
            tr2 = x.find_all(class_='tr2') # tr2 is the class that has all the "real" data
            for entry in tr2:
                data = {}
                z = entry.find_all('td') # each td has a set format with important data
                data['datetime'] = arrow.Arrow.strptime(
                                       '{} {} 2016'.format(z[1].text, z[2].text.split('-')[1]),
                                       '%d %b %H.%M %Y', tzinfo=tz.gettz('Europe/Oslo'))
                data['weekday'] = z[0].text
                data['date'] = z[1].text
                data['time'] = z[2].text
                data['details'] = z[3].text
                data['location'] = z[4].text
                data['lecturer'] = z[5].text
                weeks[week].append(data) # append our data to the appropriate week
    for x in list(weeks):
        if x < arrow.utcnow().to('Europe/Oslo').isocalendar()[1]:
            weeks.pop(x)
        else:
            weeks[x] = sorted(weeks[x], key=lambda y: y['datetime'])
    return weeks

def pickle_timetable(timetable, name):
    with open(PICKLE_DIR + name, 'wb') as f:
        pickle.dump(timetable, f)

def get_pickle(name):
    with open(PICKLE_DIR + name, 'rb') as f:
        return pickle.load(f)
