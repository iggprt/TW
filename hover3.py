import matplotlib.pyplot as plt
import numpy as np; np.random.seed(3)
import random
import sqlite3
import TW_sql
import matplotlib.ticker as ticker
from matplotlib.widgets import Button

v = TW_sql.get_villages()

# x = np.random.rand(15)
x = [x[2] for x in v]
y = [y[3] for y in v]
p = [p[7] for p in v]
owner = [o[4] for o in v]
tribe = [line[5] for line in v]
dist = [line[8] for line in v]

size = []
for points in p:
    if points < 300:
        size.append(10)
    elif points >= 300 and points < 1000:
        size.append(40)
    elif points >= 1000 and points<3000:
        size.append(70)
    elif points >= 3000 and points < 9000:
        size.append(120)
    else:
        size.append(170)

norm = plt.Normalize(0,0)

colors = ['red', 'green', 'yellow', 'blue','purple', 'black']
c_map =[]
for (vill,i) in zip(v,range(len(v))):

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


fig,ax = plt.subplots()
sc = plt.scatter(x,y,c=c_map, s=size, norm= norm)
# print (v)
annot = ax.annotate("", xy=(1,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    # print (plt.gca(projection='polar'))
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    d = dist[ind['ind'][0]]
    text = "{}: {}\n {} \n{}  {}".format(owner[ind['ind'][0]], p[ind['ind'][0]],
                           tribe[ind['ind'][0]], dist[ind['ind'][0]], ('%.1f' %((d*22)/60)))
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(c_map[ind['ind'][0]])
    annot.get_bbox_patch().set_alpha(0.9)
    # print (ax.get_ylim())


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()
    #print (plt.xlim)

fig.canvas.mpl_connect("motion_notify_event", hover)
#ticks = [t*5 for t in range(int(1000/100))]

# plt.connect('button_press_event',yolo)
# axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
# but = Button(axprev,"da")
# but.on_clicked(yolo)

# plt.axis(550,560,450,470)


#plt.grid('grid', linestyle="--", color='y')

# ax.xaxis.set_major_locator(ticks)
# plt.yticks(ticks)
#plt.xticks(ticks)
plt.minorticks_on()

# ax.set_xticks(ticks)
# ax.set_yticks(ticks)


plt.grid()
# plt.grid.minorticks_on()


# ax.xaxis.grid.ticks(500)
plt.ylim(500,520)
plt.xlim(570,590)
plt.gca().invert_yaxis()
# plt.axes().set_aspect('equal')
# splt.grid()

plt.show()
