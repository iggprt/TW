from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
import tkinter as tk
import map
# import farm_comp



from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class TW(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Solo de chitara')



		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)


		self.frames = {}

		for F in (StartPage, PageOne):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid (row=0, column = 0, sticky = 'nsew')


		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	""" misc """
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.height = 5000
		self.width  = 500

		label = tk.Label(self, text='start page')
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(PageOne))
		button1.pack(side='right')

		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(PageOne))
		button2.pack(side='left')

		m = map.Map
		button = tk.Button(self, text = 'map', command = m)
		button.pack(side = 'top')

		listbox = tk.Listbox(self, height = 5)
		elem = (1,2,23,4)
		listbox.insert('end' , elem)
		listbox.pack()



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        fr =  tk.Frame(self)
        but = tk.Button(fr, text = 'da')
        but.pack()
        fr.pack()



app = TW()
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass
