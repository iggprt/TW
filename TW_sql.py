import sqlite3
import math

conn = sqlite3.connect('TW.db')
conn.text_factory = str
c = conn.cursor()

def create_tables():
	c.execute("""CREATE TABLE IF NOT EXISTS villages (v_id primary key, name, x INTEGER, y INTEGER, owner, tribe, continent, points INTEGER)""")

def append_village(v_id=0, name="na", x=0, y=0, owner='na', tribe='na', continent='na', points=0):
	c.execute("""INSERT INTO villages(v_id, name,x,y,owner,tribe,continent,points) VALUES (:v_id, :name, :x, :y, :owner, :tribe, :continent, :points)""",{
		'v_id': v_id,
		'name': name,
		'x': x,
		'y': y,
		'owner': owner,
		'tribe': tribe,
		'continent': continent,
		'points': points
		})

	conn.commit()

def update():
	c.execute("""SELECT v_id, x, y from villages""")
	table = c.fetchall()

	for row in table:
		dist = math.sqrt((row[1]-588)**2 + (row[2]-513)**2)
		c.execute("""UPDATE villages SET distance = :dist
			WHERE v_id = :id""",{
			'dist': dist,
			'id': row[0]
			})
	conn.commit()
	
def get_villages():
	c.execute("""SELECT * from villages""")
	table = c.fetchall()
	return table
