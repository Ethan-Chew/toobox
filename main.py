### ⓖ ⒢ ℊ Granwyn's Part ℊ ⒢ ⓖ ###
# and Ethan's Part :D #
from re import S
import tkinter as tk
from tkinter import ttk
import os
import time
from tkinter import font
import json
import webbrowser

from pandas import wide_to_long

import config
from PIL import ImageTk, Image

# Important UI Details
## 1. Default Font Size is *20*

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.setup_widgets()
        # Variable to track if fullscreen
        self.fullScreen = False
        # Set fullscreen
        self.fullScreenBindings()
        self.notify("Toobox", "Testing Notification", "Boop")
        
    def change_theme(self):
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            # Set light theme
            root.tk.call("set_theme", "light")
        else:
            # Set dark theme
            root.tk.call("set_theme", "dark")

    # Full Screen Toggle
    def fullScreenBindings(self):
        root.attributes("-fullscreen", self.fullScreen)
        root.bind("f", self.toggleFullScreen)
        root.bind("<F11>", self.toggleFullScreen)
        root.bind("<Escape>", self.quitFullScreen)
    
    def toggleFullScreen(self, event):
        self.fullScreen = not self.fullScreen
        root.attributes("-fullscreen", self.fullScreen)

    def quitFullScreen(self, event):
        self.fullScreen = False
        root.attributes("-fullscreen", self.fullScreen)

    # Setup Widgets
    def setup_widgets(self):
        # Styles
        style = ttk.Style()
##        style.configure("tbstyles.Treeview", font=("TkDefaultFont",14))

        # Panedwindow
        self.paned = ttk.PanedWindow(self, orient="horizontal")
        self.paned.pack(fill="both", expand=True, anchor="center")

        # Selection Pane
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)
        
        self.newpane = ttk.PanedWindow(self.pane_1, orient="horizontal")
        
        ## Treeview Label
        self.treeViewTopLab = ttk.Label(self.newpane, text="Tools", font=('TkDefaultFont',20, 'bold'))
        self.treeViewTopLab.pack(side="left",padx=5, anchor="w", fill="y")

        # Treeview Switch
        self.switch = ttk.Checkbutton(
            self.newpane, text="Change Theme", style="Switch.TCheckbutton", command=self.change_theme
        )
        self.switch.pack(side="right", padx=5, anchor="e", fill="y")
        
        self.newpane.pack(fill="x", anchor="n", pady=10)
        
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            style="tbstyles.Treeview"
        )

        self.treeview.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)
        
        ## Treeview columns
        self.treeview.column("#0", anchor="w", minwidth=100)
        ## Define treeview data
        treeview_data = [
            ("", 1, "Chemistry"),
            (1, 2, "Periodic Table"),
            (1, 3, "Salt Solubilities"),
            (1, 4, "Chemical Equation"),
            (1, 5, "Ionic Equation"),
            ("", 6, "Mathematics"),
            (6, 7, "Calculator"),
            (6, 8, "Equations"),
            (8, 9, "Simultaneous"),
            (8, 10, "Quadratic"),
            (8, 11, "Cubic"),
            (8, 12, "Quartic"),
            (6, 13, "Matrices"),
            (6, 14, "Inequalities"),
            (6, 15, "Mensuration"),
            (15, 16, "Area"),
            (16, 17, "Rectangle/Square"),
            (16, 18, "Triangle"),
            (16, 19, "Parallelogram"),
            (16, 20, "Rhombus"),
            (16, 21, "Trapezium"),
            (16, 22, "Circle/Semicircle"),
            (15, 23, "Volume"),
            (23, 24, "Pyramid"),
            (24, 25, "Triangle-Based"),
            (24, 26, "Square-Based"),
            (24, 27, "Cone"),
            (23, 28, "Sphere/Hemisphere"),
            (23, 29, "Prism"),
            (29, 30, "Triangular Prism"),
            (29, 31, "Cylinder"),
            (29, 32, "Cuboid/Cube"),
            (6, 33, "Percentage"),
            (6, 34, "Coordinate Geometry"),
            (34, 35, "Gradient"),
            (34, 36, "Distance/Length"),
            (34, 37, "Perpendicular Lines"),
            (6, 38, "Circles"),
            (38, 39, "Circle Properties"),
            (38, 40, "Equation of Circle"),
            ("", 41, "Revision"),
            (41, 42, "Grade Planner"),
            (41, 43, "Grade Calculator"),
        ]

        # Insert treeview data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2]
            )
            if item[0] == "" or item[1] in {8, 15, 16, 23, 24, 29, 34, 38, 41}:
                self.treeview.item(item[1], open=True)  # Open parents
##        children = self.treeview.get_children() 
##        self.treeview.selection_set(children)
        # Select and scroll
        # self.treeview.selection_set(10)
        self.treeview.see(1)

        # Home Screen UI
        ## Main Home Screen Frame
        self.homeScreen = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.homeScreen, weight=10)
        self.notebook = ttk.Notebook(self.homeScreen, padding=3)
        self.notebook.pack(fill="both", expand=True)

        ## Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
##        self.sizegrip.pack(side="bottom")

        ## Top Labels
        self.welcomeFrame = ttk.Frame(self.notebook)
        self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
        self.helloUserLab = ttk.Label(self.welcomeFrame ,text="Hello, {}".format(config.username), font=("TkDefaultFont",50,'bold'))
        self.helloUserLab.pack(pady=2)
        self.welcomeLab = ttk.Label(self.welcomeFrame, text="Welcome to Toobox!",font=("TkDefaultFont", 15))
        self.welcomeLab.pack(side="left")

        ## Toobox Information
        self.widthOfTooboxInfo = 200
        self.tooboxInfoFrame = ttk.Frame(self.notebook, width=self.widthOfTooboxInfo)
        self.tooboxInfoFrame.pack(side="left", padx=25, pady=18, anchor="w")
        appIconImg = ImageTk.PhotoImage(Image.open('src/images/AppIcon.png').resize((self.widthOfTooboxInfo-40,self.widthOfTooboxInfo-40), Image.ANTIALIAS))
        self.imgPanel = ttk.Label(self.tooboxInfoFrame, image=appIconImg)
        self.imgPanel.image = appIconImg
        self.appDescText = ttk.Label(self.tooboxInfoFrame, font=(17), wraplength=self.widthOfTooboxInfo, justify="left" ,text="Toobox is an app is a Toolbox of different tools to help in your Academics. Toobox provides various tools for a wide range of topics and subjects that will definately help you while revising and studying.")
        self.appDescText.pack(side="bottom")
        self.imgPanel.pack(side="bottom", fill="both", expand="yes", pady=32)

        ## Favourites
        self.favouritesFrame = ttk.Frame(self.notebook, width=self.widthOfTooboxInfo)
        self.favouritesFrame.pack(side="left", pady=18, anchor="w")
        self.favouritesText = ttk.Label(self.favouritesFrame, text="", font=("TkDefaultFont", 18, 'bold'))
        self.favouritesText.pack(side="top", pady=3)

        ## Recently Opened
        file = open('.recentlyOpened.json')
        data = json.load(file)
        file.close()
        data = list(data['recentlyOpened'])
        self.recentlyOpenedFrame = ttk.Frame(self.notebook, width=self.widthOfTooboxInfo)
        self.recentlyOpenedFrame.pack(side="left", padx=20, pady=18, anchor="w")
        self.recentlyOpenedText = ttk.Label(self.recentlyOpenedFrame, text="Recently Opened ({})".format(str(len(data))),font=("TkDefaultFont",18, "bold"))
        self.recentlyOpenedText.pack(side="top", pady=3)
        self.holdROItemFrame = ttk.Frame(self.recentlyOpenedFrame)
        self.holdROItemFrame.pack(side="top")
        for ropenedItem in data:
            self.ropenedItemBtn = ttk.Button(self.holdROItemFrame, text=ropenedItem, width=30)
            self.ropenedItemBtn.pack(side="top", pady=2)

    def on_tree_select(self, event):
        file = open('.recentlyOpened.json')
        data = json.load(file)
        file.close()
        data = list(data['recentlyOpened'])
        bruh = {"recentlyOpened": []}
        config.currentlySelected = self.treeview.item(self.treeview.focus())['text']

        if (len(data) < 3):
            data.append(config.currentlySelected)
        else:
            data.append(config.currentlySelected)
            data.pop(0)
        bruh['recentlyOpened'] = data
        with open('.recentlyOpened.json', 'w') as f:
            json.dump(bruh,f)
        
        self.holdROItemFrame.pack_forget()
        self.notebook.update()
        for ropenedItem in data:
            self.ropenedItemBtn = ttk.Button(self.holdROItemFrame, text=ropenedItem, width=30)
            self.ropenedItemBtn.pack(side="top", pady=2)
        self.notebook.update()

        self.recentlyOpenedText.pack_forget()
        self.recentlyOpenedFrame.pack_forget()
        self.tooboxInfoFrame.pack_forget()
        self.welcomeFrame.pack_forget()
        
        if len(data) > 0:
            if config.currentlySelected == data[-1]:
                self.showHomeScreen()
            else:
                if (len(data) < 3):
                    data.append(config.currentlySelected)
                else:
                    data.append(config.currentlySelected)
                    data.pop(0)
        else:
            if (len(data) < 3):
                data.append(config.currentlySelected)
            else:
                data.append(config.currentlySelected)
                data.pop(0)
        
        root.update()
            
#        if config.currentlySelected == "Ionic Equation":
#            lambda: controller.show_frame("ionicEqn")
        # for item in self.treeview.selection():
        #     print(str("Selected Item: "+self.treeview.item(item, "text")))
        
    def showHomeScreen(self):
        self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
        self.helloUserLab.pack(pady=2)
        self.welcomeLab.pack(side="left")
        self.tooboxInfoFrame.pack(side="left", padx=25, pady=18, anchor="w")
        self.appDescText.pack(side="bottom")
        self.imgPanel.pack(side="bottom", fill="both", expand="yes", pady=32)
        file = open('.recentlyOpened.json')
        data = json.load(file)
        file.close()
        data = list(data['recentlyOpened'])
        self.recentlyOpenedFrame = ttk.Frame(self.notebook, width=self.widthOfTooboxInfo)
        self.recentlyOpenedFrame.pack(side="left", padx=20, pady=18, anchor="w")
        self.recentlyOpenedText = ttk.Label(self.recentlyOpenedFrame, text="Recently Opened ({})".format(str(len(data))),font=("TkDefaultFont",18, "bold"))
        self.recentlyOpenedText.pack(side="top", pady=3)
        self.holdROItemFrame = ttk.Frame(self.recentlyOpenedFrame)
        self.holdROItemFrame.pack(side="top")
        for ropenedItem in data:
            self.ropenedItemBtn = ttk.Button(self.holdROItemFrame, text=ropenedItem, width=30)
            self.ropenedItemBtn.pack(side="top", pady=2)
            
    def _quit(self):
        root.quit()
        root.destroy()

    def notify(self, title, text, sound):
        os.system("""
                  osascript -e 'display notification "{}" with title "{}" sound name "{}"'
                  """.format(text, title, sound))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Toobox")

    # Simply set the theme
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "light")
    
    # Set App Icon
    appIconIcns = './src/images/AppIcon.icns'
    root.iconbitmap(appIconIcns)

    app = App(root)
    app.pack(fill="both", expand=True)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = root.winfo_screenwidth()
    y_cordinate = root.winfo_screenheight()
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
##    root.resizable(True, True)
    root.state('zoomed')

    root.mainloop()
