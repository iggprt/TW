import matplotlib.pyplot as plt
import numpy as np; np.random.seed(3)
import random
import sqlite3
import TW_sql
import matplotlib.ticker as ticker

v = TW_sql.get_villages()

# x = np.random.rand(15)
x = [x[2] for x in v]
y = [y[3] for y in v]
p = [p[7] for p in v]
size = [points/3 for points in p]
id = [i[0] for i in v]
for vil in v:
    print (vil)

names = ['alfa','beta','costel','daniel','elena',
         'fanel','ghe','horia','india','jack',
         'kevin','leo','mama','tata','da',]
c = np.random.randint(1,5,size=15)
c = [1,2,3,3,5,6,0,8,9,10,11,12,13,14,15]

norm = plt.Normalize(0,0)
cmap = plt.cm.RdYlGn

colors = ['red', 'green', 'yellow', 'blue','purple', 'black']
people = ['me', 'you', 'him', 'her','them']

villages = []
for i in range(15):
    villages.append({'id' : i,
                     'owner' : random.choice(people),
                     'x' : random.randint(0,20),
                     'y' : random.randint(0,20),
                     'color' : random.choice(colors),
                     'points' : random.randint(100,1200)})
for v in villages:
    print (str(v))
ids = [village['id'] for village in villages]
owners = [village['owner'] for village in villages]
xs = [village['x'] for village in villages]
ys = [village['y'] for village in villages]
colors = [village['color'] for village in villages]
points = [village['points'] for village in villages]

fig,ax = plt.subplots()
sc = plt.scatter(x,y,c=colors, s=100)

annot = ax.annotate("", xy=(1,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    # print (plt.gca(projection='polar'))
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}\n {} ".format(" ".join(list(map(str,ind["ind"]))),
                            ind['ind'],
                           ind["ind"])
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor('red')
    annot.get_bbox_patch().set_alpha(0.7)
    print (ax.get_ylim())


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

fig.canvas.mpl_connect("motion_notify_event", hover)
# plt.axis(550,560,450,470)
plt.xlim(580,590)
plt.ylim(510,520)

# plt.rc('grid', linestyle="--", color='y')

# ax.xaxis().set_major_locator(ticker.MultipleLocator(5))
# plt.xticks(np.arange(580 , 590,5.0))
# plt.axes().set_aspect('equal')
plt.grid()
plt.gca().invert_yaxis()
plt.show()
