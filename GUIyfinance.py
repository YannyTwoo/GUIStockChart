import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd




from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from yfinance import ticker


HEIGHT = 600
WIDTH = 800
root = tk.Tk()

def get_price_from_ticker(tickersymbol):
    tickersymbol= tickersymbol.upper()
    try:
        obj = yf.download(tickers= tickersymbol, period = '5y', rounding= True)
        return obj
    except Exception as e:
        rt_string = "Couldn't find the data for this ticker"
        print(e)


def plotgraph(datayf , tickername):
    for widgets in frame_graph.winfo_children():
      widgets.destroy()
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
  
    # list of squares
    y = datayf.Open
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.xlabel = f'{tickername.upper()} Chart'
    # plotting the graph
    plot1.plot(y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = frame_graph)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame_graph)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()



# canvas = tk.Canvas(root , height = HEIGHT , width= WIDTH)
# canvas.pack()
root.geometry("800x650")
root.title('Stock Charts from YFinance')
root.configure(bg='#396EB0')


frame_top = tk.Frame(root , bg = '#2E4C6D')
frame_top.place(relx = 0 , rely = 0.02, relwidth= 1, relheight=0.18, anchor = 'nw')

frame_middle = tk.Frame(root , bg = '#396EB0')
frame_middle.place(relx= 0, rely= 0.3, relwidth= 1, relheight= 0.12 , anchor = 'nw')

frame_graph = tk.Frame(root , bg = '#DADDFC')
frame_graph.place(relx= 0, rely= 0.52 , relwidth=1 , relheight=0.48 , anchor = 'nw')



label1 = tk.Label(frame_top , text = 'Stock Price Display',  font = "Helvetica 32 bold" , bg = '#DADDFC')
label1.place(relwidth =1 , relheight =1 )


entry2 = tk.Entry( frame_middle , bg = '#DADDFC' , font = "Helvetica 18 bold")
entry2.place(relx = 0.3 , relwidth = 0.25, relheight =1 )
button1 = tk.Button(frame_middle , text = "Get Chart" , font = "Helvetica 18 bold" , bg = '#DADDFC' , activebackground= 'red' , command = lambda: plotgraph( get_price_from_ticker(entry2.get()) , entry2.get()))

button1.place(relx = 0.6 , relwidth = 0.2, relheight = 1)

# entry3 = tk.Entry( bg = 'cyan')
# entry3.place(relx = , rely = , relwidth = , relheight = )



root.mainloop()