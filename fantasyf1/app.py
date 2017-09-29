from flask import Flask, render_template
from werkzeug.contrib.cache import SimpleCache

import ergast.api
import media.formula1
import media.wikipedia

app = Flask(__name__)
app.jinja_env.auto_reload = True

ergast = ergast.api.Client()

cache = SimpleCache()

@app.route('/')
def index():
    driver_standings = cache.get('driver_standings')
    if driver_standings is None:
        data = ergast('f1/current/driverStandings')
        driver_standings = data['StandingsTable']['StandingsLists'][0]['DriverStandings']
        for ds in driver_standings:
            name = '{} {}'.format(ds['Driver']['givenName'], ds['Driver']['familyName'])
            ds['flag_image'] = media.formula1.driver_flag_image(name)
            ds['image'] = media.formula1.driver_profile_image(name)
        cache.set('driver_standings', driver_standings)
    return render_template('driver_standings.html', driver_standings=driver_standings)

@app.route('/constructors')
def constructors():
    constructors = cache.get('constructors')
    if constructors is None:
        constructors = ergast('f1/current/constructors')['ConstructorTable']['Constructors']
        for constructor in constructors:
            if 'url' in constructor:
                constructor['image'] = media.wikipedia.infobox_image(constructor['url'])
        cache.set('constructors', constructors)
    return render_template('constructors.html', constructors=constructors)

@app.route('/drivers')
def drivers():
    drivers = cache.get('drivers')
    if drivers is None:
        drivers = ergast('f1/current/drivers')['DriverTable']['Drivers']
        for driver in drivers:
            if 'url' in driver:
                driver['image'] = media.wikipedia.infobox_image(driver['url'])
        cache.set('drivers', drivers)
    return render_template('drivers.html', drivers=drivers)
