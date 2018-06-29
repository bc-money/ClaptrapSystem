import pymysql.cursors
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
	if 'db' not in g:
		mysql = MySQL()
		g.db = pymysql.connect(
				host='10.1.108.95',
				user='root',
				password='Beyond@L1m1ts',
				db='db',
				charset='utf8mb4',
				cursorclass=pymysql.cursors.DictCursor
			)
	return g.db

def close_db(e=None):
	db = g.pop('db', None)
	if db is not None:
		db.close()

def init_db():
	db = get_db()
	with current_app.open_resource('schema.sql') as f:
		db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
	""" Clear the existing data and create new tables """
	init_db()
	click.echo('Initialized the database')

def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)