from flask import Flask, render_template
from uia import scrape, unidata
import arrow

app = Flask(__name__)

@app.route('/timeplan/')
def select_schedule():
    return render_template('select.html', names=unidata.s, courses=unidata.studies)

@app.route('/timeplan/<study>')
def load_schedule(study):
    try:
        p = scrape.get_pickle(study)
    except:
        abort(404)
    return render_template('timetable.html', weeks=p['timetable'], studytitle=p['title'])


if __name__ == '__main__':
    app.run('0.0.0.0', port=3000, debug=True)
