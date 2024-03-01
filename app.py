from flask import *
from peewee import fn
from flask_peewee.db import Database

app = Flask(__name__)
# no idea why it doesn't use the PORT in config.py
app.config.from_pyfile('config.py')
db = Database(app)

from models import Album, Artist, Customer, Employee, Genre, Invoice, MediaType, Playlist, Track, PlaylistTrack, InvoiceItem


@app.route('/')
@app.route('/<int:number>')
def index(number=-1):
  return render_template('index.html', number=number)


@app.route('/track/<int:track_id>')
def track(track_id):
  track = Track.get(Track.track_id == track_id)
  return render_template('track.html', track=track)


@app.route('/employee/<int:employee_id>')
def employee(employee_id):
  employee = Employee.get(Employee.employee_id == employee_id)
  return render_template('employee.html', employee=employee)


@app.route('/genres')
def genres():
  genres = Genre.select()
  genre_map = {}
  for genre in genres:
    x = Track.select().where(Track.genre == genre).count()
    genre_map[genre.name] = x
  print(len(genre_map))
  return render_template('genres.html', genres=genres, genre_map=genre_map)


@app.route('/invoice/<int:invoice_id>')
def invoice(invoice_id):
  invoice = Invoice.get(Invoice.invoice_id == invoice_id)
  invoice_items = InvoiceItem.select().where(InvoiceItem.invoice == invoice)
  return render_template('invoice.html',
                         invoice=invoice,
                         invoice_items=invoice_items)
