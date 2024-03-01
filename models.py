from peewee import *
from config import DATABASE

db = SqliteDatabase(DATABASE['name'])


# Base model class for common fields
class BaseModel(Model):

  class Meta:
    database = db


class Artist(BaseModel):
  artist_id = IntegerField(primary_key=True,
                           null=False,
                           column_name='ArtistId')
  name = CharField(max_length=120, null=False)

  class Meta:
    table_name = 'artists'


class Album(BaseModel):
  album_id = IntegerField(primary_key=True, null=False, column_name='AlbumId')
  title = CharField(max_length=160, null=False)
  artist = ForeignKeyField(Artist,
                           on_delete='NO ACTION',
                           on_update='NO ACTION',
                           null=False,
                           column_name='ArtistId')

  class Meta:
    table_name = 'albums'


class Employee(BaseModel):
  employee_id = IntegerField(primary_key=True,
                             null=False,
                             column_name='EmployeeId')
  last_name = CharField(max_length=20, null=False, column_name='LastName')
  first_name = CharField(max_length=20, null=False, column_name='FirstName')
  title = CharField(max_length=30, null=True)
  reports_to = ForeignKeyField(model='self',
                               on_delete='NO ACTION',
                               on_update='NO ACTION',
                               null=True,
                               column_name='ReportsTo')
  birth_date = DateTimeField(null=True, column_name='BirthDate')
  hire_date = DateTimeField(null=True, column_name='HireDate')
  address = CharField(max_length=70, null=True)
  city = CharField(max_length=40, null=True)
  state = CharField(max_length=40, null=True)
  country = CharField(max_length=40, null=True)
  postal_code = CharField(max_length=10, null=True, column_name='PostalCode')
  phone = CharField(max_length=24, null=True)
  fax = CharField(max_length=24, null=True)
  email = CharField(max_length=60, null=True)

  class Meta:
    table_name = 'employees'


class Customer(BaseModel):
  customer_id = IntegerField(primary_key=True,
                             null=False,
                             column_name='CustomerId')
  first_name = CharField(max_length=40, null=False, column_name='FirstName')
  last_name = CharField(max_length=20, null=False, column_name='LastName')
  company = CharField(max_length=80, null=True)
  address = CharField(max_length=70, null=True)
  city = CharField(max_length=40, null=True)
  state = CharField(max_length=40, null=True)
  country = CharField(max_length=40, null=True)
  postal_code = CharField(max_length=10, null=True)
  phone = CharField(max_length=24, null=True)
  fax = CharField(max_length=24, null=True)
  email = CharField(max_length=60, null=False)
  support_rep = ForeignKeyField(Employee,
                                on_delete='NO ACTION',
                                on_update='NO ACTION',
                                null=True,
                                column_name='SupportRep')

  class Meta:
    table_name = 'customers'


class Genre(BaseModel):
  genre_id = IntegerField(primary_key=True, null=False, column_name='GenreId')
  name = CharField(max_length=120, null=False)

  class Meta:
    table_name = 'genres'


class Invoice(BaseModel):
  invoice_id = IntegerField(primary_key=True,
                            null=False,
                            column_name='InvoiceId')
  customer = ForeignKeyField(Customer,
                             on_delete='NO ACTION',
                             on_update='NO ACTION',
                             null=False,
                             column_name='CustomerId')
  invoice_date = DateTimeField(null=False, column_name='InvoiceDate')
  billing_address = CharField(max_length=70,
                              null=True,
                              column_name='BillingAddress')
  billing_city = CharField(max_length=40, null=True, column_name='BillingCity')
  billing_state = CharField(max_length=40,
                            null=True,
                            column_name='BillingState')
  billing_country = CharField(max_length=40,
                              null=True,
                              column_name='BillingCountry')
  billing_postal_code = CharField(max_length=10,
                                  null=True,
                                  column_name='BillingPostalCode')
  total = DecimalField(max_digits=10, decimal_places=2, null=False)

  class Meta:
    table_name = 'invoices'


class MediaType(BaseModel):
  media_type_id = IntegerField(primary_key=True,
                               null=False,
                               column_name='MediaTypeId')
  name = CharField(max_length=120, null=False)

  class Meta:
    table_name = 'media_types'


class Track(BaseModel):
  track_id = IntegerField(primary_key=True, null=False, column_name='TrackId')
  name = CharField(max_length=200, null=False)
  album = ForeignKeyField(Album,
                          on_delete='NO ACTION',
                          on_update='NO ACTION',
                          null=True,
                          column_name='AlbumId')
  media_type = ForeignKeyField(MediaType,
                               on_delete='NO ACTION',
                               on_update='NO ACTION',
                               null=False,
                               column_name='MediaTypeId')
  genre = ForeignKeyField(Genre,
                          on_delete='NO ACTION',
                          on_update='NO ACTION',
                          null=True,
                          column_name='GenreId')
  composer = CharField(max_length=220, null=True, column_name='Composer')
  milliseconds = IntegerField(null=False)
  bytes = IntegerField(null=True)
  unit_price = DecimalField(max_digits=10,
                            decimal_places=2,
                            null=False,
                            column_name='UnitPrice')

  class Meta:
    table_name = 'tracks'


class InvoiceItem(BaseModel):
  invoice_item_id = IntegerField(primary_key=True,
                                 null=False,
                                 column_name='InvoiceLineId')
  invoice = ForeignKeyField(Invoice,
                            on_delete='NO ACTION',
                            on_update='NO ACTION',
                            null=False,
                            column_name='InvoiceId')
  track = ForeignKeyField(Track,
                          on_delete='NO ACTION',
                          on_update='NO ACTION',
                          null=False,
                          column_name='TrackId')
  unit_price = DecimalField(max_digits=10,
                            decimal_places=2,
                            null=False,
                            column_name='UnitPrice')
  quantity = IntegerField(null=False)

  class Meta:
    table_name = 'invoice_items'


class Playlist(BaseModel):
  playist_id = IntegerField(primary_key=True,
                            null=False,
                            column_name='PlaylistId')
  name = CharField(max_length=120, null=False)

  class Meta:
    table_name = 'playlists'


class PlaylistTrack(BaseModel):
  playlist = ForeignKeyField(Playlist,
                             column_name='PlaylistId',
                             on_delete='NO ACTION',
                             on_update='NO ACTION',
                             null=False)
  track = ForeignKeyField(Track,
                          column_name='TrackId',
                          on_delete='NO ACTION',
                          on_update='NO ACTION',
                          null=False)

  class Meta:
    table_name = 'playlist_track'
    primary_key = CompositeKey('playlist', 'track')


# Create the tables (optional)
if __name__ == '__main__':
  db.create_tables([
      Album, Artist, Customer, Employee, Genre, Invoice, InvoiceItem,
      MediaType, Playlist, PlaylistTrack, Track
  ])
