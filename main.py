### ⓖ ⒢ ℊ Granwyn's Part ℊ ⒢ ⓖ ###
# and Ethan's Part :D #
from pydoc_data.topics import topics
from re import S
import tkinter as tk
from tkinter import ttk
import os
from tkinter import font
import json
from PIL import ImageTk, Image
from tkinter import Menu
import config
from toolsUI import *
from components.wrappedLabel import WrappingLabel
import os
from sys import platform


ROOTDIR=os.path.abspath(os.curdir)
recentlyused=os.path.join(ROOTDIR,".recentlyOpened.json")
appIconIcon = os.path.join(ROOTDIR,'src','images','AppIcon.ico')
appIconIcns = os.path.join(ROOTDIR,'src','images','AppIcon.icns')
appIconPng = os.path.join(ROOTDIR,'src','images','AppIcon.png')
# Important UI Details
## 1. Default Font Size is *20*
functionalities = {
            "Chemical Equation" :   ChemicalEquation,
            "Rectangle/Square"  :   Rectangle,
            "Ionic Equation"    :   IonicEqn,
            "Salt Solubilities" :   SaltSolubility,
            "Calculator"        :   calculate,
            "Circle/Semicircle" :   Circle,
            "Quadratic"         :   SolveQuad,
            "Parallelogram"     :   Parallelogram,
            "Trapezium"         :   Trapezium,
            "Simultaneous"      :   simsolver,
            "Triangle"          :   triangle
        }
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
                (6, 38, "Circles"),
                    (38, 39, "Circle Properties"),
                    (38, 40, "Equation of Circle"),
        ]
topics=[treeview_data[i-1][2] for i in [1,6,8,16,15,23,34,24,29]]

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.setup_menu()
        self.setup_widgets()
        # Variable to track if fullscreen
        self.fullScreen = False
        # Set fullscreen
        self.fullScreenBindings()
        self.goHome()
        # self.notify("Toobox", "Testing Notification", "Boop")

        
    def change_theme(self):
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            # Set light theme
            root.tk.call("set_theme", "light")
        else:
            # Set dark theme
            root.tk.call("set_theme", "dark")

    def setup_menu(self):
        menubar = Menu(root)
        # tools
        tools=Menu(menubar, tearoff=0)
        for i in sorted(list(functionalities.keys())):
            
            tools.add_command(label=i, command=lambda i=i: self.run_func(i))
        menubar.add_cascade(label="Tools", menu=tools)
        root.config(menu=menubar)

        #recently opened
        romenu=Menu(menubar, tearoff=0)
        file = open(recentlyused)
        data = json.load(file)
        file.close()
        data = list(set(data['recentlyOpened']))
        for i in data:
            romenu.add_command(label=i, command=lambda i=i: self.run_func(i))
        
        menubar.add_cascade(label="Recently Opened", menu=romenu)

        root.mainloop

    # Keybines :D
    ## Full Screen Toggle
    def fullScreenBindings(self):
        root.attributes("-fullscreen", self.fullScreen)
        root.bind("f", self.toggleFullScreen)
        root.bind("<F11>", self.toggleFullScreen)
        root.bind("<Escape>", self.quitFullScreen)
    
    ## Back to Home
    def goHome(self):
        root.bind("h", self.handleBackToHS)

    def handleBackToHS(self, event):
        try:
            self.clearScreen()
            self.welcomeFrame.pack_forget()
            self.showHomeScreen(self)
        except: pass
    
    def toggleFullScreen(self, event):
        self.fullScreen = not self.fullScreen
        root.attributes("-fullscreen", self.fullScreen)

    def quitFullScreen(self, event):
        self.fullScreen = False
        root.attributes("-fullscreen", self.fullScreen)

    # Setup Widgets
    def setup_widgets(self):
        # Panedwindow
        self.paned = ttk.PanedWindow(self, orient="horizontal")
        self.paned.pack(fill="both", expand=True, anchor="center")

        # Selection Pane
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)
        
        self.newpane = ttk.PanedWindow(self.pane_1, orient="horizontal")
        
        ## Treeview Label
        self.treeViewTopLab = WrappingLabel(self.newpane, text="Tools", font=('TkDefaultFont',23, 'bold'))
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
        

        # Insert treeview data
        for item in treeview_data:
            if item[2] in functionalities:
                self.treeview.insert(
                    parent=item[0], index="end", iid=item[1], text=item[2]
                )
            if item[0] == "" or item[1] in {8, 15, 16, 23, 24, 29, 34, 38, 41}:
                self.treeview.insert(
                    parent=item[0], index="end", iid=item[1], text=item[2]
                )
                self.treeview.item(item[1], open=True)  # Open parents
        # Select and scroll
        self.treeview.see(1)

        # Home Screen UI
        ## Main Home Screen Frame
        self.homeScreen = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.homeScreen, weight=10)
        self.notebook = ttk.Notebook(self.homeScreen, padding=3)
        self.notebook.pack(fill="both", expand=True)

        ## Sizegrip
        self.sizegrip = ttk.Sizegrip(self)

        ## Top Labels
        self.welcomeFrame = ttk.Frame(self.notebook)
        # self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
        # self.helloUserLab = WrappingLabel(self.welcomeFrame ,text="Hello, {}".format(config.username), font=("TkDefaultFont",50,'bold'))
        # self.helloUserLab.pack(pady=2)
        # self.welcomeLab = WrappingLabel(self.welcomeFrame, text="Welcome to Toobox!",font=("TkDefaultFont", 15))
        # self.welcomeLab.pack(side="left")

        ## Toobox Information
        self.widthOfTooboxInfo = 200
        self.tooboxInfoFrame = ttk.Frame(self.notebook, width=self.widthOfTooboxInfo)
        self.tooboxInfoFrame.pack(side="left", padx=25, pady=18, anchor="w")
        appIconImg = ImageTk.PhotoImage(Image.open(appIconPng).resize((self.widthOfTooboxInfo-40,self.widthOfTooboxInfo-40), Image.ANTIALIAS))
        self.imgPanel = WrappingLabel(self.tooboxInfoFrame, image=appIconImg)
        self.imgPanel.image = appIconImg
        self.appDescText = WrappingLabel(self.tooboxInfoFrame, font=(17), wraplength=self.widthOfTooboxInfo, justify="left" ,text="Toobox is an app is a Toolbox of different tools to help in your Academics. Toobox provides various tools for a wide range of topics and subjects that will definately help you while revising and studying.")
        self.appDescText.pack(side="bottom")
        self.imgPanel.pack(side="bottom", fill="both", expand="yes", pady=32)

        ## Favourites
        # self.favouritesFrame = ttk.Frame(self.notebook, width=self.widthOfTooboxInfo)
        # self.favouritesFrame.pack(side="left", pady=18, anchor="w")
        # self.favouritesText = WrappingLabel(self.favouritesFrame, text="", font=("TkDefaultFont", 18, 'bold'))
        # self.favouritesText.pack(side="top", pady=3)
        self.showHomeScreen(0)
        
    def clearScreen(self):
        self.recentlyOpenedText.pack_forget()
        self.recentlyOpenedFrame.pack_forget()
        self.tooboxInfoFrame.pack_forget()
        self.welcomeFrame.pack_forget()

        try:
            self.mainFrame.pack_forget()
            self.welcomeFrame.place_forget()
        except:
            pass
    def run_func(self, current):
        print(current)
        file = open(recentlyused)
        data = json.load(file)
        file.close()
        data = list(set(data['recentlyOpened']))
        bruh = {"recentlyOpened": []}
        config.currentlySelected = current

        if (len(data) < 10):
            if config.currentlySelected not in data:
                data=[config.currentlySelected] + data
        else:
            data = [config.currentlySelected] + data[:-1]

        bruh['recentlyOpened'] = data
        with open(recentlyused, 'w') as f:
            json.dump(bruh,f)
        
        self.holdROItemFrame.pack_forget()
        self.notebook.update()
        for ropenedItem in data:
            self.ropenedItemBtn = ttk.Button(self.holdROItemFrame, text=ropenedItem, width=30)
            self.ropenedItemBtn.pack(side="top", pady=2)
        self.notebook.update()

        self.clearScreen()
        
        if config.currentlySelected in functionalities:
            try: self.mainFrame.pack_forget()
            except: print("error")
            self.welcomeFrame.pack_forget()
            self.clearScreen()
            functionalities[config.currentlySelected](self)
        elif not config.currentlySelected in topics:
            try: self.mainFrame.pack_forget()
            except: print("error")
            self.welcomeFrame.pack_forget()
            self.clearScreen()
            notUsable(self)
        self.setup_menu()
        root.update()
    def on_tree_select(self, event):
        self.run_func(self.treeview.item(self.treeview.focus())['text'] )
        
        
    def showHomeScreen(self, event):
        self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
        self.helloUserLab = WrappingLabel(self.welcomeFrame,text="Hello, {}".format(config.username), font=("TkDefaultFont",50,'bold'))
        self.helloUserLab.pack(pady=2,fill="x")
        self.welcomeLab = WrappingLabel(self.welcomeFrame, text="Welcome to Toobox!",font=("TkDefaultFont", 15))
        self.welcomeLab.pack(side="left", fill="x")
        self.welcomeLab2 = WrappingLabel(self.welcomeFrame, text="Select a tool to get started!",font=("TkDefaultFont", 15))
        self.tooboxInfoFrame.pack(side="left", padx=25, pady=18, anchor="w")
        self.appDescText.pack(side="bottom")
        self.imgPanel.pack(side="bottom", fill="both", expand="yes", pady=32)
        file = open(recentlyused)
        data = json.load(file)
        file.close()
        data = list(set(data['recentlyOpened']))
        self.recentlyOpenedFrame = ttk.Frame(self.notebook, width=self.widthOfTooboxInfo)
        self.recentlyOpenedFrame.pack(side="left", padx=20, pady=18, anchor="w")
        self.recentlyOpenedText = WrappingLabel(self.recentlyOpenedFrame, text="Recently Opened ({})".format(str(len(data[:4]))),font=("TkDefaultFont",18, "bold"))
        self.recentlyOpenedText.pack(side="top", pady=3)
        self.holdROItemFrame = ttk.Frame(self.recentlyOpenedFrame)
        self.holdROItemFrame.pack(side="top")
        for ropenedItem in data[:4]:
            self.ropenedItemBtn = ttk.Button(self.holdROItemFrame, text=ropenedItem, width=30,command=(lambda : self.run_func(ropenedItem)))
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
    root.tk.call("set_theme", "dark")
    
    # Set App Icon
    # root.iconbitmap(appIconIcns)
    img = tk.Image("photo", file=appIconPng)
    # root.iconphoto(True, img) # you may also want to try this.
    root.tk.call('wm','iconphoto', root._w, img)

    app = App(root)
    app.pack(fill="both", expand=True)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = root.winfo_screenwidth()
    y_cordinate = root.winfo_screenheight()
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.state('zoomed')

    if platform == 'darwin':
        from pyobjc import Foundation, objc, CoreFoundation 
        from Foundation import NSBundle
        bundle = NSBundle.mainBundle()
        if bundle:
            info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
            if info and info['CFBundleName'] == 'Python':
                info['CFBundleName'] = 'Toobox'
    
    root.mainloop()
