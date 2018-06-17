import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
# from matplotlib.backends.backend_wxagg import NavigationToolbar2Wx 
from matplotlib.backend_tools import ToolBase, ToolToggleBase

class MyCustomToolbar(ToolBase): 
    ON_CUSTOM_LEFT  = wx.NewId()
    ON_CUSTOM_RIGHT = wx.NewId()

    def __init__(self, plotCanvas):
        # create the default toolbar
        NavigationToolbar2Wx.__init__(self, plotCanvas)
        # add new toolbar buttons 
        self.AddSimpleTool(self.ON_CUSTOM_LEFT, _load_bitmap('stock_left.xpm'),
                           'Pan to the left', 'Pan graph to the left')
        wx.EVT_TOOL(self, self.ON_CUSTOM_LEFT, self._on_custom_pan_left)
        self.AddSimpleTool(self.ON_CUSTOM_RIGHT, _load_bitmap('stock_right.xpm'),
                           'Pan to the right', 'Pan graph to the right')
        wx.EVT_TOOL(self, self.ON_CUSTOM_RIGHT, self._on_custom_pan_right)

    # pan the graph to the left
    def _on_custom_pan_left(self, evt):
        ONE_SCREEN = 1
        axes = self.canvas.figure.axes[0]
        x1,x2 = axes.get_xlim()
        ONE_SCREEN = x2 - x1
        axes.set_xlim(x1 - ONE_SCREEN, x2 - ONE_SCREEN)
        self.canvas.draw()

    # pan the graph to the right
    def _on_custom_pan_right(self, evt):
        ONE_SCREEN = 1
        axes = self.canvas.figure.axes[0]
        x1,x2 = axes.get_xlim()
        ONE_SCREEN = x2 - x1
        axes.set_xlim(x1 + ONE_SCREEN, x2 + ONE_SCREEN)
        self.canvas.draw()

fig = plt.figure()
# plotting
X=[1,2,3]
Y=[10,20,30]
ax  = fig.add_subplot(1, 1, 1)
ax.plot(X,Y,'bo-')
ax.grid()
ax.legend()
X1=[]
Y1=[]

def on_press(event):
    print( "canvas clicked")
    print ("how can I tell whether the button is clicked?")
    print( event)
def on_button_clicked(event):
    print ("button clicked")
    print( event)
axnext = plt.axes([0.9, 0.00, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(on_button_clicked)
# fig.canvas.mpl_connect('button_press_event', on_press)
plt.show()

