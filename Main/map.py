import matplotlib.pyplot as plt
import map_sql

#########  configs ########
SIZES = [10,40,70,120]  #pixel sizes for villages

class Map():

	def _init__(self):
		self.connect()

		self.table = map_sql.get_villages()

		self.x = [line[2] for line in table]
		self.y = [line[3] for line in table]
		self.points = [line[7] for line in table]
		self.owner = [line[4] for line in table]
		self.tribe = [line[5] for line in table]
		self.dist = [line[8] for line in table]

		self.size = []
		self.c_map =[]

		for p in self.points:
		    if p < 300:
		        size.append(SIZES[0])
		    elif p >= 300 and p < 1000:
		        size.append(SIZES[1])
		    elif p >= 1000 and p < 3000:
		        size.append(SIZES[1])
		    elif p >= 3000 and p < 9000:
		        size.append(SIZES[2])
		    else:
		        size.append(SIZES[3])


		for vill in self.table:

		    if vill[4] == 'iggprt' or vill[4] == 'eX0D1' or vill[4] == 'Nicusimo' or vill[4] == 'dina grameni' or vill[4] == 'juliannn':
		        c_map.append('yellow')
		        
		    elif vill[4] == 'Vă dău fum':
		        c_map.append('red')

		    elif vill[5] ==  'Roma' or vill[5] ==  'R II' or vill[5] ==  'R III' or vill[5] ==  'R IV':
		        c_map.append('pink')

		    elif vill[5] ==  'killer' or vill[5] ==  'Kill1' or vill[5] ==  'Kill2' or vill[5] ==  'Kill3' or vill[5] ==  'Kill4':
		        c_map.append('g')

		    elif vill[5] == '=SN4=' or vill[5] == '=SN3=' or vill[5] == '=SN2=' or vill[5] == '=SN=' or vill[5] == '=SN5=':
		        c_map.append('#00FFFF')

		    else:
		        c_map.append('#A4A4A4')

		self.fig,self.ax = plt.subplots()
		self.sc = plt.scatter(x,y,c=c_map, s=size)
		self.annot = ax.annotate("", xy=(1,0), xytext=(20,20),textcoords="offset points",
		                    bbox=dict(boxstyle="round", fc="w"),
		                    arrowprops=dict(arrowstyle="->"))
		self.annot.set_visible(False)
		self.plt.grid()
		self.plt.ylim(500,520)
		self.plt.xlim(570,590)
		self.plt.gca().invert_yaxis()
		self.plt.show()

	def update_annot(self, ind):
	    # print (plt.gca(projection='polar'))
	    pos = sc.get_offsets()[ind["ind"][0]]
	    self.annot.xy = pos
	    d = dist[ind['ind'][0]]
	    text = "{}: {}\n {} \n{}  {}".format(owner[ind['ind'][0]], points[ind['ind'][0]],
	                           tribe[ind['ind'][0]], dist[ind['ind'][0]], ('%.1f' %((d*22)/60)))
	    self.annot.set_text(text)
	    self.annot.get_bbox_patch().set_facecolor(c_map[ind['ind'][0]])
	    self.annot.get_bbox_patch().set_alpha(0.9)
	    # print (ax.get_ylim())


	def hover(self, event):
	    vis = self.annot.get_visible()
	    if event.inaxes == ax:
	        cont, ind = sc.contains(event)
	        if cont:
	            self.update_annot(ind)
	            self.annot.set_visible(True)
	            self.fig.canvas.draw_idle()
	        else:
	            if vis:
	                self.annot.set_visible(False)
	                self.fig.canvas.draw_idle()

	def connect(self):
		self.fig.canvas.mpl_connect("motion_notify_event", self.hover)
	
m = Map()
	
		