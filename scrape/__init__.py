import requests
import arrow
from bs4 import BeautifulSoup

def get_course(course):
    return BeautifulSoup(requests.get('http://timeplan.uia.no/swsuiah/XMLEngine/default.aspx?ModuleByWeek&' +
                                      'p1=;{}-1;&p2=32;33;34;35;36;37;38;39;'.format(course) +
                                      '40;41;42;43;44;45;46;47;48;49;50;51').text, 'lxml')

def get_timetable(courses):
    soups = []
    for course in courses:
        soups.append(get_course(course)) # populate our list with each course's timetable

    weeks = {}
    for soup in soups[0].find_all('table'):
        week = int(soup.find('td').text.split(' ')[1][:-1]) # get the current week number
        weeks[week] = [] # initialize each week in our weeks dictionary

    for soup in soups:
        for x in soup.find_all('table'): # each table is a week
            week = int(x.find('td').text.split(' ')[1][:-1]) # return of the hacky integer
            tr2 = x.find_all(class_='tr2') # tr2 is the class that has all the "real" data
            for entry in tr2:
                data = {}
                z = entry.find_all('td') # each td has a set format with important data
                data['datetime'] = arrow.Arrow.strptime(
                                      '{} {}'.format(z[1].text, z[2].text.split('-')[0]),
                                      '%d %b %H.%M') # we need an Arrow object to sort nicely
                data['weekday'] = z[0].text
                data['date'] = z[1].text
                data['time'] = z[2].text
                data['details'] = z[3].text
                data['location'] = z[4].text
                data['lecturer'] = z[5].text
                weeks[week].append(data) # append our data to the appropriate week
    for x in list(weeks):
        if x < arrow.utcnow().to('Europe/Oslo').isocalendar()[1]:
            weeks.pop(x) # remove all past weeks
        else:
            weeks[x] = sorted(weeks[x], key=lambda y: y['datetime'])
    return weeks
