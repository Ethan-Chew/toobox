# Everyone did everything here
## JSON, Main UI, Keybinds, 'Backend' mostly by Ethan
## Refractoring, 'Backend' by Jerick
## Everything else + Starting Point by Granwyn

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
import webbrowser
import tools.periodicTable as pt

# Path of the different Filed
ROOTDIR, _ =os.path.split(os.path.abspath(os.path.realpath(__file__)))
os. chdir(ROOTDIR)
jsonData = os.path.join(ROOTDIR, '.data.json')
appIconIcon = os.path.join(ROOTDIR,'src','images','AppIcon.ico')
appIconIcns = os.path.join(ROOTDIR,'src','images','AppIcon.icns')
appIconPng = os.path.join(ROOTDIR,'src','images','AppIcon.png')
appThemePath =  os.path.join(ROOTDIR,"sun-valley.tcl")
_recentlength=10
FONT='TkDefaultFont'

# Checks for Font Size Change
def reload():
    global fontMultiplier
    file = open(jsonData)
    extractedData = json.load(file)
    file.close()
    fontMultiplier = float(extractedData["fontMultiplier"])

reload()

# Variables
functionalities = {
            "Settings"          :   Settings,
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
            "Triangle"          :   triangle,
            "Equation of Circle":   SolveCircle,
            "Periodic Table"    :   periodicTable,
            "Pyramid"           :   Pyramid,
            "Prism"             :   Prism,
            "Sphere"            :   Sphere,
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
                (15, 23, "Volume and Surface Area"),
                    (23, 24, "Pyramid"),
                        (24, 25, "Triangle-Based"),
                        (24, 26, "Square-Based"),
                        (24, 27, "Cone"),
                    (23, 28, "Prism"),
                        (29, 30, "Triangular Prism"),
                        (29, 31, "Cylinder"),
                        (29, 32, "Cuboid/Cube"),
                    (23, 29, "Sphere"),
                (6, 33, "Percentage"),
                (6, 38, "Circles"),
                    (38, 39, "Circle Properties"),
                    (38, 40, "Equation of Circle"),
            ("", 41, "Settings"),
        ]
TOPICS=[treeview_data[i-1][2] for i in [1,6,8,16,15,23,34,24,29]] # Add Items into Treeview
topics = []

class App(ttk.Frame):
    def __init__(self, parent):
        self.notify("App Shortcuts for Toobox", "Use Control + H to go to the Home Screen and use Control + F to enter Full Screen, Escape Key to exit Full Screen.", "Boop")
        self.screenlist = []
        # aSecret :) hehehehe
        if config.aSecret:
            f()
        self.check_recently_opened()
        # Initalize the app
        ttk.Frame.__init__(self)
        self.setup_menu()
        self.setup_widgets()
        # Variable to track if fullscreen
        self.fullScreen = False
        # Set Bindings/Shortcuts
        self.fullScreenBindings()
        self.goHome()
        # self.resetSettingsSC()
        config.currentlySelected = "Home"
    def getInputs(self, event):
        try:
            text.grid_forget()
            text.destroy()
        except: pass
        self.resFrame.destroy()
        self.resFrame = self.addframe(self.mainFrame)
        e = self.inputField.get().replace(" ", "")
        l=pt.search(e)[:6]
        newf=self.addframe(self.resFrame,borderwidth=1)

        if len(l) > 0:
            temp=WrappingLabel(newf, text="Atomic Number", font=(font,int(fontMultiplier*10)))
            temp.grid(row=0, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Mass Number", font=(font,int(fontMultiplier*10)))
            temp.grid(row=1, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Period"+", "+"Group", font=(font,int(fontMultiplier*10)))
            temp.grid(row=2, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Symbol", font=(font,int(fontMultiplier*15), 'bold'))
            temp.grid(row=3, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Element", font=(font,int(fontMultiplier*12), 'bold'))
            temp.grid(row=4, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Atomic Mass" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=5, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text=", ".join(["Protons","Neutrons","Electrons"]), font=(font,int(fontMultiplier*10)))
            temp.grid(row=6, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Atomic Radius" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=7, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Electron Shells" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=8, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Valence Electrons" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=9, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Electronic Configuration" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=10, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Isotopes" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=11, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text=" ".join(["[{}]".format("Phase"), ", ".join(["Melting Point", "Boiling Point"])]), font=(font,int(fontMultiplier*10)))
            temp.grid(row=12, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Type" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=13, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Radioactive" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=14, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Natural" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=15, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Density" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=16, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Electronegativity" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=17, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="First Ionisation Energy" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=18, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Specific Heat Capacity / J???kg????????K?????" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=19, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Discovered" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=20, column=0, sticky = tk.N+tk.E, padx=2)

            newf.grid(row=0, column=0, sticky = tk.N+tk.E, padx=2)

            r=1
            for i in l:
                newf=self.addframe(self.resFrame,borderwidth=1)
                
                temp=WrappingLabel(newf, text=int(pt.ELEMENTDATA["AtomicNumber"][i]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=0, column=0, sticky = tk.N+tk.W, padx=2)
                temp=WrappingLabel(newf, text=str(int(pt.ELEMENTDATA["MassNumber"][i])), font=(font,int(fontMultiplier*10)))
                temp.grid(row=1, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(int(pt.ELEMENTDATA["Period"][i]))+", "+str(int(pt.ELEMENTDATA["Group"][i])), font=(font,int(fontMultiplier*10)))
                temp.grid(row=2, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Symbol"][i]), font=(font,int(fontMultiplier*15), 'bold'))
                temp.grid(row=3, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Element"][i]), font=(font,int(fontMultiplier*12), 'bold'))
                temp.grid(row=4, column=0, sticky = tk.N+tk.W, padx=2)
                
                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["AtomicMass"][i]) , font=(font,int(fontMultiplier*10)))
                temp.grid(row=5, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=", ".join([str(int(pt.ELEMENTDATA[j][i])) for j in ["Protons","Neutrons","Electrons"]]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=6, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["AtomicRadius"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=7, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(int(pt.ELEMENTDATA["Shells"][i])).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=8, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(int(pt.ELEMENTDATA["Valence"][i])).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=9, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Config"][i]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=10, column=0, sticky = tk.N+tk.W, padx=2)

                iso = str(pt.ELEMENTDATA["Isotopes"][i])
                temp=WrappingLabel(newf, text=str(int(float(iso))) if iso.replace('.','',1).isdigit() else "-", font=(font,int(fontMultiplier*10)))
                temp.grid(row=11, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=" ".join(["[{}]".format(str(pt.ELEMENTDATA["Phase"][i]).title()), ", ".join([str(pt.ELEMENTDATA["MeltingPoint"][i]).title()+"K", str(pt.ELEMENTDATA["BoilingPoint"][i]).title()+"K"])]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=12, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Type"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=13, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text="Yes" if pt.ELEMENTDATA["Radioactive"][i] else "No", font=(font,int(fontMultiplier*10)))
                temp.grid(row=14, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text="Yes" if pt.ELEMENTDATA["Natural"][i] else "No", font=(font,int(fontMultiplier*10)))
                temp.grid(row=15, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Density"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=16, column=0, sticky = tk.N+tk.W, padx=2)

                e = str(pt.ELEMENTDATA["Electronegativity"][i]).title()
                temp=WrappingLabel(newf, text=e if e.replace('.','',1).isdigit() else "-", font=(font,int(fontMultiplier*10)))
                temp.grid(row=17, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["FirstIonization"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=18, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["SpecificHeat"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=19, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=", ".join([str(pt.ELEMENTDATA["Discoverer"][i]).title(), str(pt.ELEMENTDATA["Year"][i]).title()]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=20, column=0, sticky = tk.N+tk.W, padx=2)

                newf.grid(row=0, column=r, sticky = tk.N, padx=2)
                r+=1
        else:
            text = WrappingLabel(self.mainFrame, text="Invalid Input. Please enter a valid Symbol, Element Name, Symbol, Atomic Number, or Number of Electrons, Protons or Neutrons.", font=(font,int(fontMultiplier*14)))
            text.grid(row=1, column=0, padx=2,pady=2, sticky = tk.W+tk.E, columnspan=5)
                
        # self.resFrame.grid(row=1, column=len(l)+1, rowspan=10, columnspan=10, padx=2)
        self.resFrame.grid(row=1, column=0, rowspan=len(l)+1, columnspan=10, padx=2)
        
    def check_recently_opened(self):
        file = open(jsonData)
        try:
            data = json.load(file)
            file.close()
            if type(data["recentlyOpened"]) == list:
                return 
        except Exception as e:
            file.close()
            file = open(jsonData, 'w')
            json.dump({'fontMultiplier': float(1),'recentlyOpened': [], "default-theme": "dark"}, file)
            file.close()

    
    # Theme switching
    def change_theme(self):
        file = open(jsonData, "r")
        data = json.load(file)
        file.close()
        file = open(jsonData, "w+")
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            # Set light theme
            data['default-theme'] = "light"
        else:
            # Set dark theme
            data['default-theme'] = "dark"
        root.tk.call("set_theme", data['default-theme'])
        json.dump(data, file)
        file.close()

    # MacOS Menu Bar Buttons
    def setup_menu(self):
        menubar = Menu(root)
        # file
        file=Menu(menubar, tearoff=0)
        file.add_command(label="Settings", command=(lambda *args:self.run_func("Settings")))
        menubar.add_cascade(label="File", menu=file)
        # tools
        tools=Menu(menubar, tearoff=0)
        for i in sorted(list(functionalities.keys())):
            tools.add_command(label=i, command=lambda i=i: self.run_func(i))
        menubar.add_cascade(label="Tools", menu=tools)
        root.config(menu=menubar)

        # Recently Opened
        romenu=Menu(menubar, tearoff=0)
        file = open(jsonData)
        data = json.load(file)
        file.close()
        data = list(set(data['recentlyOpened']))
        for i in data:
            if i != "Home":
                romenu.add_command(label=i, command=lambda i=i: self.run_func(i))
            else:
                romenu.add_command(label=i, command=self.handleBackToHS)

        menubar.add_cascade(label="Recently Opened", menu=romenu)


    # Keybinds :D
    ## Full Screen Toggle
    def fullScreenBindings(self):
        root.attributes("-fullscreen", self.fullScreen)
        root.bind("<Control-f>", self.toggleFullScreen)
        root.bind("<F11>", self.toggleFullScreen)
        root.bind("<Escape>", self.quitFullScreen)
        root.bind("<Control-,>", (lambda e: self.run_func("Settings")))

    ## Back to Home
    def goHome(self):
        root.bind("<Control-h>", self.handleBackToHS)

    ## Reset Settings
    # def resetSettingsSC(self):
    #     root.bind("<Control-`>", self.resetSettings)

    def periodicTableScreen(self, yes):
        if yes:
            root.bind("<Return>", self.getInputs)
        else:
            root.bind("<Return>", (lambda e: self.periodicTableScreen(False)))
            root.unbind_all('<Return>')

    def removeSelectedTreeView(self):
        config.currentlySelected = "Home"
        if len(self.treeview.selection()) > 0:
            self.treeview.selection_remove(self.treeview.selection()[0])

    def handleBackToHS(self, event):
        self.removeSelectedTreeView()
        self.showHomeScreen()

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
        self.treeViewTopLab = WrappingLabel(self.newpane, text="Tools", font=(FONT, int(fontMultiplier*23), 'bold'))
        self.treeViewTopLab.pack(side="left",padx=5, anchor="w", fill="y")

        # Switching of Themes
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
            style="MainUI.Treeview",
            takefocus=False
        )

        self.treeview.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        ## Treeview columns
        self.treeview.column("#0", anchor="w", minwidth=100)

        # Insert treeview data
        for item in treeview_data:
            if item[2] in functionalities or item[0] == "" or item[1] in {8, 15, 16, 23, 24, 29, 34, 38, 41}:
                self.treeview.insert(
                    parent=item[0], index="end", iid=item[1], text=item[2]
                )
                topics.append(item[2])
                if item[0] == "" or item[1] in {8, 15, 16, 23, 24, 29, 34, 38, 41}:
                    self.treeview.item(item[1], open=True)  # Open parents
        # Select and scroll
        self.treeview.see(1)

        # Home Screen UI
        ## Main Home Screen Frame
        self.homeScreen = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.homeScreen, weight=10)
        self.notebook = tk.Canvas(self.homeScreen, highlightthickness=0)
        self.notebook.pack(fill="both", expand=True)

        ## Sizegrip
        self.sizegrip = ttk.Sizegrip(self)

        ## Show Home Screen
        self.showHomeScreen()
        
    # Function to clear the screen of any Frames (Leaving root behind)
    def clearScreen(self): 
        # Clear Right Side of the Screen
        try:
            for i in self.screenlist[::-1]:
                try:
                    i.pack_forget()
                    i.place_forget()
                except: pass
                self.screenlist.pop(-1)
        except:
            pass
        
        finally:
            try:
                self.thingFrame.pack_forget()
                self.mainFrame.pack_forget()
                self.scrolly.pack_forget()
                self.scrollx.pack_forget()
            except: pass
        
    
    def run_func(self, current):
        reload()

        file = open(jsonData)
        data = json.load(file)
        file.close()

        config.currentlySelected = current

        self.clearScreen()

        # First in First out
        if (len(data['recentlyOpened']) <= _recentlength):
            if config.currentlySelected not in data['recentlyOpened']:
                data['recentlyOpened'].insert(0, config.currentlySelected)
        else:
            data['recentlyOpened'].insert(0, config.currentlySelected)
            data['recentlyOpened'].pop(_recentlength-1)

        with open(jsonData, 'w') as f:
            json.dump(data,f)
        self.holdROItemFrame.pack_forget()

        for ropenedItem in data:
            self.ropenedItemBtn = ttk.Button(self.holdROItemFrame, text=ropenedItem, width=30)
            self.ropenedItemBtn.pack(side="top", pady=2)

        self.notebook.update()

        if config.currentlySelected in functionalities and config.currentlySelected != "Home":
            functionalities[config.currentlySelected](self)
        else:
            if config.currentlySelected != "Home":
                infoFrame(self, config.currentlySelected)

        self.setup_menu()
        root.update()

    # Function that will run when the an item in the tree is selected
    def on_tree_select(self, event):
        try: 
            self.run_func(self.treeview.item(self.treeview.selection()[0])['text'])
            self.periodicTableScreen(self.treeview.item(self.treeview.selection()[0])['text'] == "Periodic Table")
        except: pass

    # Function to create a screen to our default parameters
    def addframe(self,frame="",**args):
        if frame == "":
            frame=self.notebook
        self.screenlist.append(ttk.Frame(frame,**args))
        return self.screenlist[-1]

    def showHomeScreen(self):
        # Config
        config.currentlySelected = "Home"
        self.clearScreen()

        # Top Frame (Hello, xxx)
        self.welcomeFrame = self.addframe()
        self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
        self.helloUserLab = WrappingLabel(self.welcomeFrame,text="Hello, {}".format(config.username), font=(FONT, int(fontMultiplier*50),'bold'))
        self.helloUserLab.pack(pady=2,fill="x")
        self.welcomeLab = WrappingLabel(self.welcomeFrame, text="Welcome to Toobox!",font=(FONT, int(fontMultiplier*15)))
        self.welcomeLab.pack(side="left", fill="x")
        self.welcomeLab2 = WrappingLabel(self.welcomeFrame, text="Select a tool to get started!",font=(FONT, int(fontMultiplier*15)))
        
        # Toobox App Logo and App Description
        self.widthOfTooboxInfo = 200
        self.tooboxInfoFrame = self.addframe(width=self.widthOfTooboxInfo)
        self.tooboxInfoFrame.pack(side="left", padx=25, pady=18, anchor="w")
        appIconImg = ImageTk.PhotoImage(Image.open(appIconPng).resize((self.widthOfTooboxInfo-20,self.widthOfTooboxInfo-20), Image.ANTIALIAS))
        self.imgPanel = WrappingLabel(self.tooboxInfoFrame, image=appIconImg)
        self.imgPanel.image = appIconImg
        self.appDescText = WrappingLabel(self.tooboxInfoFrame, font=(fontMultiplier*17), wraplength=self.widthOfTooboxInfo, justify="left" ,text="Toobox is an app is a Toolbox of different tools to help in your Academics. Toobox provides various tools for a wide range of topics and subjects that will definately help you while revising and studying.")
        self.appDescText.pack(side="bottom")
        self.imgPanel.pack(side="bottom", fill="both", expand="yes", pady=32)   
        file = open(jsonData)
        data = json.load(file)
        file.close()
        data = list(set(data['recentlyOpened']))

        # Recently Opened
        self.recentlyOpenedFrame = self.addframe(width=self.widthOfTooboxInfo)
        self.recentlyOpenedFrame.pack(side="left", padx=20, pady=18, anchor="w")
        self.recentlyOpenedText = WrappingLabel(self.recentlyOpenedFrame, text="Recently Opened ({})".format(str(len(data[:3]))),font=(FONT, int(fontMultiplier*20), "bold"))
        self.recentlyOpenedText.pack(side="top", pady=3)
        self.screenlist.append(ttk.Frame(self.recentlyOpenedFrame))
        self.holdROItemFrame = self.screenlist[-1]
        self.holdROItemFrame.pack(side="top")
        if len(data) == 0:
            self.noROText = WrappingLabel(self.recentlyOpenedFrame, text="You have not opened anything recently.".format(str(len(data[:3]))),font=(FONT, int(fontMultiplier*17)), wraplength=self.widthOfTooboxInfo)
            self.noROText.pack(side="top", pady=3, anchor="w")
        else:
            for i in range(len(data[:3])): # Loop through all the Recently Opened Items
                temp=str(data[i])
                def test(x=temp):
                    return self.run_func(str(x))
                self.ropenedItemBtn = ttk.Button(self.holdROItemFrame, text=temp, width=30, command=test)
                self.ropenedItemBtn.pack(side="top", pady=2)
        
        # Credits Section
        self.creditsFrame = self.addframe(width=self.widthOfTooboxInfo)
        self.creditsFrame.pack(side="left", padx=20, pady=18, anchor="w")
        self.creditsTitle =  WrappingLabel(self.creditsFrame, text="Credits",font=(FONT, int(fontMultiplier*20), "bold"), justify="left")
        self.creditsTitle.pack(side="top", pady=3, anchor="w")
        self.developersHeader = WrappingLabel(self.creditsFrame, text="Developers:",font=(FONT, int(fontMultiplier*17), "bold"), justify="left")
        self.developersHeader.pack(side="top", anchor="w")
        self.developersList = WrappingLabel(self.creditsFrame, text="Ethan Chew, Jerick Seng, Granwyn Tan",font=(FONT, int(fontMultiplier*17)), justify="left")
        self.developersList.pack(side="top", pady=3, anchor="w")
        self.dtHeader = WrappingLabel(self.creditsFrame, text="Dependencies and Themes:",font=(FONT, int(fontMultiplier*17), "bold"), justify="left")
        self.dtHeader.pack(side="top", anchor="w")
        self.dtList = WrappingLabel(self.creditsFrame, text="chemlib, tkinter, numpy and the sun-valley Theme for tkinker",font=(FONT, int(fontMultiplier*17)), justify="left")
        self.dtList.pack(side="top", pady=3, anchor="w")

    # Destroys and 'Quits' the app
    def _quit(self):
        root.quit()
        root.destroy()

    # Function to allow for sending of notifications through AppleScript
    def notify(self, title, text, sound):
        os.system("""
                  osascript -e 'display notification "{}" with title "{}" sound name "{}"'
                  """.format(text, title, sound))

# Its a... Secret :)
f=(lambda:exec("\x69\x6d\x70\x6f\x72\x74\x20\x77\x65\x62\x62\x72\x6f\x77\x73\x65\x72\x0a\x77\x65\x62\x62\x72\x6f\x77\x73\x65\x72\x2e\x6f\x70\x65\x6e\x5f\x6e\x65\x77\x28\x22\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x79\x6f\x75\x74\x75\x62\x65\x2e\x63\x6f\x6d\x2f\x77\x61\x74\x63\x68\x3f\x76\x3d\x64\x51\x77\x34\x77\x39\x57\x67\x58\x63\x51\x22\x29"))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Toobox")

    # Simply set the theme
    root.tk.call("source", appThemePath)
    file = open(jsonData, "r")
    data = json.load(file)
    file.close()
    root.tk.call("set_theme", data['default-theme'])

    # Set App Icon
    # root.iconbitmap(appIconIcns)
    img = tk.Image("photo", file=appIconPng)
    root.tk.call('wm','iconphoto', root._w, img)

    app = App(root)
    app.pack(fill="both", expand=True)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = root.winfo_screenwidth()
    y_cordinate = root.winfo_screenheight()
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.state('zoomed')

    root.mainloop()
