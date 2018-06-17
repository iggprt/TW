import os
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import ttk as ttk
import matplotlib

import matplotlib
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import TW_sql

v = TW_sql.get_villages()

x = [x[2] for x in v]
y = [y[3] for y in v]
p = [p[7] for p in v]

matplotlib.use('TkAgg')

pages = [ BeautifulSoup( open('./htmls/'+file, 'r').read(),'html.parser') for file in files ]

LARGE_FONT = ('Verdana', 15)

class UFC(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.wm_title(self, 'Solo de chitara')

		self.style = ttk.Style()
		self.style.configure('TFrame', background = 'pink')
		self.style.configure('TLabel', background = 'pink')

		container = ttk.Frame(self)
		container.pack(side='top', fill='both', expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)


		self.frames = {}

		for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):

			frame = F(container, self)
			self.frames[F] = frame
			# self.style1 = ttk.Style()
			# self.style1.configure('TButton', background = 'green')
			# frame.configure(background = 'red')
			frame.grid (row=0, column = 0, sticky = 'nsew')

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class StartPage(ttk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text='start page', font = LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(PageOne))
		button1.pack(side='right')

		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(PageThree))
		button2.pack(side='left')

class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text='page unos', font = LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(PageTwo))
		button1.pack(side='right')

		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(StartPage))
		button2.pack(side='left')


class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='page dos', font = LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(PageThree))
		button1.pack(side='right')

		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(PageOne))
		button2.pack(side='left')

class PageThree(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='page graph', font = LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(StartPage))
		button1.pack(side='right')

		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(PageTwo))
		button2.pack(side='left')

		button4 = tk.Button(self, text = 'top notch', command = lambda: controller.show_frame(PageFour))
		button4.pack(side='top')

		f = Figure(figsize = (5,5), dpi = 100)
		a = f.add_subplot(111)
		a.plot([1,2,3],[2,8,6])

		canvas = FigureCanvasTkAgg(f, self)
		#canvas.show()
		canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)


class PageFour(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='page graph', font = LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(StartPage))
		button1.pack(side='right')

		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(PageTwo))
		button2.pack(side='left')

		f = Figure(figsize = (5,5), dpi = 100)
		a = f.add_subplot(111)
		a.scatter([1,2,3],[2,8,6])

		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

		fig,ax = plt.subplots()

sc = plt.scatter(x,y,color = 'r', size = 100)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

app = UFC()
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass


