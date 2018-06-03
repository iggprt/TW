import matplotlib.pyplot as plt
import numpy as np; np.random.seed(3)
import random

#x = np.random.rand(15)
x = [1,2,3,3,5,6,7,8,9,10,11,12,13,14,15]
y = [1,1,3,4,5,6,7,8,9,10,11,12,13,14,15]
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
sc = plt.scatter(xs,ys,c=colors, s=points, norm=norm,)

annot = ax.annotate("", xy=(1,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):

    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}\n {} ".format(" ".join(list(map(str,ind["ind"]))), 
                           " ".join([names[n] for n in ind["ind"]]), ind['ind'],
                           ind["ind"] )
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.7)


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

plt.show()