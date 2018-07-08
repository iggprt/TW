import sqlite3

conn = sqlite3.connect('TW.db')
conn.text_factory = str
c = conn.cursor()

def create_tables():
	c.execute("""CREATE TABLE IF NOT EXISTS farm
		(v_id primary key, name, x INTEGER, y INTEGER, owner, tribe, continent, points INTEGER, distance)""")

def append_village(v_id=0, name="na", de_pe = 1, last_at = 0 ,x=0, y=0, owner='na', tribe='na', continent='na', points=0, distance=100000):
	c.execute("""INSERT INTO farm(v_id, name, de_pe, last_at, x,y,owner,tribe,continent,points, distance)
				VALUES (:v_id, :name, :de_pe, last_at, :x, :y, :owner, :tribe, :continent, :points, :distance)""",{
		'v_id': v_id,
		'name': name,
		'de_pe': 1,
		'last_at': 0 ,
		'x': x,
		'y': y,
		'owner': owner,
		'tribe': tribe,
		'continent': continent,
		'points': points,
		'distance':distance
		})

	conn.commit()

def upload():
	f = open('villages.txt', 'r')
	f = f.read()
	for line in f:
		


upload()