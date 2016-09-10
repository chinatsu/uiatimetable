from uia import scrape, unidata
from time import sleep
import pickle
from os import path
from datetime import datetime
from dateutil.relativedelta import relativedelta

PICKLE_DIR = 'pickles/'
studies = unidata.studies

# lazy prototyping means infinite loops instead of cronjobs

while True:
    for study in studies:
        try:
            file_time = datetime.fromtimestamp(path.getmtime(PICKLE_DIR + study))
        except FileNotFoundError:
            file_time = datetime.fromtimestamp(0)
        if file_time < datetime.now() - relativedelta(hours=6):
            table = {'timetable': scrape.get_timetable(studies[study]['courses']),
                     'title': studies[study]['title']}
            with open(PICKLE_DIR + study, 'wb') as f:
                pickle.dump(table, f)
        print('pickled {}!'.format(studies[study]['title']))
    sleep(21600)
