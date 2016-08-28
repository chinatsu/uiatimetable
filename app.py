from flask import Flask, render_template
import scrape
import arrow

app = Flask(__name__)
app.config["response"] = scrape.get_timetable(['IS-100', 'IS-104', 'IS-109', 'IS-111']) # initialize response
app.config['timestamp'] = arrow.now() # set a timestamp, i like arrow because it's easy

@app.route('/timeplan/')
def load_schedule():
    if app.config['timestamp'] < arrow.now().replace(hours=-6):
        app.config["response"] = scrape.get_timetable(['IS-100', 'IS-104', 'IS-109', 'IS-111'])
        app.config['timestamp'] = arrow.now()
    return render_template('timetable.html', weeks=app.config['response']) # render the response!

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000, debug=True)
