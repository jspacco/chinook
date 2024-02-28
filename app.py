from flask import *
from peewee import fn
from flask_peewee.db import Database

app = Flask(__name__)
# no idea why it doesn't use the PORT in config.py
app.config.from_pyfile('config.py')
db = Database(app)

from models import Album, Artist, Customer, Employee, Genre, Invoice, MediaType, Playlist, Track, PlaylistTrack

@app.route('/')
@app.route('/<int:number>')
def index(number=-1):
    return render_template('index.html', number=number)


@app.route('/track/<int:track_id>')
def track(track_id):
    track = Track.get(Track.track_id == track_id)
    #print(track.name)
    #print(track.album.artist.name)
    #print(f'playlist track: {PlaylistTrack.get(PlaylistTrack.playlist == 1, PlaylistTrack.track == 3402)}')
    return render_template('track.html', track=track)

@app.route('/employee/<int:employee_id>')
def employee(employee_id):
    employee = Employee.get(Employee.employee_id == employee_id)
    print(employee.first_name)
    print(employee.email)
    return render_template('employee.html', employee=employee)


if __name__ == '__main__':
    print("Why doesn't this work?")
    app.run(debug=True, port=8080)