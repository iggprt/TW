import matplotlib.pyplot as plt
import map_sql

#########  configs ########
SIZES = [10,40,70,120]  #pixel sizes for villages

#'https://matplotlib.org/users/event_handling.html'

class Map():

	def __init__(self):


		self.table = map_sql.get_villages()

		self.x = [line[2] for line in self.table]
		self.y = [line[3] for line in self.table]
		self.points = [line[7] for line in self.table]
		self.owner = [line[4] for line in self.table]
		self.tribe = [line[5] for line in self.table]
		self.dist = [line[8] for line in self.table]

		self.size = []
		self.c_map =[]
		print('_______-_-_-_____--___--_____')
		for p in self.points:
		    if p < 300:
		        self.size.append(SIZES[0])
		    elif p >= 300 and p < 1000:
		        self.size.append(SIZES[1])
		    elif p >= 1000 and p < 3000:
		        self.size.append(SIZES[1])
		    elif p >= 3000 and p < 9000:
		        self.size.append(SIZES[2])
		    else:
		        self.size.append(SIZES[3])


		for vill in self.table:

		    if vill[4] == 'iggprt' or vill[4] == 'Nicusimo':
		        self.c_map.append('yellow')

		    elif vill[5] ==  'Roma' or vill[5] ==  'R II' or vill[5] ==  'R III' or vill[5] ==  'R IV':
		        self.c_map.append('pink')

		    elif vill[5] == '=SN4=' or vill[5] == '=SN3=' or vill[5] == '=SN2=' or vill[5] == '=SN=' or vill[5] == '=SN5=':
		        self.c_map.append('#00FFFF')

		    else:
		        self.c_map.append('#6E6E6E')
		self.fig, self.ax = plt.subplots()
		self.connect()
		self.sc = plt.scatter(self.x,self.y,c=self.c_map, s=self.size)
		self.annot = self.ax.annotate("", xy=(1,0), xytext=(20,20),textcoords="offset points",
		                    bbox=dict(boxstyle="round", fc="w"),
		                    arrowprops=dict(arrowstyle="->"))
		self.annot.set_visible(False)
		plt.grid()
		plt.ylim(500,520)
		plt.xlim(570,590)
		plt.gca().invert_yaxis()
		plt.show()

	def update_annot(self, ind):
	    # print (plt.gca(projection='polar'))
	    pos = self.sc.get_offsets()[ind["ind"][0]]
	    self.annot.xy = pos
	    d = self.dist[ind['ind'][0]]
	    text = "{}: {}\n {} \n{}  {}".format(self.owner[ind['ind'][0]], self.points[ind['ind'][0]],
	                           self.tribe[ind['ind'][0]], self.dist[ind['ind'][0]], ('%.1f' %((d*22)/60)))
	    self.annot.set_text(text)
	    self.annot.get_bbox_patch().set_facecolor(self.c_map[ind['ind'][0]])
	    self.annot.get_bbox_patch().set_alpha(0.9)
	    # print (ax.get_ylim())


	def hover(self, event):
	    vis = self.annot.get_visible()
	    if event.inaxes == self.ax:
	        cont, ind = self.sc.contains(event)
	        if cont:
	            self.update_annot(ind)
	            self.annot.set_visible(True)
	            self.fig.canvas.draw_idle()
	        else:
	            if vis:
	                self.annot.set_visible(False)
	                self.fig.canvas.draw_idle()

	def press(self, event):
		if event.inaxes == self.ax:
			cont, ind = self.sc.contains(event)
			if cont:
				print(self.owner[ind['ind'][0]])
			else:
				print('___ ' + str(event))

	def connect(self):
		self.fig.canvas.mpl_connect("motion_notify_event", self.hover)
		self.fig.canvas.mpl_connect("button_press_event", self.press)
